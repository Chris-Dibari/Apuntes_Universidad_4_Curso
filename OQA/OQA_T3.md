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

##  Oceanografía Química Aplicada - TEMA 3. Ciclo del carbono inorgánico en el medio marino. 

Tendencia global del océano en comportarse como sumidero de carbono.
Gran importancia en el ciclo del carbono -> se incluye el pH.

**Índice:**

1. Introducción. Ciclos biogeoquímicos y sistemas ácido-base
2. Escalas de pH y constantes de disociación
3. Mecanismos de regulación del pH en los océanos
4. Concepto de alcalinidad y su determinación experimental
5. Intercambio de CO2 a través de la interfase atmósfera-océano
6. Reacciones en fase homogénea
7. Precipitación de CaCO3
8. Distribución de especies en agua de mar
9. Ciclo del carbono inorgánico.

### 1. Introducción. Ciclos biogeoquímicos y sistemas ácido-base

Asumimos que el agua de mar está en equilibrio químico. Este ultimo es algo complejo: existe gran **cantidad** y **variedad** de sustancias disueltas en sw. El agua de mar tiene fuerza ionica de 0,7 (disolución concentrada y compleja).
Por otro lado, todas las especies disueltas participan en procesos en el sw (reacciones ácido-base, redox, biosintesis...). Además, el sw se considera como sistema abierto (no aislado) que va a estar interaccionando con otros compartimientos medioambientales (sedimento, atmósfera, margenes continentales). 
Todos esos procesos en los que participan dichas sustancias van a variar dependiendo de las variables físico-químicas (T, pH, pE, presión salinidad).

Se aproxima -> sistema en equilibrio químico.

Esquema de las distintas entradas y procesos que ocurren en el agua de mar. 90% de las entradas a partir de los ríos, a su vez, el sw va a estar intercambiando sustancias con la atmósfera (intercambio de gases...). En el sw se tienen múltiples reacciones dependientes de las variables físico-químicas (adsorción, absorción, asociaciones iónicas...). Contacto directo con el sedimento -> intercambio con el agua intersticial (sedimentación del material particulado).

![alt text](<imagenes-4-curso/captu-3.1-oqa.png>)

Organismos vivos -> afectación de las sustancias disueltas ($O_2$, $CO_2$). Importancia de la luz solar -> condiciona la cantidad y la distribución de los organismos vivos en el medio marino.

Se estudia desde perspectiva termodinámico las reacciones y procesos individualmente, para establecer modelos que tengan en cuentas todas las reacciones del medio marino.
Hay que tener en cuenta toda la información disponible para plantear el estudio.

$A^- + H^+ -> HA$ con una cte de disociación aparente que modula el equilibrio. En todas las reacciones del medio marino, puesto que son prevalentemente ácido-base, participan los H^+. Importancia del pH como parámetro oceanográfico.
El pH ya no se usa como trazador puesto que está afectado por la T.

<div style="page-break-after: always;"></div>

![alt text](<imagenes-4-curso/captu-3.2-oqa.png>)

Se presentan bajo condiciones específicas las principales especies proteolíticas (especies cargadas con un protón, H). Para tener la K es suficiente con $10^{pK}$.
Arriba se tienen las especies principales del sw. El ácido sulfurico tiene importancia en condiciones anóxicas (sedimentos, ciertas zonas costeras, mar Negro...), puesto que la mayoría de las sw se encuentran en condiciones óxicas.

Los protones forman relaciones estables con los compuestos en el medio marino.

Resumen: para establecer un ciclo biogeoquímico se parte de un sistema en equilibrio, estudiando las reacciones por separado de forma termodinámica, necesitandose toda la imformación disponible. Importancia del pH como parámetro.

### 2. Escalas de pH y connstantes de disociación

Aunque se considere el $H^+$ como elemento libre, realmente reacciona en el sw como $HO_3^+ -> HO_q^+$

Dickson (1987) "el estudio de las reacciones de transferencia de protones en el agua de mar constituye uno de los temas más confusos de la química marina".

Tenemos 4 escalas de pH y cada una posee su propia nomenclatura, porque cada una de ellas tiene una constante de disociación diferente. La confusión puede provocar un error importante si se habla de química marina (~0,003).

![alt text](<imagenes-4-curso/captu-3.3-oqa.png>)

