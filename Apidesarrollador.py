import pandas as pd
from collections import defaultdict
from fastapi import FastAPI

# Inicializar FastAPI
app = FastAPI()

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("dfsteam_games_cleaned.csv")

# Añadir una columna "is_free" para indicar si el contenido es gratuito
df['is_free'] = df['price'].apply(lambda x: 'Free' in str(x) or 'Free to Use' in str(x) or 'Free to Play' in str(x))

# Definir la función para el análisis de desarrolladores
def developer(desarrollador: str):
    developer_df = df[df['developer'] == desarrollador]

    # Crear un diccionario para almacenar el recuento de elementos y el recuento de elementos gratuitos por año
    result = defaultdict(lambda: {"total_items": 0, "free_items": 0})

    for _, row in developer_df.iterrows():
        release_year = row['release_date'].split('-')[0]
        result[release_year]["total_items"] += 1
        if row['is_free']:
            result[release_year]["free_items"] += 1

    # Calcular el porcentaje de elementos gratuitos
    for year_data in result.values():
        total_items = year_data["total_items"]
        free_items = year_data["free_items"]
        if total_items > 0:
            year_data["percentage_free"] = f"{(free_items / total_items) * 100:.1f}%"
        else:
            year_data["percentage_free"] = "0%"

    return result

# Definir la ruta de la API
@app.get("/")
async def get_developer(desarrollador: str):
    developer_data = developer(desarrollador)
    return developer_data

# Ejecutar la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)








