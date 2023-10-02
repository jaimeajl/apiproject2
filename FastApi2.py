import pandas as pd
import numpy as np
import json
import ast
from pandas import json_normalize

# Cargamos el json en un dataframe
data = []
with open('steam_games.json') as e:
    for line in e:
        data.append(json.loads(line))
dfsteam_games = pd.DataFrame(data)

dfsteam_games.head()

dfsteam_games = dfsteam_games.drop(['publisher', 'app_name', 'url', 'tags', 'reviews_url', 'specs', 'price', 'early_access', 'developer'], axis=1)


dfsteam_games.head()

# Contar filas con valores nulos
filas_con_nulos = dfsteam_games.isnull().sum(axis=1)
total_filas = len(dfsteam_games)

# Calcular porcentaje de filas con valores nulos
porcentaje_nulos = (filas_con_nulos / total_filas) * 100

# Imprimir resultados
print(f"Total de filas con valores nulos: {filas_con_nulos.sum()}")
print(f"Porcentaje de filas con valores nulos: {porcentaje_nulos.mean()}%")

# Número de filas antes de eliminar NaN
num_filas_antes = len(dfsteam_games)
print("Total de filas:", num_filas_antes)

# Eliminar filas con NaN y crear el nuevo DataFrame
dfsteam_games_cleaned = dfsteam_games.dropna()

# Número de filas después de eliminar NaN
num_filas_despues = len(dfsteam_games_cleaned)
print("Total de filas despues drop:", num_filas_despues )

# Calcular el total de filas eliminadas
total_filas_eliminadas = num_filas_antes - num_filas_despues

print("Total de filas eliminadas:", total_filas_eliminadas)

# Contar filas con valores nulos
filas_con_nulos = dfsteam_games_cleaned.isnull().sum(axis=1)
total_filas = len(dfsteam_games_cleaned)

# Calcular porcentaje de filas con valores nulos
porcentaje_nulos = (filas_con_nulos / total_filas) * 100

# Imprimir resultados
print(f"Total de filas con valores nulos: {filas_con_nulos.sum()}")
print(f"Porcentaje de filas con valores nulos: {porcentaje_nulos.mean()}%")

# Imprimir los primeros juegos del DataFrame
print(dfsteam_games_cleaned.head())

# Imprimir información sobre el DataFrame
print(dfsteam_games_cleaned.info())


# import numpy as np

# Reemplazar "Soon.." con NaN
dfsteam_games_cleaned['release_date'].replace("Soon..", np.nan, inplace=True)

# Convertir la columna a datetime
dfsteam_games_cleaned['release_date'] = pd.to_datetime(dfsteam_games_cleaned['release_date'], errors='coerce')

# import numpy as np

# Reemplazar "Soon.." con NaN
dfsteam_games_cleaned['release_date'].replace("Soon..", np.nan, inplace=True)

# Convertir la columna a datetime
dfsteam_games_cleaned['release_date'] = pd.to_datetime(dfsteam_games_cleaned['release_date'], errors='coerce')

dfsteam_games_cleaned.head()

# Convierte la lista de géneros en una cadena de texto separada por comas
dfsteam_games_cleaned['genres'] = dfsteam_games_cleaned['genres'].apply(lambda x: ', '.join(x))

# Ahora, la columna 'genres' contiene una cadena de texto con los géneros separados por comas

dfsteam_games_cleaned.head()


# ID que deseas consultar (interpretado como int)
id_a_consultar = 761140

# Fecha que deseas buscar
fecha_a_buscar = '2018-01-04'

# Convierte la columna 'id' a tipo int para la comparación
dfsteam_games_cleaned['id'] = dfsteam_games_cleaned['id'].astype(int)

# Convierte la columna 'release_date' a tipo datetime para la comparación
dfsteam_games_cleaned['release_date'] = pd.to_datetime(dfsteam_games_cleaned['release_date'])

# Verifica si el ID tiene la fecha '2018-01-04' en la columna 'release_date'
id_tiene_fecha = (dfsteam_games_cleaned['id'] == id_a_consultar) & (dfsteam_games_cleaned['release_date'] == fecha_a_buscar)

if id_tiene_fecha.any():
    print(f"El ID {id_a_consultar} tiene asociada la fecha '{fecha_a_buscar}' en la columna 'release_date'.")
else:
    print(f"El ID {id_a_consultar} no tiene asociada la fecha '{fecha_a_buscar}' en la columna 'release_date'.")


    # ID que deseas consultar
id_a_consultar = 761140

# Género que deseas buscar
genero_a_buscar = 'Action'

# Convierte la columna 'id' a tipo int para la comparación
dfsteam_games_cleaned['id'] = dfsteam_games_cleaned['id'].astype(int)

# Verifica si el ID tiene el género 'Action' en la columna 'genres'
id_tiene_genero_action = (dfsteam_games_cleaned['id'] == id_a_consultar) & (dfsteam_games_cleaned['genres'].str.contains(genero_a_buscar))

if id_tiene_genero_action.any():
    print(f"El ID {id_a_consultar} tiene asociado el género '{genero_a_buscar}' en la columna 'genres'.")
else:
    print(f"El ID {id_a_consultar} no tiene asociado el género '{genero_a_buscar}' en la columna 'genres'.")


    # Valor que deseas buscar como número entero
id_a_buscar = 761140

# Verifica si el valor está en la columna 'id' como número entero
id_encontrado = (dfsteam_games_cleaned['id'].astype(int) == id_a_buscar).any()

if id_encontrado:
    print(f"El ID {id_a_buscar} se encuentra en la columna 'id' como un número entero.")