<div style="page-break-after: always;"></div>

**Principal diferencia**: disolución de calibración de los pHímetros que se utiliza.

- NBS -> Es la más clasica. Se utiliza un agua destilada (fuerza iónica muy baja). La concentración se expresa en términos actividades, el pH como pH(NBS) y la constante como K'. 
- Concentración total del ión hidrógeno (mol/kg-SW). La más antigua. Fuerza iónica similar al sw. Esta y las siguientes son específicas del sw.
- Concentración libre del ion hidrógeno (mol/kg-agua).
- SWS (mol/kg-SW).

Tradicionalmente, el pH se midió con electrodos de vidrio, con una disolución muy concentrada y un electrodo de referencia. Consiste en una celda galvanica que mide el *potencial de la muestra*. Para pasar de potencial a pH se utiliza la ecuación de Nernst.

![alt text](<imagenes-4-curso/captu-3.4-oqa.png>)

El potencial que tiene la muestra va a ser igual al potencial aparente (escala NBS) + RT/F * lna_{H^+}+E_{J(x)} Este último es el potencial de únion líquida. Va a surgir en la zona de contacto entre las dos disoluciones y se debe a la difusión de especies de electrolitos (iones) y su magnitud va a depender de la concentración de la muestra y del intercambio de iones.

El potencial estandar es especifico del electrodo => puedo igualar:

*{Desarrollo fórulas 21/10}*

**ESCALA NBS (National Bureau of Standard):**

- Soluciones de calibración de baja fuerza iónica (utilizada para agua dulce).
- Es la escala más utilizada internacionalmente.
- Las variaciones de los potenciales de unión líquida entre el agua de mar y las soluciones de calibración:

El problema que presenta es que calibras con fuerza ionica muy baja, pero luego se miden muestras con fuerza ionica muy altas -> esto conlleva a diferencias elevadas.

![alt text](<imagenes-4-curso/captu-3.5-oqa.png>)

Otro inconveniente (en sw) es que son poco reproducible (dependiendo a la diferencia).

La expresión es utilizada para pasar de la escala NBS a la escala total (mucha utilidad a la hora de poder comparar datos con otras localizaciones).

Cálculo del coeficiente: coge una solución de calibración de la escala total (disoluciones tamponadas) de la cual conoce el pH. Se mide en el pHimetro de escala NBS y asi se tiene un criterio de comparación. Esto sirve para poder encontrar la forma de comparar datos.
La escala no es ideal para sw, pero siempre que la utilice se puede pasar a escala total, y también a escala libre.

La escala libre son moles por kg de agua (se expresa en molal por kg de agua) Es la única escala que se expresa en molal. 

![alt text](<imagenes-4-curso/captu-3.6-oqa.png>)

Son escalas específicas para sw. La disolución de calibración tendrá una disolución artificial y una disolución tampón (se utiliza una mezcla equimolecular -mismas concentraciones- de dos sustancias tampones que son TRIS y TRIS-HCl).

Ventajas: la diferencia de los potenciales de unión líquida es practicamente cero puesto que ambos tienen la misma fuerza iónica (me evito el error en la medida del pH).

Diferencia entre las tres escalas: como se prepara el sw artificial para la disolución de calibración.

En el caso de la escala libre, se prepara solo con cloruro sódico y se pesa la cantidad suficiente para que la fuerza iónica se de 0,7 Molal (M).

La total es la que comete el menor error. Se prepara con cloruro sodico y sulfato sodico, para una fuerza ionica final de 0,7 M.

La seawater es la más completa, se prepara con los dos compuestos anteriores y además el NaF. La constante de disociación del ácido fluorhidrico no se conoce con exactitud => cometemos más error utilizando esta escala comparado con la total.

Se definen como sigue:

![alt text](<imagenes-4-curso/captu-3.7-oqa.png>)

**Relación entre las escalas total y libre:**

![alt text](<imagenes-4-curso/captu-3.8-oqa.png>)

**pH espectrofotométrico:**

En la obtención de pH por técnicas espectofotométricas los valores del pH son determinados mediante la adición al agua de mar de un indicador coloreado. Generalmente se suelen emplear indicadores como el azul de timol, m-cresol púrpura o el rojo de cresol. La precisión del valor del pH obtenida con esta técnica llega a ser de ± 0.0004 (Clayton y Byrne, 1993), frente a valores típicos de ± 0.003 obtenidos con técnicas potenciométricas (Furhmann y Zirino, 1988).

