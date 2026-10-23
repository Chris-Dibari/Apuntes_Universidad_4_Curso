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

##  Pesquerías. TEMA 13. Modelos de Crecimiento.

El crecimiento es la acumulación de tejido somático que depende de la energía consumida, que se considera el incremento de una unidad vital.
Se mida a través de los incrementos de tallas o de peso (forma más fácil). Una parte del alimento (energía) se invierte en procesos metabólicos, otra se invierte en crecimiento somático y otra que se invierte en el crecimiento reproductor (relacionado con perpetuar la especie y crecimiento poblacional).
A diferencia de los mamiferos, los peces tienen crecimiento continuo (indeterminado) a pesar de que conforme se vayan haciendo más mayore, dicho crecimiento se ralentice.

$I=M+G+R+E$

En el crecimiento se tienen variaciones:

- entre distintas especies
- dentro de la misma especie (intraespecífica) -> se tienen interpoblacionales (poblaciones en diferentes sitios, con factores abióticos que afectan dicho crecimiento) e intrapoblacionales (se deben en parte a los propios factores endógenos -genéticos-). También hay factores exógenos relacionados. Esto varía claramente de una zona a otra (fotoperíodo, T, s, saturación de oxígeno...).

**Interacciones bióticas:** puede darse competencia por el mismo recurso. También puede darse predación (cuando el depredador depreda mucho se reduce la cantidad de presa y un aumento de las mismas en las tasas de crecimiento -las que sobreviven tienen más recurso-). Otra es el parasitismo (desviación mayor de la energía al metabolismo). Otros tipos son ejempplares de mayor tamaño que pueden inhibir el acceso a la comida a los más pequeños.

**Medida del crecimiento:** Una de las formas más faciles son medidas de peso y tallas (= longitud). Podemos sacar ambas y hacer una relación longitud-peso. Dicha relación es de tipo potencial (NO exponencial). $P=aL^b$. Implica que normalmente el peso va a crecer en términos de volumen (el animal crece en 3D).
La b = 3 nos indica que el crecimiento es isométrico (crece proporcionalmente en longitud y peso). b > 3 implica que el pez está creciendo más en peso que en longitud (crecimiento alométrico positivo). Finalmente, b < 3 implica crecimiento alométrico negativo (no crece proporcionado, más en longitud que en peso).

**Cálculo de la relación:**  Mediante los datos experimentales (medidas de longitud y peso) -> relación de tipo potencial = necesitamos linealizarla (tomar log tanto de longitud como de peso). Se obtiene una recta con pendiente negativa $log(P)=log(a)+b(logL)$ y a partir de aqui puedo sacar los parámetros a y b, obteniendo los valores teóricos de peso y longitud. Al tener los parámetros, ya puedo sustituir en la ecuación.

**La condición: el grado de bienestar** -> uno de los indices que está relacionado con la propia reserva que tiene el pez. Evaluación útil acerca del estado de bienestar.

**Índice de Fulton:** se calcula de forma individual (para cada individuo), se hace una media de la población o grupo de población y se asume crecimiento isométrico. No permite comparar entre especies, solo intraespecie. Permite analizar los valores estacionales.

$$K=(P/L^3) * 10^5$$

El índice viscerosomático -> Es una variación que se utiliza cuando se quitan todos los órganos del pez (peso eviscerado). $$IN=(P_{evis}/L^3)*10^2$$
En acuicultura también se utiliza mucho el índice epatosomático.
La condición se calculas partiendo de los datos experimentales.

**Crecimiento anual:** cuanto crecen los peces a lo largo de los años. Se representa X = edad mientras que Y = longitud. El pez va creciendo a lo largo de los años hasta alcanzar un crecimiento asintótico. Algunas especies tienen crecimiento estacional (variación del crecimiento), además hay otro crecimiento a saltos (tipo incrementos) que es más típico de crustáceos (se corresponde a las mudas).

La determinación de la edad en los peces es asignarle un tiempo de vida al pez en función de la talla. Este tiempo se asigna desde el momento en que nació el pez. La longevidad de las especies varía mucho. Algunas especies pueden crecer muy poco independientemente del tiempo que pase (y otras como el atún que pueden crecer hasta los 13 años). Los peces de mayor tamaño suelen ser más longevo por lo general. En cautividad pueden alcanzar mayor longevidad puesto que la parte de la energía reservada a la reproducción no se gasta puesto que no se reproducen. 

Para estimar la edad se tiene en cuenta también la abundancia por clases de edad (información sobre la mortalidad).

**Determinación de la edad:**

