import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
lugares = {
    1: {"nombre": "Portería 27", "descripcion": "Porteria carrera 27"},
    2: {"nombre": "Luis A. Calvo", "descripcion": "Edificio de 20 metros de altura con una fachada curva en semióvalo y sin ventanas visibles. Está construido en ladrillo rojizo."},
    3: {"nombre": "Administración 1", "descripcion": "Edificio blanco con detalles grises, está compuesto por dos bloques de cuatro y dos pisos. 2 pasillos conectan los bloques en los primeros dos pisos. Tiene ventanas oscuras."},
    4: {"nombre": "Administración 3", "descripcion": "Compuesto por dos bloques amarillos mostaza, conectados por un puente verde vibrante."},
    5: {"nombre": "Auditorio José Antonio Galán", "descripcion": "Teatrino pequeño con graderías al aire libre en dos lados, de cinco y seis filas respectivamente. Las gradas son de ladrillo pequeño."},
    6: {"nombre": "Administración 2", "descripcion": "Estructura de cinco pisos de color blanco, con bloques conectados por escaleras."},
    7: {"nombre": "Bienestar Estudiantil", "descripcion": "El complejo está compuesto por tres bloques con diseños diversos. El primero tiene paneles metálicos verdes, el segundo es completamente acristalado y el tercero tiene una terraza."},
    8: {"nombre": "Casona La Perla", "descripcion": "Edificio de un solo piso de estilo colonial, con techo de tejas de barro y pisos rojizos."},
    9: {"nombre": "Ciencias Humanas 2", "descripcion": "Edificio de 9 plantas, color amarillo mostaza, ubicado frente de la portería de la carrera 27."},
    10: {"nombre": "Ingeniería Mecánica", "descripcion": "Edificio blanco de tres pisos, ubicado frente a biblioteca y al lado del auditorio Luis Eduardo Lobo, tiene tres entradas."},
    11: {"nombre": "Auditorio Luis Eduardo Lobo", "descripcion": "Este auditorio, de estructura semicircular, se encuentra junto al edificio Camilo Torres. Su techo es de color gris y el resto de la fachada es blanca."},
    12: {"nombre": "Biblioteca", "descripcion": "Edificio de cuatro plantas con una estructura de lápices verticales y con vista al interior."},
    13: {"nombre": "Instituto de Lenguas", "descripcion": "Este edificio actualmente se encuentra en construcción."},
    14: {"nombre": "Ingeniería Industrial", "descripcion": "Este edificio cuenta con 5 pisos, tiene en su entrada un letrero con su nombre 'Ingeniería Industrial'. Es de color blanco y gris, cuenta con una rampa a la derecha y escaleras al frente para el ingreso."},
    15: {"nombre": "Laboratorio Biología Vegetal", "descripcion": "Edificio blanco, minimalista de un piso"},
    16: {"nombre": "Laboratorio de Livianos", "descripcion": "Construcción de cuatro pisos, de color blanco, ubicado después del edificio de humanas y unido por un pasillo al tercer piso del Camilo Torres."},
    17: {"nombre": "Camilo Torres", "descripcion": "Este edificio de 5 pisos está construido en ladrillo de color rojizo, se destaca por tener en su fachada la imagen del sacerdote y activista colombiano Camilo Torres."},
    18: {"nombre": "CENTIC", "descripcion": "Edificio de cómputo de la universidad, pintado de blanco y 4 pisos, con cristales en el exterior en la parte frontal y trasera."},
    19: {"nombre": "Uisalud", "descripcion": "Este edificio cuenta con 3 pisos, tiene su nombre en grande en la fachada, es de colores gris y blanco, y cuenta con varios ventanales. Está ubicado detrás del CENTIC y junto al Aula Máxima de Ciencias."},
    20: {"nombre": "Federico Mamitza Bayer", "descripcion": "Edificio de muro de ladrillo, 3 plantas y reja amplia para el ingreso."},
    21: {"nombre": "Ingeniería E3T", "descripcion": "En este edificio se encuentran la Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones y cuenta con 4 pisos. Es de color blanco y gris, con puertas de vidrio, y se identifica por su letrero de 'E3T' en la parte superior izquierda de su entrada. Está ubicado junto al edificio de Ingeniería Industrial."},
    22: {"nombre": "Facultad de Ciencias", "descripcion": "Edificio de 4 pisos alargado con dos salientes de latrillo rojo en los expremos, la de la derecha tiene una impresion de Camilo Torres con color negro. La parte central del edificio es mayoritariamante blanca."},
    23: {"nombre": "Ingeniería Química", "descripcion": "Este edificio cuenta con dos niveles, se reconoce por su nombre en letras rojas en la parte superior y por la escultura llamada Torre de Destilación ubicada en su entrada, que representa una torre utilizada en los laboratorios de procesos de ingeniería química. Su fachada es de color blanco."},
    24: {"nombre": "Aula Máxima de Ciencias", "descripcion": "Edificio blanco con una entrada principal concava (esta unos pasos dentro del edificio) en la parte posterior, entre 2 y 3 pisos, de color blanco. Al la izquierda tiene una especie de grafiti con el lema <<12 años, viva la FEU>>"},
    25: {"nombre": "Bienestar Pro", "descripcion": "Edificio de un color parecido al vino tinto, pero no tan oscuro. Su fachada presenta una decoración atípica, ya que parecen ser láminas de aproximadamente un metro largo, apiladas una encima de la otra creando formas simétricas a lo largo de toda la fachada."},
    26: {"nombre": "Laboratorio de Alta Tensión", "descripcion": "Edificio blanco, alargado y de dos pisos. Posee solo 1 entrada en la parte frontal y tiene multiples ventanas a lo largo en ambos pisos"},
    27: {"nombre": "Laboratorio de Hidráulica", "descripcion": "Edificio de color blanco de 2 pisos (la mayor parte del edificio es de 1 piso,pero hay una pequeña sección de segundo), se distingue por 3 <<aletas>> de color mostaza, dos ubicadas justo sobre el primer piso y la tercera sobre la seccion del segundo."},
    28: {"nombre": "Talleres de Diseño Industria", "descripcion": "Edificio de un solo piso, distintivo por sus colores llamativos ya que tiene <<secciones>> verticales de azul y rojo intercalados"},
    29: {"nombre": "Planta de Aceros", "descripcion": "Edificio alargado de color ladrillo, a la derecha tiene 2 <<torres>> altas, el resto de la construccion es de un solo piso"},
    30: {"nombre": "Jorge Bautista Vesga", "descripcion": "Edificio de escuela de Ingeniería Metalúrgica y Ciencia de Materiales, 3 pisos, con muro de ladrillo y al final de la calle."},
    31: {"nombre": "Facultad de Ingenierías Físico-Mecánicas", "descripcion": "Esta facultad cuenta con 4 niveles, está construida en ladrillo de color rojizo, en su entrada se puede apreciar un letrero con su nombre y se identifica principalmente por la figura denominada Corte de construcción al Viento construida en hierro y PVC."},
    32: {"nombre": "Daniel Casas", "descripcion": "Edificio de tres pisos, color ladrillo, con ventanales en la mayor parte de su extensión."},
    33: {"nombre": "Residencias Estudiantiles", "descripcion": "Este edificio combina un diseño moderno con elementos funcionales, caracterizado por líneas rectas, ventanales amplios y un pasaje abierto en la planta baja. Su fachada blanca y los detalles en concreto expuesto le dan un aspecto limpio y sobrio."},
    34: {"nombre": "EDIC", "descripcion": "El Edificio de Investigaciones de la Facultad de Ciencias, está constituido por 8 niveles, se distingue por su color crema, casi amarillo, y por su fachada con pequeñas ventanas blancas y cafés. Está ubicado junto al Laboratorio de Livianos."},
    35: {"nombre": "Canchas de Squash", "descripcion": "Ubicadas al lado del estadio 1ero de Marzo son dos bloques, el primero tiene las graderias ascendentes y en la parte superior una pequeña seccion de sintetico, la otra parte esta justo al frente y son las canchas en sí."},
    36: {"nombre": "Ciencias Humanas (Virginia Gutiérrez)", "descripcion": "Edificio de cinco pisos, con muro de ladrillo, se identifica por su planetario en la última planta."},
    37: {"nombre": "Canchas de tenis", "descripcion": "Dos canchas pequeñas de color azul con sus respectivas graderias de ese mismo color."},
    38: {"nombre": "Estadio 1ero de marzo", "descripcion": "Estadio con pista de atletismo de ocho carriles, alternando azul claro y oscuro que rodea el campo central."},
    39: {"nombre": "Cancha de Fútbol Sur", "descripcion": "Cancha pequeña en arena ubicada al lado del estadio Primero de Marzo."},
    40: {"nombre": "Canchas Múltiples", "descripcion": "Área deportiva con varias canchas al aire libre para diversas disciplinas."},
    41: {"nombre": "Coliseo UIS", "descripcion": "Esta ubicado al sureste del campus, cuenta con una cancha polifuncional, camerinos, oficinas y gradería. Tiene 2 pisos y su fachada es en ladrillo rojizo, tiene unas lineas de colores y su techo tiene un estilo semicurvo."},
    42: {"nombre": "Diamante de Béisbol-Sóftbol", "descripcion": "Espacio con las medidas y diseño especiales para poder practicar ese deporte, es de grama y está cercado."},
    43: {"nombre": "CENIVAM", "descripcion": "Está rodeado de plantas y tiene una cerca azul celeste. El edificio de aproximadamente 4 pisos y es muy colorido, alterna entre el verde, amarillo, azul, naranja y rojo, los cuales están distribuidos por secciones aparentemente al azar"},
    44: {"nombre": "Portería 25", "descripcion": "Porteria carrera 25"},
    45: {"nombre": "Laboratorio Estructura y Materiales", "descripcion": "Edificio aparentemente de 2 pisos, con los filas de ventanas en ambos pisos. Cuenta con una única entrada en el frente."},
    46: {"nombre": "Gestión Logística", "descripcion": "Edificio de varios pisos con fachada blanca y paneles verticales marrones. Las escaleras laterales conectan todos los niveles."},
    47: {"nombre": "Mesas de Ping Pong", "descripcion": "3 mesas verdes al aire libre justo a la derecha de las canchas de tenis"},
    48: {"nombre": "Tienda Universitaria", "descripcion": "Tiene un letrero con su nombre en la fachada, es de color blanco y azul celeste y está ubicada enfrente del edificio de humanas 2."},
    49: {"nombre": "Planta de Reciclaje y Compostaje", "descripcion": "Esta ubicada el el punto mas al noreste de la universidad, es la unica entrada despues de la del modulo de psicorientacion"},
    50: {"nombre": "Bienestar Campestre", "descripcion": "Espacio al aire libre con techos verdes y mesas."},
    51: {"nombre": "Portería 30", "descripcion": "Porteria carrera 30"},
    52: {"nombre": "Auditorio Jorge Zalama", "descripcion": "Un gran bloque <<recubierto>> con laminas verticales muy delgadas y de color amarillo que le aportan este tono si es visto desde lejos"},
    53: {"nombre": "Módulo de Psicorientación", "descripcion": "Estrustura de un solo piso de color amarillo compuesto por laminas verticales de este color"},
    54: {"nombre": "Skate Park", "descripcion": "Parque de forma triangular con diversas formas y colinas artificiales, podría decirse, diseñadas específicamente para practicar este deporte."}
}