### 3. Mecanismos de regulación del pH en los océanos

El pH del agua de mar varía entre 7,95-8,35 (muy pequeña) y se considera un pH promedio de 8,15. Por ello se dice que el pH está tamponado. El hecho de que practicamente no varíe a pesar de la gran cantidad de reacciones ácido-base que se tienen se debe a 2 procesos a distintas escala de tiempo:

1. Sistema de pH fluctuante: se produce en la **superficie del océano** y en una **escala de tiempo muy corta**. Se debe a la capacidad de interconversión de las especies del carbónico (cambian de una a otra). En el sw el C_inorg disuelto es de aprox. 2,3 mM y es = [$HCO_3^-$] + [$CO_3^{2-}$] + [$CO_2$]. En el sw la cantidad de tampón que se debería añadir es la cantidad de ácido-base que se añadiría para que el pH varíe de una unidad. También se producen procesos en la interfase océano-atm (intercambio de $CO_2$) y los procesos de disolución de $CACO_3$. Es un mecanismo que permite que no varíe el pH a nivel **local** (ej, entrada de $CO_2$ de la atmósfera, entradas por los ríos...).

2. Sistema de pH estático: se produce en las aguas profundas en contacto directo con el sedimento, tiene escalas largas (hasta siglos). Se debe al interacción de las arcillas con los iones $H^+$ y bicarbonato. Se produce la regulación por dos formas: en las proximidades del sedimento gracias al Na procedente de las arcillas con los iones en disolución (proceso limitado a la superficie del sedimento).
El otro mecanismo es mucho más intenso (mayor capacidad de regulación del pH) y se debe al cambio de las arcillas de un tipo de mineral a otro -> transformación de las arcillas. Ej. típicos: transformación de a mica en caolinita (va a hacer que el pH aumente puesto que retira protones), formación de la sepiolita a partir de la sílice amorfa de los esqueletos de las diatomeas (libera protones = acidificación del medio).

![alt text](<imagenes-4-curso/captu-3.9-oqa.png>)

### 4. Concepto de alcalinidad y su determinación experimental


La alcalinidad total es una magnitud experimental, que se define como la cantidad de ácido fuerte **necesaria para neutralizar** 1 kg de agua de mar hasta un punto final correspondiente a la formación de $CO_2$ a partir del ion bicarbonato. La valoración ácida del agua de mar no es un procedimiento específico para el carbono inorgánico y participan todos los equilibrios ácido-base presentes. La alcalinidad es muy fácil de medir. La alcalinidad total se define como:

$A_T$ = [Bases débiles] - [Ácidos débiles protonados] + [$OH^-$] - [$H^+$]

Establecer unas pautas que sirva de condiciones generales: se consideran en las reacciones ácido-base donadores de protones todas las especies cuyas constantes de disociación sean mayores que $K'>10^{-4.5}$. Los aceptores de protones tendrán $K'< 10^{-4.5}$.

![alt text](<imagenes-4-curso/captu-3.10-oqa.png>)

**Definición exacta de la alcalinidad total:**

$A_T$ = [$HCO_3^-$]+ 2[$CO_3^{2-}$]+[$B(OH)_4^-$]+[$HPO_4^{2-}$]+ 2[$PO_4{3-}$] + [$SiO(OH)_3^-$] +[$NH_3$]+[$HS^-$] + 2[$S_2^-$] + [$OH^-$] - [$HSO_4^-$] - [$HF$]-[$H_3PO_4$]-[$H^+$]

Simplificación para el sistema oceánico: la sensibilidad del medio analítico es de más/menos 1 micromolar (precisión del método).
Las concetraciones analíticas en sw de fosfato, silicato y amonio son < 10-20 micromolar. Además, no se encuentra sulfuro puesto que la mayoría se encuentra en condiciones óxicas. Por tanto la expresión queda simplificada:

$A_T=[HCO_3^-]+2[CO_3^{2-}]+[B(OH)_4^-]$

Alcalinidad orgánica = Contribución a la alcalinidad que tienen las especies orgánica debida a esas especies que se forman en el momento en que añado ácido para la valoración (se resta a la alcalinidad medida para obtener la alcalinidad total).

