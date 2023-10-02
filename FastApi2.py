import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI

# Cargar los DataFrames
dfsteam_games_cleaned = pd.read_csv('dfsteam_games_cleaned.csv')
dfusers_items = pd.read_csv('dfusers_items.csv')

# Combinar los DataFrames en uno solo
merged_df = dfusers_items.merge(dfsteam_games_cleaned, on='id', how='inner')

# Crear una matriz de características (usuarios x juegos) usando pivot_table
user_game_matrix = pd.pivot_table(merged_df, values='playtime_forever', index='steam_id', columns='id', fill_value=0)

# Calcular la similitud del coseno entre juegos
cosine_sim = cosine_similarity(user_game_matrix.T)

app = FastAPI()

@app.get("/playtime_genre")
def PlayTimeGenre(genre: str):
    # Filtrar juegos del género especificado en dfsteam_games_cleaned
    genre_filter = dfsteam_games_cleaned['genres'].str.contains(genre, case=False, na=False)
    juegos_genre = dfsteam_games_cleaned[genre_filter]

    # Realizar un merge entre juegos_genre y dfusers_items utilizando 'id' como clave de unión
    merged_df = juegos_genre.merge(dfusers_items[['id', 'playtime_forever']], left_on='id', right_on='id', how='inner')

    # Convertir la columna 'playtime_forever' a tipo int
    merged_df['playtime_forever'] = merged_df['playtime_forever'].astype(int)

    # Convertir la columna 'release_date' a tipo datetime si aún no lo está
    merged_df['release_date'] = pd.to_datetime(merged_df['release_date'])

    # Obtener el año con más horas jugadas
    year_with_most_playtime = merged_df.groupby(merged_df['release_date'].dt.year)['playtime_forever'].sum().idxmax()

    return {"year_with_most_playtime": year_with_most_playtime}

@app.get("/recommendations")
def get_game_recommendations(game_id: int):
    # Encuentra el índice del juego de entrada
    idx = user_game_matrix.columns.get_loc(game_id)
    # Obtén las puntuaciones de similitud para ese juego
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Ordena los juegos según la similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Obtén los 5 juegos más similares (excluyendo el juego de entrada)
    similar_games = sim_scores[1:6]
    # Obtén los IDs de los juegos recomendados
    recommended_games = [user_game_matrix.columns[i[0]] for i in similar_games]
    # Mapea los IDs de juego a los nombres de juego
    recommended_game_names = dfsteam_games_cleaned[dfsteam_games_cleaned['id'].isin(recommended_games)]['title'].tolist()
    return {"recommended_games": recommended_game_names}

# Ejecutar la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