aristas = {
    1: [(48, 5), (2, 20), (9, 14)],
    2: [(1, 20), (3, 20), (10, 10), (37, 15)],
    3: [(2, 20), (4, 5), (11, 5), (52, 5)],
    4: [(3, 5), (6, 5), (5, 3), (38, 5)],
    5: [(4, 3), (13, 10), (12, 10)],
    6: [(4, 5), (7, 5)], 
    7: [(6, 5), (8, 5), (50, 10)],
    8: [(7, 5), (14, 5), (13, 10)],
    9: [(1, 14), (10, 5), (36, 5)],
    10: [(9, 5), (2, 10), (11, 5)],
    11: [(10, 5), (12, 5), (17, 5), (3, 5)],
    12: [(11, 5), (5, 10), (18, 5)],
    13: [(5, 10), (8, 10), (20, 10), (14, 10)],
    14: [(13, 10), (8, 5), (21, 5), (15, 20)], 
    15: [(14, 20), (45, 5)],
    16: [(17, 0), (34, 5), (22, 10)],
    17: [(11, 5), (16, 0), (18, 5)],
    18: [(17, 5), (12, 5), (23, 5), (19, 15)],
    19: [(24, 5), (20, 10), (18, 15)],
    20: [(19, 10), (13, 10), (21, 10)],
    21: [(20, 10), (14, 5), (27, 10) ],
    22: [(16, 10), (29, 5), (30, 5)],
    23: [(18, 5), (30, 10), (24, 15)],
    24: [(23, 15), (19, 5), (25, 15)], 
    25: [(24, 15), (31, 10), (26, 10), (32, 5)],
    26: [(25, 10), (27, 10), (28, 10), (45, 20)],
    27: [(26, 10), (28, 10), (21, 10)],
    28: [(27, 10), (26, 10)], 
    29: [(22, 5), (30, 5), (34, 10), (44, 5)],
    30: [(29, 5), (23, 10), (22, 5), (31, 5), (44, 10)],
    31: [(30, 5), (25, 10), (32, 15)],
    32: [(31, 15), (25, 5)],
    33: [(35, 5), (46, 5), (42, 5)], 
    34: [(29, 10), (16, 5), (44, 10)], 
    35: [(40, 5), (33, 5)],
    36: [(9, 5), (48, 5)],
    37: [(2, 15), (47, 5), (39, 2)],
    38: [(4, 5), (40, 2), (52, 4)],
    39: [(37, 2), (41, 5), (51, 15), (47, 5)],
    40: [(38, 2), (35, 5), (54, 2), (42, 15)],
    41: [(39, 5), (51, 5), (46, 5)],
    42: [(33, 5), (46, 2), (40, 15)],
    43: [(51, 20), (46, 15), (49, 30)],
    44: [(34, 10), (30, 10), (29, 5)],
    45: [(15, 5), (26, 20)], 
    46: [(43, 15), (42, 2), (41, 5), (33, 5)], 
    47: [(37, 5), (39, 5)], 
    48: [(1, 5), (36, 5)], 
    49: [(53, 15), (43, 30)], 
    50: [(7, 10), (53, 15)],
    51: [(43, 20), (41, 5), (39, 15)], 
    52: [(3, 5), (38, 4)],
    53: [(49, 15), (50, 15)],
    54: [(40, 2)]
}

