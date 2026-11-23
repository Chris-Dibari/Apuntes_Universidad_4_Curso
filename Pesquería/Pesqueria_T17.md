<style>
img {
    width: 60% !important; /* Forzamos el tamaño con !important */
    max-width:60% !important;
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

##  Pesquerías. TEMA 17. Modelos analíticos.

Estos modelos están basados en las características biológicas del stock. El APV reconstruye la abundancia y la mortalidad por pesca de una cohorte a partir de sus capturas a lo largo del tiempo.
En un stock sin pesca y en equilibrio, el reclutamiento (R) y el crecimiento (C) compensan las pérdidas de biomasa por mortalidad natural (M).

Cuando una población es sometida a pesca, ésta tiene efecto sobre todos los otros factores:

- Aumenta el reclutamiento;
- Aumenta la tasa de crecimiento;
- Se reduce la mortalidad natural.

En poblaciones no explotadas, se establece una situación de equilibrio en la cual ENTRADAS = SALIDAS.
La población crece hasta “ocupar todo el espacio disponible”.

- La pesca crea "espacio" para una mayor cantidad de nuevos reclutas (menos densidad deja más alimento y favorece el crecimiento o la supervivencia).
- La pesca extrae los peces grandes de crecimiento lento que son reemplazados por peces pequeños de crecimiento rápido.
- La pesca remueve peces antes que estos puedan morir de viejos o por otras causas naturales.

La pesca tiene un efecto estimulante sobre la producción de peces (puede compensar parte de la biomasa extraída por la pesca), siempre y cuando se le dé al stock suficiente tiempo para ajustarse a la nueva situación y en tanto la presión de pesca no llegue a ser demasiado intensa. La "sobrepesca“ afecta a las entradas:
- primero el crecimiento individual de los peces (se capturan peces demasiado pequeños y se pierde rendimiento potencial en peso por recluta) (SOBREPESCA DE CRECIMIENTO)
- cuando llega a ser muy severa, también al reclutamiento (la pérdida de reproductores compromete la reposición del stock). (SOBREPESCA DE RECLUTAMIENTO).

La variación de la biomasa de un stock no explotado en el tiempo depende de la propia dinámica poblacional en la que actúa el crecimiento y la mortalidad natural.

![alt text](<imagenes-4-curso/peces.17.1.png>)

Todo esto lo recoge el modelo de Beverton y Holt:

![alt text](<imagenes-4-curso/peces.17.2.png>)

![alt text](<imagenes-4-curso/peces.17.3.png>)

![alt text](<imagenes-4-curso/peces.17.4.png>)

Y/R se considera una función de F (mortalidad por peca) y Tc (tiempo de primera captura). Frecuentemente se verá graficado Y/R contra F(o el esfuerzo). El modelo permite comparar dos decisiones: ¿Cuánto pescar? F resume la mortalidad por pesca. Si la capturabilidad se mantiene constante, F es proporcional al esfuerzo. ¿Desde qué edad capturar? La selectividad del arte influye en t꜀. El crecimiento permite relacionarla con una talla. Los parámetros F y Tc son aquellos que pueden ser controlados por los administradores, porque:

1) F es proporcional al esfuerzo de pesca
2) Tc es una función de selectividad del arte

La ordenación pesquera según este modelo se puede dirigir a:

- MODIFICAR LA MORTALIDAD POR PESCA
- CAMBIAR LA TALLA DE 1ª CAPTURA
- CAMBIAR AMBAS COSAS

Se generan diferentes valores de F y Tc (edad primera captura) para evaluar su efecto sobre el rendimiento por recluta.

La supervivencia combina dos pérdidas: mortalidad natural y mortalidad por pesca. 

Supuestos de la versión clásica:
- Reclutamiento constante para interpretar el rendimiento de equilibrio.
- Los peces de una cohorte nacen en la misma fecha y se incorporan al stock a una edad común. La selectividad cambia de forma brusca en t꜀.
- M es constante. F es constante en la fase explotada.
- Los individuos se mezclan dentro del stock.
- El crecimiento sigue Von Bertalanffy y la relación talla-peso supone W = aL³ (isométrica).
- Los parámetros se mantienen constantes al comparar escenarios. El modelo no predice la respuesta del reclutamiento a la pérdida de reproductores.

**Análisis de la población virtual: APV.**

![alt text](<imagenes-4-curso/peces.17.5.png>)

$N_1$ = primer año.
Se supone entrada ya en la fase explotada.

La suma de las capturas de una cohorte indica un mínimo de individuos que tuvo que existir. El tamaño inicial también incluye las muertes naturales y los supervivientes. Es denominada stock utilizado o población virtual.

El APV, considera a las poblaciones desde una perspectiva histórica. El APV reconstruye el pasado de la población con series de capturas por edad.
Esa reconstrucción sirve de punto de partida para proyectar escenarios. Predecir capturas futuras exige supuestos sobre reclutamiento, mortalidad y pesca.
EL APV ha permitido recurrir a las series históricas de abundancia de muchos stocks marinos explotados boreales y templados, de los que existían series de tiempo relativamente largas de capturas y muestreos de esas capturas que permitieron determinar las clases de edad o tamaño.

El APV sí incorpora M. La incertidumbre surge al estimar M, las capturas por edad y la abundancia o F del intervalo terminal.

![alt text](<imagenes-4-curso/peces.17.6.png>)

EJEMPLO EN EQUILIBRIO: las cohortes entran con igual número de reclutas (Reclutamiento constante) y siguen las mismas tasas de mortalidad. Es una simplificación del ejemplo, no un requisito general del APV.

![alt text](<imagenes-4-curso/peces.17.7.png>)

