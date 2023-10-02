import pandas as pd
import numpy as np
import json
import ast
from pandas import json_normalize

# import pandas as pd
from fastapi import FastAPI

# Supongamos que ya tienes los DataFrames dfsteam_games_cleaned y dfusers_items cargados
# También supongamos que ya tienes FastAPI configurado

#dfsteam_games_cleaned = pd.read_csv(r'C:\Users\jaime\Desktop\Henry\Proyectopersonal1\dfsteam_games_cleaned.csv')
#dfusers_items = pd.read_csv(r'C:\Users\jaime\Desktop\Henry\Proyectopersonal1\dfusers_items.csv')

dfsteam_games_cleaned = pd.read_csv('dfsteam_games_cleaned.csv')
dfusers_items = pd.read_csv('dfusers_items.csv')

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

# Ejecutar la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

