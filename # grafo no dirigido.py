import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
lugares = {
    1: {"nombre": "Portería 25", "descripcion": "Porteria carrera 25"},
    2: {"nombre": "Portería 30", "descripcion": "Porteria carrera 30"},
    3: {"nombre": "Portería 27", "descripcion": "Porteria carrera 27"},
    4: {"nombre": "Coliseo UIS", "descripcion": "Esta ubicado al sureste del campus, cuenta con una cancha polifuncional, camerinos, oficinas y gradería. Tiene 2 pisos y su fachada es en ladrillo rojizo, tiene unas lineas de colores y su techo tiene un estilo semicurvo."},
    5: {"nombre": "Luis A. Calvo", "descripcion": "Edificio de 20 metros de altura con una fachada curva en semióvalo y sin ventanas visibles. Está construido en ladrillo rojizo."},
    6: {"nombre": "Residencias de Estudiantes", "descripcion": "Edificio de varios pisos con fachada blanca y paneles verticales marrones. Las escaleras laterales conectan todos los niveles."},
    7: {"nombre": "Estadio 1ero de marzo", "descripcion": "Estadio con pista de atletismo de ocho carriles, alternando azul claro y oscuro que rodea el campo central."},
    8: {"nombre": "Canchas Múltiples", "descripcion": "Área deportiva con varias canchas al aire libre para diversas disciplinas."},
    9: {"nombre": "Administración 1", "descripcion": "Edificio blanco con detalles grises, está compuesto por dos bloques de cuatro y dos pisos. 2 pasillos conectan los bloques en los primeros dos pisos. Tiene ventanas oscuras."},
    10: {"nombre": "Administración 2", "descripcion": "Estructura de cinco pisos de color blanco, con bloques conectados por escaleras."},
    11: {"nombre": "Administración 3", "descripcion": "Compuesto por dos bloques amarillos mostaza, conectados por un puente verde vibrante."},
    12: {"nombre": "Bienestar Estudiantil", "descripcion": "El complejo está compuesto por tres bloques con diseños diversos. El primero tiene paneles metálicos verdes, el segundo es completamente acristalado y el tercero tiene una terraza."},
    13: {"nombre": "Bienestar Campestre", "descripcion": "Espacio al aire libre con techos verdes y mesas."},
    14: {"nombre": "Auditorio José Antonio Galán", "descripcion": "Teatrino pequeño con graderías al aire libre en dos lados, de cinco y seis filas respectivamente. Las gradas son de ladrillo pequeño."},
    15: {"nombre": "Casona La Perla", "descripcion": "Edificio de un solo piso de estilo colonial, con techo de tejas de barro y pisos rojizos."},
    16: {"nombre": "Tienda Universitaria", "descripcion": "Tiene un letrero con su nombre en la fachada, es de color blanco y azul celeste y está ubicada enfrente del edificio de humanas 2."},
    17: {"nombre": "Humanas 2", "descripcion": "Edificio de 9 plantas, color amarillo mostaza, ubicado frente de la portería de la carrera 27."},
    18: {"nombre": "Ingeniería Mecánica", "descripcion": "Edificio blanco de tres pisos, ubicado frente a biblioteca y al lado del auditorio Luis Eduardo Lobo, tiene tres entradas."},
    19: {"nombre": "Humanas 1", "descripcion": "Edificio de cinco pisos, con muro de ladrillo, se identifica por su planetario en la última planta."},
    20: {"nombre": "Laboratorio de Livianos", "descripcion": "Construcción de cuatro pisos, de color blanco, ubicado después del edificio de humanas y unido por un pasillo al tercer piso del Camilo Torres."},
    21: {"nombre": "EDIC", "descripcion": "El Edificio de Investigaciones de la Facultad de Ciencias, está constituido por 8 niveles, se distingue por su color crema, casi amarillo, y por su fachada con pequeñas ventanas blancas y cafés. Está ubicado junto al Laboratorio de Livianos."},
    22: {"nombre": "Auditorio Luis Eduardo Lobo", "descripcion": "Este auditorio, de estructura semicircular, se encuentra junto al edificio Camilo Torres. Su techo es de color gris y el resto de la fachada es blanca."},
    23: {"nombre": "Biblioteca", "descripcion": "Edificio de cuatro plantas con una estructura de lápices verticales y con vista al interior."},
    24: {"nombre": "Instituto de Lenguas", "descripcion": "Este edificio actualmente se encuentra en construcción."},
    25: {"nombre": "Federico Mamitza Bayer", "descripcion": "Edificio de muro de ladrillo, 3 plantas y reja amplia para el ingreso."},
    26: {"nombre": "Ingeniería Industrial", "descripcion": "Este edificio cuenta con 5 pisos, tiene en su entrada un letrero con su nombre 'Ingeniería Industrial'. Es de color blanco y gris, cuenta con una rampa a la derecha y escaleras al frente para el ingreso."},
    27: {"nombre": "Ingeniería E3T", "descripcion": "En este edificio se encuentran la Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones y cuenta con 4 pisos. Es de color blanco y gris, con puertas de vidrio, y se identifica por su letrero de 'E3T' en la parte superior izquierda de su entrada. Está ubicado junto al edificio de Ingeniería Industrial."},
    28: {"nombre": "Diseño Industrial", "descripcion": "Construcción de un solo piso, con tejado visible."},
    29: {"nombre": "Laboratorios de Alta Tensión", "descripcion": "Este edificio es de color blanco y tiene dos pisos."},
    30: {"nombre": "Camilo Torres", "descripcion": "Este edificio de 5 pisos está construido en ladrillo de color rojizo, se destaca por tener en su fachada la imagen del sacerdote y activista colombiano Camilo Torres."},
    31: {"nombre": "CENTIC", "descripcion": "Edificio de cómputo de la universidad, pintado de blanco y 4 pisos, con cristales en el exterior en la parte frontal y trasera."},
    32: {"nombre": "Ingeniería Química", "descripcion": "Este edificio cuenta con dos niveles, se reconoce por su nombre en letras rojas en la parte superior y por la escultura llamada Torre de Destilación ubicada en su entrada, que representa una torre utilizada en los laboratorios de procesos de ingeniería química. Su fachada es de color blanco."},
    33: {"nombre": "Jorge Bautista Vesga", "descripcion": "Edificio de escuela de Ingeniería Metalúrgica y Ciencia de Materiales, 3 pisos, con muro de ladrillo y al final de la calle."},
    34: {"nombre": "Ingenierías Físico-Mecánicas", "descripcion": "Esta facultad cuenta con 4 niveles, está construida en ladrillo de color rojizo, en su entrada se puede apreciar un letrero con su nombre y se identifica principalmente por la figura denominada Corte de construcción al Viento construida en hierro y PVC."},
    35: {"nombre": "Uisalud", "descripcion": "Este edificio cuenta con 3 pisos, tiene su nombre en grande en la fachada, es de colores gris y blanco, y cuenta con varios ventanales. Está ubicado detrás del CENTIC y junto al Aula Máxima de Ciencias."},
}