else:
    print(f"El ID {id_a_buscar} no se encuentra en la columna 'id' como un número entero.")


primera_fila = dfsteam_games_cleaned.iloc[0]

# Imprime la información de la primera fila
print(primera_fila)

# Guardar el DataFrame como un archivo CSV
dfsteam_games_cleaned.to_csv(r'C:\Users\jaime\OneDrive\Escritorio\Henry\Proyectos\Proyectopersonal1\2intento\archivos csv\dfsteam_games_cleaned.csv', index=False)

# EXTRAER JSON user_reviews.json

# Leer el contenido del archivo user_reviews.json
with open('user_reviews.json', "r", encoding='utf-8') as f:
    data = f.readlines()
    
# Convertir la lineas a registros JSON
records = [eval(line.strip()) for line in data]

df_user_reviews = pd.DataFrame(records)

df_user_reviews.head()

df_user_reviews = df_user_reviews.drop(['user_url'], axis=1)

df_user_reviews.head()

# Contar filas con valores nulos
filas_con_nulos1 = df_user_reviews.isnull().sum(axis=1)
total_filas1 = len(dfsteam_games)

# Calcular porcentaje de filas con valores nulos
porcentaje_nulos1 = (filas_con_nulos1 / total_filas1) * 100

# Imprimir resultados
print(f"Total de filas con valores nulos: {filas_con_nulos1.sum()}")
print(f"Porcentaje de filas con valores nulos: {porcentaje_nulos1.mean()}%")

# Imprimir los primeros juegos del DataFrame
print(df_user_reviews.head())

# Imprimir información sobre el DataFrame
print(df_user_reviews.info())



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

df_user_reviews.to_csv(r'C:\Users\jaime\OneDrive\Escritorio\Henry\Proyectos\Proyectopersonal1\2intento\archivos csv\user_reviews.csv', index=False)



# EXTRAER JSON users_items.json


# Leer el contenido del archivo users_items.json
with open('users_items.json', "r", encoding='utf-8') as f:
    data = f.readlines()
    
# Convertir la lineas a registros JSON
records = [eval(line.strip()) for line in data]

dfusers_items = pd.DataFrame(records)

dfusers_items.head()

# Suponiendo que tu DataFrame se llama 'df'
columnas = dfusers_items.columns
print(columnas)

dfusers_items = dfusers_items.drop(['items_count', 'user_url', ], axis=1)

dfusers_items.head()

dfusers_items['playtime_forever'] = dfusers_items['items'].apply(lambda x: x[0].get('playtime_forever') if len(x) > 0 else 0)
dfusers_items['playtime_2weeks'] = dfusers_items['items'].apply(lambda x: x[0].get('playtime_2weeks') if len(x) > 0 else 0)
dfusers_items['id'] = dfusers_items['items'].apply(lambda x: x[0].get('item_id') if len(x) > 0 else 0)
dfusers_items['playtime_forever'] = dfusers_items['playtime_forever'].astype(int)
dfusers_items['playtime_2weeks'] = dfusers_items['playtime_2weeks'].astype(int)

dfusers_items.head()

dfusers_items.drop(['items'], axis=1, inplace=True)

dfusers_items.drop(['playtime_2weeks'], axis=1, inplace=True)

dfusers_items.head()

# import pandas as pd

# Supongamos que ya tienes el DataFrame dfusers_items cargado

# Convertir la columna 'id' a valores numéricos
dfusers_items['id'] = pd.to_numeric(dfusers_items['id'], errors='coerce')

# La opción 'errors' con valor 'coerce' transformará los valores no numéricos en NaN

# Verificar que la columna 'id' ahora contiene valores numéricos
print(dfusers_items.dtypes)


# import pandas as pd

# Verifica el DataFrame dfsteam_games_cleaned
if dfsteam_games_cleaned['id'].apply(lambda x: isinstance(x, (int, float))).all():
    print("Todos los valores en la columna 'id' de dfsteam_games_cleaned son numéricos.")
else:
    print("La columna 'id' de dfsteam_games_cleaned contiene valores no numéricos.")

# Verifica el DataFrame dfusers_items
if dfusers_items['id'].apply(lambda x: isinstance(x, (int, float))).all():
    print("Todos los valores en la columna 'id' de dfusers_items son numéricos.")
else:
    print("La columna 'id' de dfusers_items contiene valores no numéricos.")


 #    import pandas as pd

# Supongamos que ya tienes los DataFrames dfsteam_games_cleaned y dfusers_items cargados

# Filtrar juegos del género "Action" en dfsteam_games_cleaned
juegos_action = dfsteam_games_cleaned[dfsteam_games_cleaned['genres'].str.contains('Adventure', case=False, na=False)]

# Realizar un merge entre juegos_action y dfusers_items utilizando 'id' como clave de unión
merged_df = juegos_action.merge(dfusers_items[['id', 'playtime_forever']], left_on='id', right_on='id', how='inner')

# Convertir la columna 'playtime_forever' a tipo int
merged_df['playtime_forever'] = merged_df['playtime_forever'].astype(int)

# Convertir la columna 'release_date' a tipo datetime si aún no lo está
merged_df['release_date'] = pd.to_datetime(merged_df['release_date'])

# Obtener el año con más horas jugadas
year_with_most_playtime = merged_df.groupby(merged_df['release_date'].dt.year)['playtime_forever'].sum().idxmax()

print(f"Año con más horas jugadas para el género 'Adventure': {year_with_most_playtime}")


# import pandas as pd
from fastapi import FastAPI

# Supongamos que ya tienes los DataFrames dfsteam_games_cleaned y dfusers_items cargados
# También supongamos que ya tienes FastAPI configurado

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