import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI

# Cargar los datos
dfsteam_games_cleaned = pd.read_csv('dfsteam_games_cleaned.csv')
dfusers_items = pd.read_csv('dfusers_items.csv')

# Calcular la matriz TF-IDF para la columna 'title' en dfsteam_games_cleaned
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(dfsteam_games_cleaned['title'])

# Calcular la similitud del coseno entre los ítems basado en los títulos
cosine_sim_titles = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Inicializar FastAPI
app = FastAPI()

# Definir la función de recomendación de usuario
def recomendacion_usuario(user_id):
    # Filtrar los juegos que el usuario ha jugado y obtener sus IDs
    user_items = dfusers_items[dfusers_items['id'] == user_id]['id'].tolist()

    # Crear un diccionario para almacenar la puntuación total de similitud de juegos
    game_scores = {}

    # Recorrer los juegos jugados por el usuario
    for game_id in user_items:
        game_idx = dfsteam_games_cleaned[dfsteam_games_cleaned['id'] == game_id].index[0]
        sim_scores = list(enumerate(cosine_sim_titles[game_idx]))

        # Ordenar por similitud y obtener los 5 juegos más similares
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

        # Calcular la puntuación total de similitud para recomendación
        for sim_game in sim_scores:
            if sim_game[0] not in game_scores:
                game_scores[sim_game[0]] = sim_game[1]
            else:
                game_scores[sim_game[0]] += sim_game[1]

    # Ordenar los juegos recomendados por puntuación de similitud
    recommended_games = sorted(game_scores.items(), key=lambda x: x[1], reverse=True)

    # Obtener los títulos de los juegos recomendados
    recommended_titles = [dfsteam_games_cleaned.iloc[i[0]]['title'] for i in recommended_games]

    return recommended_titles

# Definir la ruta de la API
@app.get("/")
async def get_recommendations(user_id: int):
    recommended_games = recomendacion_usuario(user_id)
    return {"user_id": user_id, "recommended_games": recommended_games}

# Ejecutar la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