aristas = {
    1: [(21,10), (33, 10), (34, 20)],
    2: [(4, 5), (6, 20)],
    3: [(17, 5), (19, 12), (5, 10), (16,2), (18, 20)],
    4: [(6, 15), (7, 20), (2, 5)],
    5: [(3, 10), (9, 12), (17, 7), (18, 7), (22, 10), (7, 12), (16, 5)],
    6: [(4, 15), (2, 20), (7,5), (8,10)], 
    7: [(5, 12), (8, 5), (9,8), (10, 7), (11, 5), (12, 10), (13, 14), (6, 5), (4, 20)],
    8: [(7, 5), (6, 10)],
    9: [(5, 12), (7, 8), (11, 2), (23, 12), (22, 3), (14, 6), (18, 7)],
    10: [(7, 7), (14, 6), (12, 4), (13, 7), (15, 12), (11, 2)],
    11: [(9,2), (10, 2), (7,5), (14, 2), (23, 15), (22, 5)],
    12: [(13, 3), (14, 6), (15, 3), (7, 10), (10, 4)],
    13: [(10, 7), (7, 14), (12, 3)],
    14: [(9, 6), (10, 6), (11, 2), (12, 6), (15, 5), (23, 7), (24, 10)], 
    15: [(12, 3), (10, 12), (14, 5), (26, 3), (24, 3)],
    16: [(19, 10), (17, 3), (3, 2), (18, 18), (20, 15), (5, 5)],
    17: [(18, 4), (16, 3), (20, 5), (30, 6), (5, 3), (19, 4)],
    18: [(17, 4), (23, 8), (3, 20), (5, 7), (16, 18), (22, 2), (9, 3), (10, 12), (30, 2), (20, 5), (19, 20)],
    19: [(3, 12), (16, 10), (17, 4), (20, 5)],
    20: [(16, 15), (17, 5), (30, 1), (19, 5), (18, 3), (22, 5), (21, 3)],
    21: [(20, 3), (33, 10), (34, 30), (30, 6), (1, 10)],
    22: [(30, 2), (23, 3), (9, 3), (11, 5), (31, 5), (18, 2), (5, 10), (14, 10), (20, 5)],
    23: [(22,3), (30, 5), (9, 12), (11, 15), (31, 3), (18, 8), (14, 8), (24, 4), (35, 8)],
    24: [(23, 4), (25, 2), (15, 3), (14, 3), (31, 15), (35, 13), (27, 8), (26, 3)], 
    25: [(23, 10), (24, 2), (31, 15), (35, 4), (27, 3), (26, 8), (28, 15), (29, 12)],
    26: [(15, 3), (25, 8), (24, 6), (29, 17), (28, 20), (27, 2), (35, 4)],
    27: [(26, 2), (25, 3), (24, 8), (35, 10), (28, 15), (29, 10), (15, 6)],
    28: [(25, 15), (26, 20), (27, 15), (29, 7)], 
    29: [(25, 12), (26, 17), (27, 10), (28, 7)],
    30: [(17, 6), (18, 2), (20, 1), (21, 6), (22, 2), (23,5), (31, 6), (32, 9)],
    31: [(22, 5), (23,3), (24, 15), (25, 15), (30, 6), (35, 8), (32, 3), (33, 10)],
    32: [(31, 3), (33, 7), (34, 10), (35, 6), (30, 9)],
    33: [(1, 10), (21, 10), (31, 10), (32, 7), (34, 3)], 
    34: [(1, 20), (21, 30), (32, 10), (33, 3)], 
    35: [(23, 8), (24, 13), (25, 4), (26, 4), (27, 10), (31, 8), (32, 6)]
}

