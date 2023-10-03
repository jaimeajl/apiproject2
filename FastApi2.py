import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Cargar los DataFrames
dfsteam_games_cleaned = pd.read_csv('dfsteam_games_cleaned.csv')
dfusers_items = pd.read_csv('dfusers_items.csv')

# Combinar los DataFrames en uno solo
merged_df = dfusers_items.merge(dfsteam_games_cleaned, on='id', how='inner')

# Crear una matriz de características (usuarios x juegos) usando pivot_table
user_game_matrix = pd.pivot_table(merged_df, values='playtime_forever', index='steam_id', columns='id', fill_value=0)

# Calcular la similitud del coseno entre juegos
cosine_sim = cosine_similarity(user_game_matrix.T)

# Función para obtener recomendaciones basadas en un juego de entrada
def get_recommendations(input_game, cosine_sim, user_game_matrix, dfsteam_games_cleaned):
    # Encuentra el índice del juego de entrada
    idx = user_game_matrix.columns.get_loc(input_game)
    # Obtén las puntuaciones de similitud para ese juego y obtén los 5 juegos más similares
    similar_games = list(enumerate(cosine_sim[idx]))
    similar_games = sorted(similar_games, key=lambda x: x[1], reverse=True)[:5]
    # Obtén los IDs de los juegos recomendados
    recommended_games = [user_game_matrix.columns[i] for i, _ in similar_games]
    # Mapea los IDs de juego a los nombres de juego
    recommended_game_names = dfsteam_games_cleaned[dfsteam_games_cleaned['id'].isin(recommended_games)]['title'].tolist()
    return recommended_game_names

# Ejemplo de recomendaciones para un juego de entrada
input_game_id = 273350
recommendations = get_recommendations(input_game_id, cosine_sim, user_game_matrix, dfsteam_games_cleaned)
print(f"Juegos recomendados para el juego con ID {input_game_id}:")
print(recommendations)


