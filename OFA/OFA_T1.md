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

### Conjunto de datos oceano-meteorológicos

Actualmente hay un sistema de observación muy completo (in situ y remoto). Hacen falta registros largos y fiables para pronósticos, cambio climático...
**Solución numérica:** Aproximación de la realidad y aplicación de retrosimulación (hindcasting), análisis presente (nowcasting) y futuro (pronóstico, forecasting). 
Para ejecutar un modelo numerico y resolver las ecuaciones de NS necesito datos de entrada -> Ec. NS en derivadas parciales, necesidad de integrar. Necesidad de condiciones de contorno (condiciones iniciales). Una vez que parto de un estado conocido, conforme va pasando el tiempo el modelo incrementa su eficiencia. Se puede incorporar al modelo nueva información (nuevas informaciones) -> El modelo traslada la información a aquellas zonas en las que no se tiene información directa. Problema sobredefinido -> estoy entregando más información que la necesaria para que la solución se acerque a la realidad lo máximo posible.

Análisis -> Pronostico para present o futuro inmediato en el cual el modelo incorpora observaciones para dar un resultado.
Re-análisis -> serie temporal del pasado en el cual se incorporan toda la info de calidad existente.

**Se distinguen 5 niveles de procesado de info oceano-meteorológicas:**

- Nivel 0. Datos brutos sin procesado
- Nivel 1. Datos procesados a las unidades de los sensores
- Nivel 2. Variables geofísicas derivadas -> empiezo a tener T, S...
- Nivel 3. Datos georreferenciados (mallados)
- Nivel 4. Salida de modelo -> tienen en cuenta los maps without gaps.

Importancia de la resolución (tanto espacial como temporal)

Resolución 2,5ºx2,5º (1 valor de T cada x km) -> 1º = 111km (en términos de meridianos). Los paralelos están afectados por la latitud.
1 milla nautica = 1 minuto de arco meridiano -> 1º = 60 millas nauticas.

**Climatologías:** estado medio de la atmósfera y el océano y sus variabilidades dominantes. El tiempo es el estado instantáneo (variaciones que pueda haber).
Normal climática -> promedios temporales computados durante un periodo uniforme y relativamente largo, de al menos 3 decadas consecutivas. Las 3 decadas se debe a que la serie sea lo suficientemente pequeña para que las tendencias sean representativas y suficientemente grande para que las oscilaciones internas del clima no influyan en los estadísticos.












</div>