# Diccionario de numeros 
dictNumeros = {str(i): i for i in range(1, 101)}
# Aristas originales llevadas al formato de networkx
aristas_formateadas = [
    (origen, destino, {'weight': peso})
    for origen, destinos in aristas.items()
    for destino, peso in destinos
]
# Agregar nodos ya arista a la instacia de networkx
G.add_nodes_from(lugares.items())
G.add_edges_from(aristas_formateadas)

# Función para imprimir los nodos y su nombre
def imprimirNombreNodos():
    for n in G.nodes:
        print(str(n)+": "+G.nodes[n]["nombre"])

# Función para mostrar el grafo
def plotearGrafo():
    pos = nx.spring_layout(G, seed=42)  
    labels = {n: G.nodes[n]["nombre"] for n in G.nodes}
    #edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in G.edges(data=True)}
    nx.draw(G,pos, with_labels=True, labels=labels,font_size=6,width=0.4, node_size=100) 
    #nx.draw_networkx_edge_labels(G, pos,edge_labels=edge_labels,font_size=5)
    plt.show()

# Función para encontrar la ruta mas corta 
def rutaMasCorta(lugarPartida, lugarLlegada):
    path = nx.shortest_path(G, dictNumeros[str(lugarPartida)], dictNumeros[str(lugarLlegada)], weight="weight")
    total_weight = nx.shortest_path_length(G, dictNumeros[str(lugarPartida)], dictNumeros[str(lugarLlegada)], weight="weight")
    contador = 1
    for numero in path:
        nombre = lugares[numero].get("nombre")
        descripcion = lugares[numero].get("descripcion")
        print(contador)
        print(nombre+ ": " +descripcion)
        contador += 1

    print("Camino más corto: ", path)
    print("Peso del recorrido: ", total_weight)
    print(" ")

