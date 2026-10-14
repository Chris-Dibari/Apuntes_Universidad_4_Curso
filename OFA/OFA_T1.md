<style>
img {
    width: 30% !important; /* Forzamos el tamaño con !important */
    max-width:30% !important;
    display: block;
    margin: 0 auto !important; /* Centrado obligatorio */
}

/* Esto asegura que se aplique al exportar a PDF */
p, li, div, h2, h3 {
    text-align: justify !important;
}
</style>

<!-- Usamos el atributo 'align' que es el único que la vista previa y el PDF respetan a la vez -->
<div align="justify">

# Oceanografía Física Aplicada - 4 Curso CC del Mar

## Índice de la asignatura:

- TEMA 1. Visualización de datos oceanográficos y atmosféricos.
- TEMA 2. Climatologías y reanálisis. Salidas de modelos de atmósfera y océano y datos observados.
- TEMA 3. Análisis de series temporales de variables oceanográficas/meteorológicas.
- TEMA 4. Técnicas de análisis espacial.
- TEMA 5. Modelado numérico como herramienta de diagnóstico y pronóstico de procesos físicos.
- TEMA 6. Herramientas de visualización y análisis: NCVIEW, Ferret, CDO, Python, ODV.


##  Oceanografía Física Aplicada - TEMA 1. Visualización de datos oceanográficos y atmosféricos.

**Large data sets, data formats and NetCDF.**
Antigüedad -> grandes atlantes con información.
Un mes de datos (con frecuencia de cada 6h -> mínima cantidad de valores a lo largo de día que me permite reconstruir el ciclo diurno - ciclo sinoptico). => equivaldría a 30GB. En 100 = 36TB -> una columna de DVD de 11m de alto.

Utilizando dichos datos se pueden llevar a cabo distintos análisis -> visualización de fenómenos, series temporales, climatología...

Los datos se organizan en matrices (arrays) -> Ej. 2D: columnas = longitudes y filas = latitudes.
Representación en 3D -> la tercera dimensión puede ser profundidad en el océano, altura en la atmósfera o incluso el tiempo.
Importancia de entender la estructura del conjunto de datos.

Missing value -> valor anómalo (ej: $-9,999e^{-20}$). Valores que a la hora de graficar o realizar cálculos no se tendrá en cuenta por el sistema.

**Principales formatos de datos:**

- Datos ASCII (American standard code for information interchange) -> el procesador entiende un formato binario, dicho codigo le convierte el binario en valores. Es un esquema de codificación de caracteres basado en el alfabeto inglés. Representan el texto en computadora.
- Datos binario -> en función de la longitud de la palabra que lea mi ordenador, se tienen limitaciones de precisión -> número de bytes. No es lo mismo leer un valor de 16 bits que con 8 bits. Se utiliza dado que son más comprimidos -> un fichero de datos binario ocupa aprox la mitad de un fichero de valores en texto.
- Datos autodescrito NetCDF (network common data form) -> formato independiente de la arquitectura de la máquina que permite la creación, acceso e intercambio de datos científicos. Tiene un encabezado que permite conocer la descripción del conjunto de datos (dimensiones, autores, nombres variables...) esto permite no solo intercambiando información del fichero sino que también incluye una especie de guía de usuario. Importancia de dimensiones, atributos y variables del fichero.






</div>
