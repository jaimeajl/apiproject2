**PROYECTO INDIVIDUAL Nº2**

**Telecomunicaciones**

El Internet tiene una importancia significativa en la sociedad actual y desempeña un papel fundamental en diversas áreas de la vida humana. El Internet ha transformado la forma en que vivimos, trabajamos, nos comunicamos, aprendemos y nos entretenemos. Su importancia radica en su capacidad para conectar a las personas y proporcionar acceso a una gran cantidad de recursos y oportunidades en línea.

**Objetivo**

Realizar un análisis del comportamiento de acceso a internet en el sector de telecomunicaciones. Este análisis permitirá evaluar oportunidades de crecimiento y de mejoramiento del servicio.

**Contenido**

En este trabajo se hace un análisis del comportamiento de accesos a internet, utilizando la información contenida en estos archivos .csv

Internet\_Accesos\_por\_tecnologia.csv: Archivo con la información de Año, Trimestre, Provincia, ADSL, Cablemodem, Fibra óptica, Wireless, Otros, Total.

<a name="_hlk150251358"></a>Internet\_Penetracion.csv: Archivo con la información de Año, Trimestre, Provincia, Accesos por cada 100 hogares.

Listado\_local\_con\_conec\_internet.csv: Archivo con la información de Provincia, Partido, Localidad, ADSL, Cablemódem, Dial Up, Fibra óptica, 4G, 3G, Telefonía Fija, Wireless, Satelital

**Proceso**

1. Se revisa la página web para extraer la información y se identifican las Apis con la información necesaria para desarrollar el proyecto.
1. El proceso se inicia con un ETL, que inicia con la extracción de los archivos y el ajuste de la información para poder cargarla en Powerbi. 
1. Se revisa e identificaron las columnas que permitirán resolver el problema u objetivo planteado
1. Se revisa información faltante, errores en la información y que columnas tienen menos errores
1. Se hicieron los ajustes necesarios para normalizar los datos y realizar el análisis inicial estadístico y determinar nivel de confianza
1. Se revisaron valores nulos y faltantes y se les dio tratamiento.

**EDA (Exploratory Data Analysis)**

Se hicieron varios análisis que incluyeron entre otros análisis de outliers y estadísticas descriptivas. Estos análisis se hicieron con la información de los archivos Internet\_Accesos\_por\_tecnologia.csv, Internet\_Penetracion.csv y Listado\_local\_con\_conec\_internet.csv en las columnas total y Accesos por cada 100 hogares, entre otras.

**PROCESO POWERBI**

Se carga información a Powerbi y se hace la verificación de la información ingresada.

Se generan las medidas y columnas necesarias para generar y ver la información de total de accesos, accesos por tecnología, por provincias, entre otros y que sirven para dar forma a la página inicial general y dar contexto a los Kpis definidos.

**ANALISIS GENERAL**

Para el análisis general se tomó la información del archivo de Internet\_Accesos\_por\_tecnologia.csv, el cual mostro el acceso a internet desde el año 2014 hasta el año 2022. El total de accesos del periodo de años es de 445.460 con un promedio de 515.58.

En la primera grafica se evidencia un decrecimiento acentuado desde el año 2016, que en principio es jalonado por un menor uso del servicio a través de fibra óptica.

Se muestra dentro del análisis de accesos, que existe un 82.35% de provincias con algún tipo de tecnología que permite el acceso a internet, mientras que hay un 17.65% de provincias que aun no cuenta con algún tipo de acceso.

Por otro lado en cuanto a promedio de cantidad de tecnología por provincia, la provincia de Caba cuenta con 9 tipos de tecnologías, seguidas por Buenos Aires con 4.25 y La Pampa con 4.13.

En cuanto a participación de tecnología, la tecnología 4G representa el 18.51%, seguida por el acceso con tecnología fija con el 16% y con Wireless del 16%.

El análisis por trimestre muestra una paridad entre ellos.

**Análisis Kpi 1**

El kpi 1 propuesto para el análisis del caso que evalúa aumentar en un 2% el acceso al internet para el próximo trimestre, cada 100 hogares por provincia, se encontró que tuvo un 0.65% de cumplimiento para el último trimestre de 2022 incumpliendo con el objetivo del KPI propuesto.

A nivel general se observa un crecimiento en cantidad de hogares con acceso a internet.

El promedio de accesos cada 100 hogares para el periodo fue de 69.03 hogares cada 100.

A nivel general solo 2 provincias superaron la meta propuesta y siete de ellas tuvieron un resultado negativo de un total de 24 provincias.

**Análisis Kpi 2**

Para el Kpi 2 se propone el siguiente: Incremento del 2% en accesos totales para el siguiente año (2022), con respecto al año anterior.

En este caso se evidencia que el resultado fue del -12%, que al observar la grafica de accesos por tecnología año, es jalonado por las tecnologías de Fibra óptica Cable Modem y Otros.

Las únicas tecnologías que mantuvieron su nivel de accesos fueron las de ADSL y Wireless

A nivel general año por año se ve un decrecimiento de accesos, con un pico en el año 2017. El único año en que se cumple el indicador es en el año 2016.

**Conclusiones**

A nivel general se observa un decrecimiento importante de accesos a pesar de que se observa un crecimiento sostenido de la cantidad de hogares con acceso.

La principal tecnología que jalona la cantidad de accesos es la fibra óptica, situación que se acentúa desde el año 2016.

Como aspectos a resaltar, se encontró que a la fecha existe un total de 17.65% provincias si accesos a internet, lo cual se convierte en una oportunidad para empresa.

Por otro lado se observa una gran cantidad de provincias que en promedio tienen 2 o 3 tecnologías de acceso a internet, situación que también se convierte en una oportunidad de mercado para la empresa.

El decrecimiento de accesos a través de fibra óptica, requieren un estudio adicional de que otros factores pueden estar afectando ese servicio y dependiendo del estudio también se puede convertir en una oportunidad para obtener mayor participación.





