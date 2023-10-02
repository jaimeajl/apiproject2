import pandas as pd

# import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Descargar el léxico VADER si aún no lo has hecho
nltk.download('vader_lexicon')

# Crear una instancia de SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

# Función para asignar un valor de sentimiento a cada reseña
def assign_sentiment(review):
    if isinstance(review, str):
        sentiment_scores = sid.polarity_scores(review)
        compound_score = sentiment_scores['compound']

        if compound_score >= 0.05:
            return 2  # Positivo
        elif compound_score <= -0.05:
            return 0  # Malo
        else:
            return 1  # Neutral
    else:
        return 1  # Valor por defecto si no hay reseña escrita

# Aplicar la función de análisis de sentimientos a la columna 'reviews' y reemplazar 'reviews'
df_user_reviews['sentiment_analysis'] = df_user_reviews['reviews'].apply(assign_sentiment)
df_user_reviews.drop(columns=['reviews'], inplace=True)

print("Análisis de sentimientos completado y columna 'reviews' reemplazada por 'sentiment_analysis' en el DataFrame.")

df_user_reviews.to_csv(r'C:\Users\jaime\Desktop\Henry\Proyectopersonal1\user_reviews.csv', index=False)



# import pandas as pd

from fastapi import FastAPI

# Cargar los DataFrames desde los archivos CSV
dfsteam_games_cleaned = pd.read_csv(r'C:\Users\jaime\Desktop\Henry\Proyectopersonal1\dfsteam_games_cleaned.csv')
dfusers_items = pd.read_csv(r'C:\Users\jaime\Desktop\Henry\Proyectopersonal1\dfusers_items.csv')

app = FastAPI()

@app.get("/playtime_genre/{genre}")
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
