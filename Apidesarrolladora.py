import pandas as pd
from fastapi import FastAPI

# Inicializar FastAPI
app = FastAPI()

# Cargar los DataFrames
df_users_items = pd.read_csv('dfusers_items.csv')
user_reviews = pd.read_csv('user_reviews.csv')
df_steam_games_cleaned = pd.read_csv('dfsteam_games_cleaned.csv')

# Hacer un join entre los DataFrames
df_merged = pd.merge(df_users_items, user_reviews, on='user_id')
df_merged = pd.merge(df_merged, df_steam_games_cleaned, on='id')

def developer_reviews_analysis(desarrolladora: str):
    # Filtrar por el desarrollador dado
    df_developer = df_merged[df_merged['developer'] == desarrolladora]

    if df_developer.empty:
        return f"No hay datos disponibles para el desarrollador {desarrolladora}"

    # Contar los registros de reseñas positivas (sentiment_analysis == 2) y negativas (sentiment_analysis == 0)
    positive_reviews = df_developer[df_developer['sentiment_analysis'] == 2].shape[0]
    negative_reviews = df_developer[df_developer['sentiment_analysis'] == 0].shape[0]

    return {desarrolladora: {'Positive': positive_reviews, 'Negative': negative_reviews}}

# Definir la ruta de la API
@app.get("/")
async def Get_developer_reviews_analysis(desarrolladora: str):
    developer_data = developer_reviews_analysis(desarrolladora)
    return developer_data

# Ejecutar la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
