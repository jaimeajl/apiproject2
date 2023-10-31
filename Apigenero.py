import pandas as pd
from fastapi import FastAPI

# Inicializar FastAPI
app = FastAPI()

# Cargar los DataFrames
df_users_items = pd.read_csv('dfusers_items.csv')
df_steam_games_cleaned = pd.read_csv('dfsteam_games_cleaned.csv')

# Hacer un join entre los DataFrames
df_merged = pd.merge(df_users_items, df_steam_games_cleaned, on='id')

def UserForGenre(genero: str):
    # Filtrar por el género dado
    df_genre = df_merged[df_merged['genres'].str.contains(genero, case=False)]

    if df_genre.empty:
        return f"No hay datos disponibles para el género {genero}"

    # Agregar las horas jugadas por usuario y año
    df_genre['release_date'] = pd.to_datetime(df_genre['release_date'])
    df_genre['year'] = df_genre['release_date'].dt.year
    hours_played_by_user_and_year = df_genre.groupby(['user_id', 'year'])['playtime_forever'].sum().reset_index()

    # Encontrar el usuario con más horas jugadas
    max_hours_user = hours_played_by_user_and_year.groupby('user_id')['playtime_forever'].sum().idxmax()

    # Filtrar las horas jugadas por el usuario con más horas jugadas
    user_hours = hours_played_by_user_and_year[hours_played_by_user_and_year['user_id'] == max_hours_user]

    # Convertir el resultado a un formato específico
    max_hours = round(user_hours['playtime_forever'].max() / 60, 2)  # Redondear a 2 decimales
    user_hours_list = [{'Año': int(row['year']), 'Horas': int(row['playtime_forever'] / 60)} for _, row in user_hours.iterrows()]

    return {
        f"Usuario con más horas jugadas para {genero}": max_hours_user,
        "Horas jugadas": max_hours,
        "Detalle por año": user_hours_list
    }

# Definir la ruta de la API
@app.get("/")
async def Get_UserForGenre(genero: str):
    developer_data = UserForGenre(genero).

    return developer_data

# Ejecutar la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)