**Medidas de alcalinidad:** Se coge cierto volumen de sw (cuanto más mejor) y se realiza una valoración potenciométrica (medir el potencial cada vez que se añada ácido a la muestra), concretamente se utiliza la de punto final (se aáde ácido hasta llegar a un punto de potencial final que es cuando se deja de añadir ácido).
Curva con dos puntos de inflexión: el primero indica la cantidad de ácido que se ha tenido que añadir para que todo el carbonato presente se transforme en bicarbonato. El 2º punto de inflexión es el que interesa para la alcalinidad total -> cantidad de ácido que he tenido que añadir a la muestra para que todo el bicarbonato y carbonato se transformen en $CO_2$, a partir de ese punto todo el ácido añadido está en exceso.

![alt text](<imagenes-4-curso/captu-3.11-oqa.png>)

Se tiene que $A_T*V_0=C_A*V_e$

Yo conozco la cantidad de muestra y el volumen inicial, me falta conseguir el $V_e$

- Método diferencial: representar el delta de potencial / delta del volumen frente al volumen de ácido que se ha añadido. $ΔE/ΔV$ frente a $V_{HCl}$
- Método de Gran: algoritmo matematico que me sirve para obtener el volumen de equivalencia para cualquier valoración potenciométrica. Se define una función arbitraria (sin unidades) llamada $F'$ que consiste en linearizar la parte ácida de la curva (la que la cantidad de ácido está en exceso). Al representarla frente al volumen de de ácido que he ido añadiendo, tiene un comportamiento lineal y cuando su valor será igual al volumen de equivalencia ($F' = 0$).

**Obtención de la función de Gran:** se aplican 3 pasos.

1. Reconocimiento de las reacciones principales.

![alt text](<imagenes-4-curso/captu-3.12-oqa.png>)

En el circulo azul es la zona ácida. El ácido en exceso produce un aumento de concentración de las 3 especies indicadas. 

2. Balance de masa referido a ese volumen de equivalencia. 
El número de moles que tengo de las tres especies anteriores es igual al exceso de número de moles que tengo de iones $H^+$ (del ácido). La concentración total es la suma de las concentraciones que tenemos de las tres especies. Se obtiene la función de Gran.

![alt text](<imagenes-4-curso/captu-3.13-oqa.png>)

3. Aplicación de la ecuación de Nernst. Para pasar la concentración de protones a potencial.

![alt text](<imagenes-4-curso/captu-3.14-oqa.png>)

Grado de disociación puesto que se trabaja con la constante de disociación. También se puede trabajar con la constante de asociación.

![alt text](<imagenes-4-curso/captu-3.15-oqa.png>)

$F'_G=a+b*v$
$F'_G=0 -> v=v_e=-a/b$

**Alcalinidad de carbonato:** 

![alt text](<imagenes-4-curso/captu-3.16-oqa.png>)

$B_T$ aprox 0,43 mM -> La concentración de borato supone un 1% de la alcalinidad total.

### 5. Intercambio de $CO_2$ a través de la interfase atmósfera-océano

Normalmente se supone el sistema en equilibrio, el $CO_2$ en el sw y en la atmósfera siguen un equilibrio dinámico: $[CO_2]_{g} <-> [CO_2]_{ac}$
En la naturaleza se tienen procesos que pueden romper dicho equilibrio, esto provoca que se produzca un flujo de gas desde mayores concentraciones hasta menores.
Ejemplos de fenómenos son: intensa actividad fotosintetica, un upwelling de masas de aguas fría ricas en $CO_2$.

![alt text](<imagenes-4-curso/captu-3.17-oqa.png>)

El coeficiente de solubilidad varía con salinidad, profundidad y presión, sin embargo, al considerar la presión cte, dicha variación no se considerará. La expresión de Weiss permite calcular el coeficiente de solubilidad. A medida que aumenta T y S, disminuye $K_0$ (relación inversa con estas dos variables).

### 6. Reacciones en fase homogénea

Se verán las diferentes reacciones ácido-base y disolución en las que participan las especie del carbono. El DIC se compone de bicarbonato, carbonato y $CO_2$ (NO el ácido carbónico, ahora se verá el porqué).

![alt text](<imagenes-4-curso/captu-3.18-oqa.png>)

