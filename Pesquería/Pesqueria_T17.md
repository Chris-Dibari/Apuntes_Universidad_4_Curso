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





