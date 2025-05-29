# Optimizacion-de-rutas
Andrea Valentina Delgado Ruiz - 2240048
Vanessa Martínez Angarita - 2241917
Nelson Andres Urrea Calvo - 2221115

# Descripción del problema: 
Se desarrolló un programa que ayude a encontrar la ruta más optima (más corta) para ir de un lugar a otro dentro de la UIS, tomado todos sus edificios como pontos de referencia.  
Este programa le permitirá al usuario elegir el lugar donde se encuentra y al que quiere llegar, mostrándole el camino más corto según la distancia que deba recorrer. Este programa se creó pensando en facilitar la movilidad y ubicación dentro de la universidad, mayormente para estudiantes de nuevo ingreso o personas que no conozcan muy bien el campus.  

# Enfoque del proyecto:
A través de este proyecto se desarrolló un sistema de optimización de rutas que encuentra el camino más óptimo desde un lugar a otro, nosotros decidimos basar este proyecto en la UIS, tomando como referencia todos sus edificios.  

# Desarrollo de la primera versión:
Para el desarrollo de esta primera versión del proyecto, trabajaremos con listas doblemente 
enlazadas. Cada nodo representará un punto (edificio de la universidad) y se tendrán varias 
listas que contienen todos los lugares pero en orden diferente (rutas).
El objetivo de esta versión del proyecto es que el usuario pueda ingresar el lugar donde se
encuentra y su destino, y que el programa recorra las listas y escoja cual de estas rutas fijas es
el camino más rápido para llegar.
Para calcular la ruta más eficiente y rápida, se tomará en cuenta la cantidad de edificios por
los que el usuario debe pasar. La mejor ruta será aquella que requiera atravesar el menor
número de edificios para llegar al destino.

# Desarrollo de la segunda versión:
En esta segunda versión del proyecto, se implementaron las rutas mediante tres árboles utilizando la librería BigTree. Los árboles se estructuraron con cada portería de la universidad como raíz, y los lugares se conectaron a través de diferentes rutas que parten desde cada una de las porterías. Se creó una clase llamada Arbol, la cual contiene todos los nodos y sus respectivas descripciones, lo cual fue algo nuevo en esta implementación. Además, se creó un diccionario que contiene todos los nodos (lugares de la universidad). Con este diccionario, se desarrolló un método llamado asignarHijo, el cual asocia los padres con sus respectivos hijos. Luego, se construyó un árbol para cada portería y sus respectivos hijos.

Una vez creada la estructura de los árboles, se le muestra al usuario un menú que contiene 4 opciones: 

La opción "0. Mostrar arboles" permite al usuario mirar la estructura de cada uno de los tres árboles si así lo desea.

La primera “1. Añadir lugar actual y destino” una vez escogida muestra la lista de lugares que tiene la Universidad numerados y se solicita al usuario la ruta que desea calcular, el punto de origen y el destino ingresando un número del 1-35 el cual está asociado a cada uno de los nodos. Se solicita el número en vez de las cadenas de texto porque estás ante el mínimo error de ortografía, tales como mayúsculas o tildes, pueden llevar a errores; posteriormente se usa el método buscarNodoPorNumero para encontrar el nodo asociado a cada número. 

La segunda opción es “2. Ruta más corta” que muestra la ruta que se calculó mediante el método encontrarRutaMasCorta, que encuentra las rutas en cada uno de los árboles, determina su longitud y las compara, mostrando la de menor longitud.

La tercera opción es “3. Todas las rutas”, esta opción nos permite ver las 3 rutas posibles que encontró el programa.
Y la cuarta opción es "4. Salir" que simplemente finaliza la ejecución del programa.

Las opciones 2 y 3 piden que primero haya sido diligenciada la opción 1, después de ejecutados cada uno de los métodos de la opción escogida se le pregunta al usuario si desea volver al menú principal o salir del programa. 

Esta versión del proyecto permite calcular las rutas de manera más eficiente, ya que facilita la comparación entre varias opciones. La implementación es menos tediosa que cuando utilizamos listas enlazadas, y la dificultad del código es menor en comparación con la versión anterior. El uso de árboles mejora la organización y la optimización de las rutas, permitiendo obtener la ruta más adecuada de forma más rápida y sencilla.
