**PROYECTO INDIVIDUAL Nº1**

**Machine Learning Operations (MLOps)**

![IA y ML para juegos - Casos de uso y casos prácticos - AWS para videojuegos](Aspose.Words.efa58f4e-8782-431b-92b8-0b217a683388.001.png)

**¡Este es mi primer proyecto individual de la etapa de labs, en mi rol de**  

**MLOps Engineer.**

***Contexto:*** 

Un modelo de recomendación de videojuegos a través de machine learning puede mejorar significativamente la experiencia de los usuarios, aumentar las ventas y la retención de clientes, y proporcionar información valiosa sobre las preferencias de los jugadores para tomar decisiones estratégicas. En este trabajo se implementará un modelo de machine learning que incluye los procesos de Ingeniería de datos que incluye un ETL, el desarrollo de las APIs y un EDA que finaliza en la aplicación de un modelo de predicción deployado.

***Ingeniería de datos*** 

Para el trabajo y desarrollo de los procesos de ingeniería de datos se tomaron los siguientes archivos:

venv: Carpeta que incluye los archivos para creación de un ambiente virtual

word2vec\_model: archivo que contiene los vectores de palabras entrenados usando el algoritmo Word2Vec.

.gitattributes: archivo de configuración utilizado en el sistema de control de versiones Git

dfsteam\_games\_cleaned: archivo con la informacion de géneros, títulos de juegos, precio, desarrollador, entre otros.

user\_reviews: archivo con la información de identificador de usuario y la reviews de los juegos.

dfusers\_items: archive con la informacion de tiempo de uso, URL, identificador único de usuario, entre otros.

df\_merged: archivo que incluye la información de las columnas: genres, title, release\_date, id, user\_id, steam\_id, playtime\_forever y que vienen de los archivos dfsteam\_games\_cleaned, user\_reviews y dfusers\_items.

df\_merged\_cleanfinal: archivo que incluye la información de las columnas: genres, release\_date, id, user\_id, playtime\_forever, title y la columna sentiment\_analysis

df\_merged\_cleanfinalA: archivo que incluye la información de las columnas: genres, release\_date, id, user\_id, playtime\_forever, title y que deja el primer genero como principal de la columna genres

EDA-1: archivo que incluye el EDA de la información del archivo df\_merged.

Apidesarrollador: archivo con la función def developer( desarrollador : str ): Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

Apigenero: archivo con la función def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

Apiano: archivo con la función def best\_developer\_year( año : int ): Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)

Apidesarrolladora: archivo con la función def developer\_reviews\_analysis( desarrolladora : str ): Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

ModeloML: archivo con el modelo de ML de relación ítem-ítem

ETL-1: archivo con el ETL realizado a la información de los archivos JSON steam\_games.json, user\_reviews.json y users\_items.json




***ETL (Extraction, transform y load)***

El proceso de ETL consistió en la extracción de la información de los archivos .Json steam\_games.json, user\_reviews.json y users\_items.json, para los cuales se les realizo una verificación de la información y columnas que contenían, se eliminaron las columnas que no son necesarias, una limpieza de valores nulos y una transformación del tipo de datos para asegurar los resultados posteriores. 

Adicionalmente se realizaron pruebas para comprobar que los ajustes realizados a la información y a las columnas trajeran los datos correctos en la solicitud y finalmente esta información fue guardada en los archivos .csv dfsteam\_games\_cleaned, user\_reviews y dfusers\_items.

***Desarrollo de las APIs***

Para el desarrollo de las Apis se tomaron la información de los archivos dfsteam\_games\_cleaned.csv, dfusers\_items.csv y user\_reviews.csv y se utilizaron la biblioteca pandas y fastapi. 

Las funciones que se desarrollaron fueron las siguientes: 

1. def developer( desarrollador : str ) con la cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.
1. def UserForGenre( genero : str ) que debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
1. def best\_developer\_year( año : int ) que devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)
1. def developer\_reviews\_analysis( desarrolladora : str ) que según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

A las anteriores funciones se les hizo el deployment a través de Fastapi, para que pudieran ser consumidas desde la web 

***EDA (Exploratory Data Analysis)***

El EDA se ejecuto en el archivo EDA-1 en incluyo el análisis de Estadísticas descriptivas para la columna playtime\_forever, genres y title.

Se observo que para la información de la columna playtime\_forever la desviación estándar fue de std: 12153, lo que nos indica una gran dispersión frente a la media que fue del mean: 1555.

Por otro lado se encontró que en la columna genres, el genero que mayor cantidad de juegosparticipa es el genero Action con 180,  seguido por el genero Strategy con 76.

Se genero un histograma de la columna 'playtime\_forever, que nos mostro que la participación del tiempo cero es la mayor dentro de la muestra. También se hizo un boxplot sobre esta misma información encontrando outliers en el rango cercano a los 340000, 100000 y 95000 minutos.

Por otro lado se utilizaron herramientas que nos mostraron mediante grafica de barras la participación del top 80 (37 géneros) de los géneros que más participan en el total y que permitieron una mejor comprensión de la distribución de géneros en toda la data.

Se utilizo la herramienta WordCloud para generar una nube de palabras para revisar los mas destacados en géneros y títulos de juego, encontrando el género Action y el juego Game War como los mas destacados.

Se genero un grafico de dispersión para ver las fechas año en los cuales hubo mas tiempo de juego y se encontró que a partir del año 2004 se incrementa el tiempo, aunque la mayoría con tiempo de juego cero.

Por ultimo se crear un gráfico de dispersión para playtime\_forever vs title que nos muestra la participación del 80% de videojuegos de los cuales 4 tienen mas de 50000 minutos de juego.


***Modelo de machine learning***

El modelo de machine se ejecuto en el archivo ModeloML.ipynb y se escogió la opción de un sistema de recomendación que tiene una relación ítem-ítem. Para el modelo se utilizo el modulo klearn el cual crear una instancia de TfidfVectorizer para transformar el texto a vectores TF-IDF y  construye la matriz TF-IDF con la columna 'genres'.

Posteriormente se crea el modelo KNN que ubica los generos mas cercanos y finalmente se entrena para que sea capaz de generalizar a nuevos datos.

Por ultimo para evaluar el modelo se utilizan las métricas KFold, Recall y F1\_score para evaluar el modelo.

Este modelo se ubica en render para que pueda ser consumido en la ruta: <https://apipersonalproject2v2.onrender.com>.

***Conclusiones***

El proceso de desarrollar un sistema de recomendación basado en machine learnig incluye varias etapas que van desde la exploración de la información que se tanga sobre la recomendación de video juegos, su uso, y otros factores asociados. Pueden haber diferentes modelos de desarrollo de un sistema de recomendación y cada uno ofrece una serie de ventajas o desventajas que se deben analizar para cumplir con el objetivo o necesidad y se deben al analizar al momento de la planeación del proyecto. Por ultimo es importante evaluar el modelo con datos reales de los usuarios para poder contrastar la información que entrega este y que realmente sea útil para los usuarios.










"# projectindiv2" 
