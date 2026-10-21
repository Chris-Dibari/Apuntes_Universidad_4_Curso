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
3. Mediante estructuras -> aproximación anatómicas.

