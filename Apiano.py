import pandas as pd

from fastapi import FastAPI

# Inicializar FastAPI
app = FastAPI()

def best_developer_year(año):
    # Cargar los datos desde los archivos CSV
    dfusers_items = pd.read_csv("dfusers_items.csv")
    user_reviews = pd.read_csv("user_reviews.csv")
    dfsteam_games_cleaned = pd.read_csv("dfsteam_games_cleaned.csv")

    # Realizar los joins
    merged_data = dfusers_items.merge(user_reviews, on="user_id").merge(dfsteam_games_cleaned, left_on="id", right_on="id")

    # Filtrar los juegos lanzados en el año especificado
    juegos_del_año = merged_data[merged_data["release_date"].apply(lambda x: str(año) in str(x))]

    # Filtrar los juegos con valores de fecha de lanzamiento válidos (no NaN)
    juegos_del_año = juegos_del_año[juegos_del_año["release_date"].notna()]

    # Convertir la columna "sentiment_analysis" a tipo int
    juegos_del_año["sentiment_analysis"] = juegos_del_año["sentiment_analysis"].astype(int)

    # Considerar '2' como recomendación positiva
    juegos_del_año = juegos_del_año[juegos_del_año["sentiment_analysis"] == 2]

    # Agrupar por desarrollador y contar las recomendaciones positivas
    developer_ratings = juegos_del_año.groupby("developer")["sentiment_analysis"].count().reset_index()

    # Ordenar por las recomendaciones positivas en orden descendente
    developer_ratings = developer_ratings.sort_values(by="sentiment_analysis", ascending=False)

    # Verificar si hay al menos 3 desarrolladores antes de intentar acceder a los 3 primeros
    if len(developer_ratings) >= 3:
        top_3_developers = developer_ratings.head(3)
    else:
        top_3_developers = developer_ratings

    # Crear el formato deseado de resultado
    result = [{"Puesto 1": top_3_developers.iloc[0]["developer"] if len(top_3_developers) >= 1 else None},
              {"Puesto 2": top_3_developers.iloc[1]["developer"] if len(top_3_developers) >= 2 else None},
              {"Puesto 3": top_3_developers.iloc[2]["developer"] if len(top_3_developers) >= 3 else None}]

    return result

# Definir la ruta de la API
@app.get("/")
async def Get_best_developer_year(año):
    developer_data = best_developer_year(año)
    return developer_data

# Ejecutar la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