1. Aproximación empírica basada en observación directa -> se captura el pez y se marca, volviendose a liberar y recuperandolo años despues para ver como ha crecido. Esto aporta info adicional sobre los movimientos del pez (desplazamientos) => método de captura-recaptura.
2. Aproximación estadística (indirecto) -> obtener distribuciones de frecuencias de longitudes => histograma. Este último posee modas que nos pueden indicar las clases de edad (más complicado). Cuando somos capaces de visualizar la distribución normal, tenemos las clases de edad.

Una aproximación estadística basada en distribuciones de frecuencias de longitudes.

![alt text](<imagenes-4-curso/captu-13.1-peces.png>)

La pregunta es ¿es posible separar las distintas cohortes que constituyen una muestra sin utilizar técnicas de determinación de edades por medio de estructuras duras?

- Dependiendo de las características reproductivas y del crecimiento de cada especie, muchos peces se reproducen una vez al año y tienen un periodo de reproducción muy corto, lo cual hace que las cohortes sean de tallas muy similares y bien marcadas.
- En ciertas condiciones si es posible, excepto en aquellas partes en que las frecuencias de tallas de las diferentes cohortes se superponen demasiado.
- La sobreposición en la composición de tallas de las cohortes de los peces mas grandes (que equivale a los peces mas viejos) limita claramente el análisis.

Este es un buen método para peces menores de 4 o 5 años. Los componentes modales son difíciles de definir en especies longevas o en aquellas con desove y reclutamiento continuo o prolongado en el año.

No hay escala de tiempo real, las edades son relativas.
- MÉTODOS DE DETERMINACIÓN DE LA EDAD
- MÉTODOS ESTADÍSTICOS, POBLACIONALES
- METODOS DE LAPIZ Y PAPEL
• Método de PETERSEN
• Método de HARDING (1949)
• Método de CASSIE
• Método de BHATTACHARYA
• Método de PAULY Y CADDY (1985)
• Método del Análisis de progresión de clases modales
• Método Integrado
- METODOS COMPUTACIONALES
• NORMSEP (Normal Distribution Separation)
• ENORMSEP
• ELEFAN I (Electronic Length Frequency Analysis)

![alt text](<imagenes-4-curso/captu-13.2-peces.png>)

**Método del papel semilogarítmico:**

Consiste en transformar las frecuencias absolutas en frecuencias relativas acumuladas.
- Permite separar las distintas distribuciones normales dentro de una distribución multimodal, que están separadas gráficamente por puntos de inflexión, puntos donde cambia la tendencia de la pendiente.
- Cada distribución normal se separa en rectas que al representar permiten obtener el 50% (valor de abcisas al que le corresponde una valor de X, de talla, que se corresponde con la talla media de esa edad).
- De igual manera se calcula la desviación tipica, con aquellos puntos del eje de abcisas correspondientes a los valores de ordenada de 15,87 y 84,13.

**PROGRESIÓN MODAL** -> Análisis de la variación, del desplazamiento de la moda de la distribución de tallas de las capturas a lo largo del tiempo.

3. Mediante estructuras -> aproximación anatómicas. Una aproximación anatómica basada en datos de peces individuales a partir de sus estructuras duras como ser escamas, otolitos, vértebras, huesos operculares, radios duros de las aletas, espinas. Se basan en que las tallas de los individuos de una determinada clase de edad responde a una distribución normal y por lo tanto, la media mediana y moda coinciden, por lo que un muestreo suficientemente representativo seguirá una distribución multimodal, en la que cada moda se corresponde con una clase de edad.

**Otros métodos de determinación de la edad:**

ANÁLISIS DE MARCAS ANUALES EN ESTRUCTURAS DURAS DE CRECIMIENTO MARGINAL:
￼
- En el año 1759 el reverendo Hans Hederström analizó las vértebras de un pez teleósteo.
- El primer estudio serio fue publicado en escamas de carpas hecho por Hoffbauer en 1898.

Las escamas son estructuras exoesqueléticas, láminas delgadas, que se va incrementando en tamaño por oposición de círculos concéntricos de osificación. Son muy resistentes y flexibles y están dispuestas oblicuamente en el sentido dorsoventral, siguiendo la disposición de la musculatura lateral.

**Otolitos:** Mas densos que el resto del cuerpo, sensibles a:
Cambios de posición y a la fuerza de gravedad --> EQUILIBRIO
Las ondas sonoras -> RECEPCIÓN DEL SONIDO
* En CONDRICTIOS: Pequeños cristales de carbonato cálcico:

Matriz gelatinosa
* En OSTEICTIOS: Estructura ósea con una matriz proteica
- MEMBRANA OTOLITICA, gelatinosa
- EPITELIO SENSORIAL O MACULA.

- El otolito crece a partir de un núcleo central de materia orgánica (primordium) que proporciona un soporte que favorece la nucleación de los cristales de aragonito.
- En un otolito se distinguen bandas translúcidas, o unidades continuas, alternadas con bandas opacas o discontinuas. Un año de crecimiento está formado por una banda opaca (verano) y otra traslúcida (invierno).