# Función par agregar un nuevo lugar al grafo
def agregarLugar(nuevoLugar,descripcionLugar,numero):
    G.add_nodes_from([dictNumeros[str(numero)]], nombre = nuevoLugar, descripcion = descripcionLugar)


def menu():
    
    
    global contadorLugares 
    contadorLugares = 35
    print("Nodos del grafo: ")
    imprimirNombreNodos()
    print(" ")
    while True:
        print("\nMenú:")
        print("1. Mostrar Grafo")
        print("2. Encontrar la ruta mas corta")
        print("3. Agregar lugar")
        print("4. Eliminar lugar")
        print("5. Salir")
        
        opcion = input("¿Qué función desea utilizar? ")

        if opcion == '1':
            plotearGrafo()
            print(" ")

        elif opcion == '2':
            lugarPartida = input("Ingrese el lugar de partida: ")
            lugarLlegada = input("Ingrese el lugar de Llegada: ")
            rutaMasCorta(lugarPartida, lugarLlegada)
            print(" ")

        elif opcion == '3':
            nuevoLugar = input("Ingrese el nombre del nuevo lugar: ")
            descripcionLugar = input( "Ingrese la descripción del nuevo lugar: ")
            contadorLugares += 1
            numero = str(contadorLugares)
            agregarLugar(nuevoLugar,descripcionLugar,numero)
            print("Lugar ingresado al número "+numero)
            print(" ")


        elif opcion == '4':
            lugarAEliminar = input("Ingrese el número del lugar a eliminar: ")
            numero = dictNumeros[lugarAEliminar]
            G.remove_node(numero)
            contadorLugares += 1
            print(" ")

        elif opcion == '5':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción correcta.")
            print(" ")

menu()
