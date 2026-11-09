<style>
img {
    width: 50% !important; /* Forzamos el tamaño con !important */
    max-width:50% !important;
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

##  Oceanografía Química Aplicada - TEMA 6. Acoplamiento biogeoquímico en el Atlántico Norte.

![alt text](<imagenes-4-curso/captu-oqa-6.1.png>)

3300 millas con 15 estaciones.

### Ocean Data View

Variable experimentales de partida: CTD 
- t, s, fluorescencia y P
- Nutrientes;
- $pH_T$ espectofotométrico;
- Alcalinidad total;
- Oxígeno disuelto.

1. Identificación de masas de agua -> diagramas T-S y gráfica de perfiles verticales.
2. 
3. Identificación de clorofila.

**Parte I:** Se utiliza un perfil vertical:

![alt text](<imagenes-4-curso/captu-oqa-6.2.png>)

- Calcule la AOU utilizando la ecuación de Weiss:

![alt text](<imagenes-4-curso/captu-oqa-6.3.png>)

- Represente y explique las variaciones verticales de la temperatura, salinidad, concentración deoxígeno, AOU, flourescencia y turbidez.
- Calcule la temperatura potencial y realice un diagrama T-S en esta estación. Identifique y marque sobre el diagrama las 4 principales masas de agua que observe.

---

Vamos a abrir el fichero "CTD 8 ODV.xls" con ODV.

Calculamos la T (K), luego calculamos el LN mediante la ecuación de Weiss y seguidamente la $C^*$ aplicando exponencial.
La AOU se calcula como la solubilidad ($C^*$) - oxígeno.
Copiamos la columna de AOU y pegamos como valaores, de esta forma podemos eliminar las columnas de T, $C^*$ puesto que solo nos sirve la. AOU.
Se procede exportando el archivo en txt para importarlo en ODV.