El crecimiento del otolito es cíclico y está sujeto a ritmos circadianos relacionados con el metabolismo, y sincronizados con factores ambientales externos:

• En épocas de crecimiento favorable, la zona hialina es ancha y bien diferenciada, y los microscristales delgados.
• En periodos de crecimiento lento, el microincremento es más fino y los microcristales más compactos.

- El 1ºanillo bien marcado se deposita a un determinado tiempo comprendido entre la eclosión del huevo y el comienzo de la alimentación activa, dependiendo de la especie. Acompañando al Calcio, existen trazas de metales (Sr, Ba, Mg, Cd, Co, Cu, Zn, Na, K, etc...) y otros no metálicos (Si, P, S, B, etc...).
- La incorporación está relacionada con los cambios fisiológicos en el desarrollo y con el medio ambiente (cambios de Tª, alimentación, niveles de nutrientes y contaminantes disueltos en agua de mar, etc.). Por ejemplo la relación Sr/Ca parece estar inversamente relacionada con la Tª.

En base a esta hipótesis, las poblaciones que se encuentran en hábitats distintos deben caracterizarse por la diferente composición elemental de los otolitos. Este criterio ha sido utilizado para la discriminación entre distintos "stocks" y trazar la historia medioambiental del pez.

![alt text](<imagenes-4-curso/captu-13.3-peces.png>)

**Utilización del retrocalculo:**

1. Calcular longitudes a edades en que raramente son observados
2. Comparar el crecimiento entre sexos
3. Comparar el crecimiento de distintas cohortes
4. Comparar el crecimiento de distintas poblaciones.

![alt text](<imagenes-4-curso/captu-13.4-peces.png>)

**Modelo de crecimiento anual:**

![alt text](<imagenes-4-curso/captu-13.5-peces.png>)

![alt text](<imagenes-4-curso/captu-13.6-peces.png>)

![alt text](<imagenes-4-curso/captu-13.7-peces.png>)

MODELO DE VON BERTALANFFY: Los valores de k en la naturaleza varían.

![alt text](<imagenes-4-curso/captu-13.8-peces.png>)

**Velocidad de crecimiento:**

- CRECIMIENTO LENTO: BAJOS VALORES DE k INDEPENDIENTEMENTE DE LA TALLA MÁXIMA QUE PUEDA ALCANZAR
- CRECIMIENTO RÁPIDO: ALTOS VALORES DE k INDEPENDIENTEMENTE DE LA TALLA MÁXIMA QUE PUEDA ALCANZAR.

Merluccius merluccius, tiene un crecimiento lento (k pequeña) pero crece mucho de un año al siguiente. El crecimiento lento supone que tarda en alcanzar su talla máxima pero no supone valor alguno en los incrementos de la magnitud medida de una año a otro.

CUANTO MAYOR SEA SU VALOR LA POBLACIÓN CRECE MÁS RÁPIDO, ALCANZA SU TALLA MÁXIMA ANTES. PERMITE COMPARAR STOCK CON IGUAL $L_{inf}$

![alt text](<imagenes-4-curso/captu-13.9-peces.png>)

![alt text](<imagenes-4-curso/captu-13.10-peces.png>)

![alt text](<imagenes-4-curso/captu-13.11-peces.png>)

Al efectuar este análisis por separado con cada familia de peces se reduce la varianza, puesto que la mayoría de ellas son, ya sea predominantemente pelágicas o predominantemente demersales. Para la familia Scombridae (caballa y atún).

Las diferencias en el crecimiento entre especies de longevidad diferente pueden ser comparadas mediante los parámetros k, Peso (P), L

Gallucci & Quinn (1979):
RANGO DE CRECIMIENTO: ω es el rango de crecimiento próximo a $t_0$, es un parámetro estable, más próximo a la distribución normal que j y $L_{inf}$ por separado.

![alt text](<imagenes-4-curso/captu-13.12-peces.png>)

Existen otras especies animales cuyo crecimiento no presenta un modelo asintótico, sobretodo en el caso de los cefalópodos. Entre las expresiones del crecimiento más usual es en estos casos podemos encontrar: la lineal, la logaritmica, la exponencial, la doble exponencial.

![alt text](<imagenes-4-curso/captu-13.13-peces.png>)

![alt text](<imagenes-4-curso/captu-13.14-peces.png>)

C = la amplitud de la oscilación, generalmente entre 0 y 1.
- Cuando C= 0 no hay variación estacional y esta expresión se transforma en la expresión general de VB.
- Cuando C= 1 la tasa de crecimiento en invierno es 0.

![alt text](<imagenes-4-curso/captu-13.15-peces.png>)

</div>