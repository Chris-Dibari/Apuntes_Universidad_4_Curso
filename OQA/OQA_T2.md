<style>
img {
    width: 45% !important; /* Forzamos el tamaño con !important */
    max-width:45% !important;
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

##  Oceanografía Química Aplicada - TEMA 2. Modelos biogeoquímicos básicos

1. COMPARTIMENTOS AMBIENTALES Y MODELOS BIOGEOQUÍMICOS SIMPLES
2. MODELOS DE UTILIZACIÓN BIOLÓGICA DE COMPUESTOS
3. TIEMPOS DE RESIDENCIA

### 1. Compartimientos ambientales y modelos biogeoquímicos simples.

Biogeoquímica marina -> Ciencia interdisciplinar que utiliza la información oceanográfica disponible para modelar el comportamiento de los elementos en el océano. No solamente basta con tener información sobre la química por tanto. El objetivo final es establecer los ciclos biogeoquímicos. Se busca invididuar los compartimientos ambientales, establecer los flujos que ocurren en los mismos e identificar las principales interconversiones.

La formulación es relativamente simple  y no se tienen en cuenta variaciones con la latitud. Debe ser cuanto más homogéneo posible, a pesar de que no cumplan perfectamente con la realidad (son aproximaciones).

Dentro de los compartimientos ambientales independientes se tienen:
- Continentes -> importancia de la biota como subcompartimiento; El continente en sí es un compartimiento relativamente inactivo, a diferencia de la biota, que es muy activo y en continuo cambio -> problema a la hora de plantear el modelo.
- Océano -> en contacto con los sedimentos, que es otro compartimiento independiente. Muy amplio y necesidad de distinta información.
- Sedimentos -> dificultad a la hora de establecer la composición puesto que se habla de testigos de sedimentos a miles de metros de profundidad. 
- Atmósfera -> compartimiento más homogéneo de todos. Para algunos gases de tipo reactivo sí hay cambio con la latitud, pero en general posee coherencia en su interior.

Se establecen flujos entre todos los compartimientos ambientales -> relaciones entre los compartimientos de intercambio.
Intentar resolver si nos vale tratar al océano como compartimiento independiente, si es suficiente.

Un elemento X tiene cierta concentración en cierto volumen de agua. La principal llegada de los elementos proviene de los ríos (el caudal). A partir de este primer esquemas se han propuesto distintos modelos:

- Modelo acumulativo -> nos dice que lo que cambia de un elemento en el océano va a ser igual a la cantidad de dicho elemento que entra a partir del caudal del río. Un elemento que tiene mucha concentración en el río se acumula mayormente en el océano y tiene mayor tiempo de residencia. Dicho modelo funciona relativamente bien para los elementos que poseen perfil conservativo (mayoritarios).

- Modelo reactivo -> tiene en cuenta la reactividad de ciertos elementos, Posee la misma basa (la vel de cambio del contenido de un elementos en el océano es igual a lo que entra de dicho elemento por el río), pero añade un termino negativo que es lo que sale del océano por la reactividad de los elementos. La reactividad constituye la desaparición de los elementos del océano. Se considera que la reactividad sigue cinética de 1º orden. En dicho caso, si se calculan los tiempor de residencia, sale que estos son inversamente proporcionales a la reactividad.

- Modelo de control termodinámico -> utilizado mayormente por los geólogos. Se basa en un equilibrio entre fases. Importancia a la hora de combinarlo con otros modelos.

<div style="page-break-after: always;"></div>

![alt text](<imagenes-4-curso/captu-2.1-oqa.png>)

En común: No permiten reproducir adecuadamente los tiempos de residencia calculados de forma experimental para elementos reactivos. Considerar el océano como único compartimiento ambiental, por lo tanto, parece no ser suficiente.



### 2. Modelos de utilización biológica de compuestos.

Si un único compartimiento ambiental no funciona para el océano, habrá que considerar más. Se empieza con considerar el segundo caso más simple: dos compartimientos.

- Aguas cálidas -> Lámina de agua superficial cálida de regiones subtropicales y ecuatoriales.
- Aguas frías -> Zonas profundas del océano y aguas superficiales en regiones polares (sin PP).

Tenemos separados los dos compartimientos mediante la termoclina principal (entre 70 y 2000m).
Se utiliza aprox el compartimiento 40ºN - 40ºS puesto que es la región en la que la T es mayor que 10Cº.

La termoclina hace que los procesos de mezcla vertical en el océano sean muy reducidos -> por lo tanto se considera como fase entre un compartimiento y el otro.

**Aproximaciones:**

Sólo se considera la entrada continental de componentes al océano:
- Otras fuentes: intercambio con la atmósfera, deposición de polvo atmosférico, actividad hidrotermal, entrada de aguas subterráneas.

“Los océanos adquieren su contenido total de compuestos a través de los ríos en periodos de tiempo comprendidos entre 104 y 106 años (tiempos de residencia típicos)”.

Los componentes reactivos son retirados de aguas superficiales por la actividad biológica e incorporados nuevamente por afloramientos.
- Mecanismo cíclico muy regular en una escala de tiempos de cientos de años.

Se considera el sistema en estado estacionario (no cambia en el tiempo).
- La concentración de un constituyente en un compartimento es constante
- Las velocidades de entrada y salida deben ser iguales en cada compartimento.

Al entrar agua en el río, para que el volumen de agua sea constante debe haber una salida (evaporación neta). PImportancia de los procesos de mezcla vertical.

![alt text](<imagenes-4-curso/captu-2.2-oqa.png>)

Volumen de mezcla -> volumen que se comparte verticalmente en el océano entre sus dos compartimientos. Para que dicho V sea cte el caudal de mezcla debe ser el mismo.

![alt text](<imagenes-4-curso/captu-2.3-oqa.png>)

La P es la cantidad de un elemento que se retira.
Ríos y afloramientos son las principales entradas de los elementos.

En la fórmula se sustituye P por los valores que contien, luego se divide en la suma de dos fracciones.

**Balance en aguas superficiales:**

![alt text](<imagenes-4-curso/captu-2.4-oqa.png>)

Importancia de la coherencia una vez obtenido un resultado, para el caso del P es coherente puesto que tiene caracter biolimitante en aguas superficiales. El 5% restante no se pierde sino que se queda en el compartimiento de las aguas superficialeas.

Hemos relacionado aguas superficiales con aguas profundas, ahora veremos la relación entre aguas profundas y sedimentos. Relación de la P con lo que queda preservado.

![alt text](<imagenes-4-curso/captu-2.5-oqa.png>)

Se despeja $f$ -> es igual a $(V_{río}*C_{río})/P$
Se sustituye P y se saca factor común entre los numeradores y denominadores, quedando la fórmula de la imagen.

![alt text](<imagenes-4-curso/captu-2.6-oqa.png>)

### 3. Tiempos de residencia.

![alt text](<imagenes-4-curso/captu-2.7-oqa.png>)

![alt text](<imagenes-4-curso/captu-2.8-oqa.png>)

f más grande nos indica que el aterial es más estable.

En cada ciclo de mezcla, un constituyente pasa la mayor parte del tiempo en las aguas profundas frías. El tiempo que permanece en las aguas superficiales se puede estimar a partir de la diferencia de volúmenes y concentraciones en los 2 compartimientos.

- Dividiendo en partes iguales la termoclina, el volumen de las aguas superficiales es 1/10 del volumen de las aguas profundas.
- Si $T_{mez}$ = 1000 años, el tiempo medio de permanencia en aguas superficiales es de 100 años.
- Eficacia del transporte como material particulado. $T_{sup} = 100/(C_{prof}/C_{sup})$

![alt text](<imagenes-4-curso/captu-2.9-oqa.png>)

![alt text](<imagenes-4-curso/captu-2.10-oqa.png>)

![alt text](<imagenes-4-curso/captu-2.11-oqa.png>)

Limitaciones del cálculo de la entradas a partir de las concentraciones medias en ríos:

1. Fiabilidad de medidas analíticas de elementos traza
2. Influencia de la actividad humana en la composición química de los ríos
3. Utilización de concentraciones de especies disueltas (necesidad de incluir detritus orgánico, formas precipitadas en estuarios y adsorbidas a partículas)
4. Diferencias de composición entre ríos, y dependencia con periodos de lluvia/sequía

El grado de incertidumbre asociado a la estimación de las velocidades de entrada a partir de la composición media de los ríos es de un 20%.
El cálculo de los tiempos de residencia basados en las velocidades de sedimentación son más precisos que los basados en la entrada a través de los ríos para los elementos afectados por la actividad antrópica.

Posibilidad de calcular tiempos de residencia a partir de velocidades de salida -> Velocidades de acumulación en el sedimento:
- P: Base de datos de concentraciones en ríos poco fiable
- Enriquecimiento actual por actividades agrícolas y vertidos urbanos

Forma parte de la materia orgánica particulada, precipita como apatito en estuarios y se adsorbe de forma intensa sobre partículas minerales.





</div>