Los "análisis de población virtual (APV)“ son métodos que miran hacia el pasado, usando datos "históricos", y que consisten en la Estimación de las tasas instantáneas de mortalidades por pesca y abundancias por clases de edad a partir de la estructura demográfica de las capturas.

![alt text](<imagenes-4-curso/peces.17.8.png>)

Información necesaria:

La tasa instantánea de mortalidad natural a la que está sometida una cohorte. En APV monoespecífico se considera constante.

- La CAPTURA TOTAL (en número por edad y año) es un dato que puede ser suministrado por diversos organismos oficiales, administrativos.
- Una estimación de M. En los ejemplos básicos se toma constante, aunque puede variar por edad.
- Una F (mortalidad por pesca) o abundancia terminal para comenzar la reconstrucción.
También se puede determinar mediante MUESTRAS REPRESENTATIVAS (edad o talla):
➢ grupos de edad (métodos basados en la edad)
➢ grupos de tallas (métodos basados en las tallas)
Los desembarques totales pueden no incluir todas las capturas: hay que considerar descartes y otras extracciones relevantes.

El APV analiza las capturas logradas por la pesca comercial, obtenidas a través de estadísticas pesqueras, con información detallada sobre la contribución de cada cohorte a la captura total, la cual se obtiene por medio de programas de muestreo y lecturas de edad.

DE LA MUESTRA A LAS CAPTURAS POR EDAD
1. Tomamos muestras representativas de la pesquería.
2. Medimos tallas y estimamos edades.
3. Elevamos la composición de la muestra a las capturas totales.

Estructuras utilizadas según la especie:
- Peces: otolitos, escamas, radios u otras estructuras validadas.
- Cefalópodos: estatolitos y, en algunos casos, picos.
- Bivalvos: marcas de crecimiento en las valvas.
- Crustáceos: la muda dificulta la estimación de edad.

La periodicidad de las marcas debe validarse. Las distribuciones de tallas también aportan información sobre las cohortes.

Se deben preparar tablas que contengan el desembarque total en número de individuos, por edad o tallas, por año o por mes, antes de comenzar el análisis.

Esta información se obtiene a partir de:
• Datos de capturas de años sucesivos
• Distribución las capturas en edades a partir de distribuciones de tallas, de escamas, etc.

Las capturas en número de ejemplares sobre la cohorte en cada intervalo (el intervalo suele tener una duración de 1 año).
Esta información se obtine de la distribución de tallas en la captura y los estudios de crecimiento y edad.

![alt text](<imagenes-4-curso/peces.17.9.png>)

![alt text](<imagenes-4-curso/peces.17.10.png>)

De que depende la fiabilidad de los modelos:

El error causado por la introducción de un valor incorrecto de F o N para laúltima clase de edad se irá reduciendo durante la recurrencia, de manera proporcional a la exponencial del sumatorio de las tasas instantáneas de mortalidad por pesca por clase de edad. (Al retroceder, suele disminuir su influencia, especialmente si las capturas acumuladas representan una parte importante de la cohorte).

ASÍ, EL APV CONVERGE HACIA EL VERDADERO VALOR DE F Y N SEGÚN NOS DESPLAZAMOS HACIA ATRÁS, ESTO ES NOS CAPACITA MÁS PARA HACER UN ANÁLISIS RETROSPECTIVO DEL PASADO DINÁMICO DEL STOCK. Un error sistemático en M provocará un error en F de signo contrario.

MORTALIDAD NATURAL. Con la misma pérdida total, atribuir más mortalidad a M deja menos para F.

El error puede hacerse muy grande: cuando $F_i$ es pequeña. El error será menor cuando se subestime M a cuando se sobrestime.

![alt text](<imagenes-4-curso/peces.17.11.png>)

Análisis de la población virtual multiespecífico: El APV multiespecífico estima de forma explícita la mortalidad por depredación. En el APV monoespecífico básico, M se fija como dato de entrada (M se considera cte). El MSVPA es una extensión del APV monoespecífico:

El APV multiespecífico combina las capturas con información sobre qué comen los depredadores y cuánto consumen.

$M = M_1 + M_2$
$M_1$: otras causas naturales. 
$M_2$: depredación.
$Z = F + M_1 + M_2$

![alt text](<imagenes-4-curso/peces.17.12.png>)

Presas que mueren por depredación:

Lo que necesitamos estimar -> Cuántos depredadores hay, cuánto come cada uno y qué presas componen su dieta.
Cómo se calcula la pérdida de cada presa -> Sumamos los peces de esa especie y edad consumidos por los distintos depredadores.
Cómo se relaciona con $M_2$ -> Muertes por depredación = $M_2$ × abundancia media de presas × duración del intervalo.

Los depredadores no incluidos explícitamente también deben contemplarse si su consumo es importante.

No toda la biomasa es alimento accesible: 

Disponibilidad -> la abundancia y el peso medio indican cuanta biomasa hay de cada presa.
Adecuación de la presa -> el tamaño, hábitat y dieta determinan que parte accesible a cada depredador.
Datos de alimentación -> los contenidos estomacales informan de que come. La ración estima cuanto consume durante el intervalo.

El modelo combina biomasa y adecuación. Incluye otro alimento para las presas que no modeliza por separado.

![alt text](<imagenes-4-curso/peces.17.13.png>)

Incluir la depredación cambia la mortalidad natural estimada y puede modificar las referencias de gestión. Este gráfico, por sí solo, no determina cuánto debe cambiar Bpa.

Diferencias mayores entre ambos modelos Arenque - en este ejemplo las estimaciones. Difieren en muchas edades. Ser una presa frecuente ayuda a entender por qué la depredación importa.

</div>