dictNumeros = {str(i): i for i in range(1, 101)}
aristas_formateadas = [
    (origen, destino, {'weight': peso})
    for origen, destinos in aristas.items()
    for destino, peso in destinos
]


G.add_nodes_from(lugares.items())
G.add_edges_from(aristas_formateadas)
#pos = nx.spring_layout(G, seed=42)  
#labels = {n: G.nodes[n]["nombre"] for n in G.nodes}
#nx.draw(G,pos, with_labels=True, labels=labels,font_size=6,width=0.8, node_size=500)  # with_labels=True para ver los nodos numerados
#plt.show()

#partida = 1
#salida = 14
#path = nx.shortest_path(G, partida, salida, weight="weight")
#total_weight = nx.shortest_path_length(G, partida, salida, weight="weight")
#contador = 1


#for numero in path:
 #   descripcion = lugares[numero].get("descripcion")
 #   print(contador)
 #   print(descripcion)
#    contador += 1

#print("Camino más corto:", path)
#print("Peso total:", total_weight)
def imprimirNombreNodos():
    for n in G.nodes:
        print(str(n)+": "+G.nodes[n]["nombre"])

def menu():
    
    
    global contadorLugares 
    contadorLugares = 35
    while True:

        print("Nodos del grafo: ")
        imprimirNombreNodos()
        print(" ")
        print("\nMenú:")
        print("1. Mostrar Grafo")
        print("2. Encontrar la ruta mas corta")
        print("3. Agregar lugar")
        print("4. Eliminar lugar")
        print("5. Salir")
        
        opcion = input("¿Qué función desea utilizar? ")

        if opcion == '1':
            pos = nx.spring_layout(G, seed=42)  
            labels = {n: G.nodes[n]["nombre"] for n in G.nodes}
            #edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in G.edges(data=True)}
            nx.draw(G,pos, with_labels=True, labels=labels,font_size=6,width=0.8, node_size=500) 
            #nx.draw_networkx_edge_labels(G, pos,edge_labels=edge_labels,font_size=5)
            plt.show()
            print(" ")

        elif opcion == '2':
            lugarPartida = input("Ingrese el lugar de partida: ")
            lugarLlegada = input("Ingrese el lugar de Llegada: ")
            path = nx.shortest_path(G, dictNumeros[lugarPartida], dictNumeros[lugarLlegada], weight="weight")
            total_weight = nx.shortest_path_length(G, dictNumeros[lugarPartida], dictNumeros[lugarLlegada], weight="weight")
            contador = 1
            for numero in path:
                descripcion = lugares[numero].get("descripcion")
                print(contador)
                print(descripcion)
                contador += 1

            print("Camino más corto: ", path)
            print("Peso del recorrido: ", total_weight)
            print(" ")

        elif opcion == '3':
            nuevoLugar = input("Ingrese el nombre del nuevo lugar: ")
            descripcionLugar = input( "Ingrese la descripción del nuevo lugar: ")
            contadorLugares += 1
            numero = str(contadorLugares)
            G.add_nodes_from([dictNumeros[numero]], nombre = nuevoLugar, descripcion = descripcionLugar)
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


#Llamada a la función del menú
menu()
