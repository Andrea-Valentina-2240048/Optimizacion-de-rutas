# Optimizacion-de-rutas
Andrea Valentina Delgado Ruiz - 2240048
Vanessa Martínez Angarita - 2241917
Nelson Andres Urrea Calvo - 2221115

# Descripción del problema: 
Se desarrolló un programa que ayude a encontrar la ruta más optima (más corta) para ir de un lugar a otro dentro de la UIS, tomado todos sus edificios como pontos de referencia.  
Este programa le permitirá al usuario elegir el lugar donde se encuentra y al que quiere llegar, mostrándole el camino más corto según la distancia que deba recorrer. Este programa se creó pensando en facilitar la movilidad y ubicación dentro de la universidad, mayormente para estudiantes de nuevo ingreso o personas que no conozcan muy bien el campus.  

# Enfoque del proyecto:
A través de este proyecto se desarrolló un sistema de optimización de rutas que encuentra el camino más óptimo desde un lugar a otro, nosotros decidimos basar este proyecto en la UIS, tomando como referencia todos sus edificios.  

# Primera implementación: 
Para el desarrollo de la primera versión del proyecto, se trabajó con listas doblemente enlazadas y se tomaron como referencia solo 12 edificios de la universidad. Cada nodo representaba un punto (es decir, un edificio de la universidad), y se manejaban varias listas que contenían todos los lugares, pero en un orden diferente, representando así las distintas rutas. 
El objetivo de esta versión del proyecto era que el usuario pudiera ingresar el lugar donde se encuentra y su destino, y que el programa recorriera cada una de las listas para seleccionar cuál de esas rutas fijas era el camino más rápido para llegar. 
Para calcular la ruta más eficiente y rápida, se tuvo en cuenta la cantidad de edificios que el usuario debía atravesar. La mejor ruta era aquella que requiriera pasar por el menor número de edificios para llegar al destino.
En cuanto a la eficiencia, las operaciones pequeñas e individuales como agregar elementos tienen una eficiencia de (O(1)). Los recorridos y búsquedas en la lista son lineales (O(n). La operación con menor eficiencia es encontrarRutaMasCorta, ya que tiene una complejidad (O(n^2) debido a que recorrer todas las rutas tiene una complejidad (O(n)) y en cada una de ellas realizamos operaciones de complejidad (O(n)) como obtener las posiciones de inicio y fin e imprimirRutaParcial. 
La complejidad del código era de (O(n^2)), lo cual podría ser un problema si agregaramos muchas rutas y elementos, esto es debido a que estamos usando únicamente listas enlazadas, las cuales no son tan eficientes para enfrentar este tipo de problemas. 

# Segunda implementación: 
En esta segunda versión del proyecto, se implementaron las rutas mediante tres árboles utilizando la librería BigTree. Los árboles se estructuraron con cada portería de la universidad como raíz, y los lugares se conectaron a través de diferentes rutas que parten desde cada una de las porterías. Se creó una clase llamada Arbol, la cual contiene todos los nodos y sus respectivas descripciones, lo cual fue algo nuevo en esta implementación. Además, se creó un diccionario que contiene todos los nodos (lugares de la universidad). Con este diccionario, se desarrolló un método llamado asignarHijo, el cual asocia los padres con sus respectivos hijos. Luego, se construyó un árbol para cada portería y sus respectivos hijos. 
Una vez creada la estructura de los árboles, se le mostraba al usuario un menú que contenía cuatro opciones: 
La opción "0. Mostrar arboles" permitía al usuario mirar la estructura de cada uno de los tres árboles si así lo deseaba. 
La primera “1. Añadir lugar actual y destino” una vez escogida le mostraba la lista de lugares que tiene la Universidad numerados y se solicitaba al usuario la ruta que deseaba calcular, el punto de origen y el destino ingresando un número del 1-35 el cual estaba asociado a cada uno de los nodos. Se solicitaba el número en vez de las cadenas de texto porque estás ante el mínimo error de ortografía, tales como mayúsculas o tildes, pueden llevar a errores; posteriormente se usaba el método buscarNodoPorNumero para encontrar el nodo asociado a cada número. 
La segunda opción era “2. Ruta más corta” que mostraba la ruta que se calculó mediante el método encontrarRutaMasCorta, que encuentraba las rutas en cada uno de los árboles, determinaba su longitud y las comparaba, mostrando la de menor longitud. 
La tercera opción era “3. Todas las rutas”, esta opción permitía ver las 3 rutas posibles que encontró el programa. Y la cuarta opción "4. Salir" que simplemente finalizaba la ejecución del programa. 
Las opciones 2 y 3 pedían que primero hubiera sido diligenciada la opción 1, después de ejecutados cada uno de los métodos de la opción escogida se le preguntaba al usuario si deseaba volver al menú principal o salir del programa. 
Esta versión del proyecto permitió calcular las rutas de manera más eficiente, ya que facilitó la comparación entre varias opciones. La implementación fue menos tediosa que cuando se utilizaron listas enlazadas, y la dificultad del código fue menor en comparación con la versión anterior. El uso de árboles mejora la organización y la optimización de las rutas, permitiendo obtener la ruta más adecuada de forma más rápida y sencilla. 

# Implementación final

Para la tercera y última implementación del sistema de optimización de rutas desarrollado en este proyecto se trabajó con grafos no dirigidos, cuyos nodos representan los 53 edificios de la universidad. 
En esta versión se utilizó la librería NetworkX de Python, la cual permite crear y manipular el grafo. Todos los nodos (edificios) están conectados entre sí con diferentes distancias representadas como pesos en las aristas. Esta librería también incorpora algoritmos como el de Dijkstra, que fue utilizado en este caso para encontrar la ruta más corta entre dos lugares. Además, NetworkX tiene integradas las funciones para añadir, eliminar o buscar elementos dentro del grafo. 
Se usó también la librería matplotlib.pyplot para visualizar gráficamente el grafo, mostrando sus conexiones y pesos. 
La creación del grafo se hizo de la siguiente manera: 
Con G = nx.Graph(), se genera un grafo no dirigido (bidireccional). Luego se construyó el diccionario con los lugares, que contiene los nodos (los edificios) y sus respectivas descripciones. El diccionario aristas con las conexiones entre nodos, basadas en la proximidad o distancia que se puede observar entre los edificios. 
Con aristas_formateadas, el diccionario de aristas se transformó en una lista de tuplas, para trabajar con NetworkX, incluyendo los pesos de cada conexión. Posteriormente, se cargaron los nodos con sus atributos y las aristas al grafo usando G.add_nodes_from(lugares.items()) y G.add_edges_from(aristas_formateadas), y se dibujó el grafo. 
Utilizando el algoritmo de Dijkstra con los pesos definidos, se calculó el camino más corto entre dos puntos. Como caso de prueba, se tomó la ruta desde el nodo 1 hasta el nodo 14. 
Después, se muestra el recorrido paso a paso según el camino más corto hallado, junto con las descripciones de los lugares por los que se debe pasar. 
Esta implementación basada en grafos resultó más eficiente que las dos versiones anteriores, desarrolladas con listas doblemente enlazadas y árboles. Aunque las estructuras manejadas anteriormente son más simples, los grafos permiten realizar más operaciones y manejar las rutas de una forma más flexible y directa. En este caso, no fue necesario definir múltiples listas o árboles para representar las rutas. Solo fue necesario agregar todos los lugares con sus respectivas descripciones a un diccionario, así como para conectar los nodos asignándoles pesos. 
Finalmente se dispone de un menú donde se le permite a la persona que va a hacer uso del programa elegir si quiere ver inicialmente el grafo con los lugares (opción 1), que pueda ingresar el lugar donde se encuentra y a donde quiere ir para encontrar la ruta más corta entre ellos (opción 2), que pueda agregar (opción 3) o eliminar (opción 4) un lugar y cuando ya no necesite hacer más uso del programa salir de él (opción 5).  
Cabe aclarar que, para poder hacer un buen uso del programa al momento de usar el menú con los lugares, se le da previamente una lista al usuario con todos los lugares disponibles para que pueda ingresar el número de los lugares correctos. 

En cuanto a la estructura del código, esta implementación es más sencilla y eficiente en términos de complejidad ya que los nodos y aristas se definen usando diccionarios, y la creación del grafo, así como el cálculo del camino más corto, se realiza mediante llamadas a funciones incorporadas en la librería y haciendo uso de los datos ya definidos. 
Haciendo un análisis de este código podemos ver que presenta una complejidad lineal de O(n) debido a que la estructura de mayor complejidad que llega a usarse es un ciclo ‘for’, ya que lo demás son asignaciones o llamado a funciones.  
