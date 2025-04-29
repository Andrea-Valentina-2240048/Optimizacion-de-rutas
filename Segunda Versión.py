from bigtree import Node
from bigtree import print_tree

class Arbol():
    def __init__(self):
        self.porteria25 = Node("Portería 25", Num = 1,descripcion='Porteria carrera 25')
        self.porteria30 = Node("Portería 30", Num = 2,descripcion='Porteria carrera 30')
        self.porteria27 = Node("Portería 27", Num = 3,descripcion='Porteria carrera 27')
        self.coliseo = Node("Coliseo UIS", descripcion="Esta ubicado al sureste del campus, cuenta con una cancha polifuncional, camerinos, oficinas y gradería. Tiene 2 pisos y su fachada es en ladrillo rojizo, tiene unas lineas de colores y su techo tiene un estilo semicurvo.", Num=4)
        self.luis_a_calvo = Node("Luis A. Calvo", descripcion="Edificio de 20 metros de altura con una fachada curva en semióvalo y sin ventanas visibles. Está construido en ladrillo rojizo.", Num=5)
        self.residencias = Node("Residencias de Estudiantes", descripcion="Edificio de varios pisos con fachada blanca y paneles verticales marrones. Las escaleras laterales conectan todos los niveles.", Num=6)
        self.estadio = Node("Estadio 1ero de marzo", descripcion="Estadio con pista de atletismo de ocho carriles, alternando azul claro y oscuro que rodea el campo central.", Num=7)
        self.canchas = Node("Canchas Múltiples", descripcion="Área deportiva con varias canchas al aire libre para diversas disciplinas.", Num=8)
        self.admin1 = Node("Administración 1",descripcion="Edificio blanco con detalles grises, está compuesto por dos bloques de cuatro y dos pisos. 2 pasillos conectan los bloques en los primeros dos pisos. Tiene ventanas oscuras.", Num=9)
        self.admin2 = Node("Administración 2", descripcion="Estructura de cinco pisos de color blanco, con bloques conectados por escaleras.", Num=10)
        self.admin3 = Node("Administración 3", descripcion="Compuesto por dos bloques amarillos mostaza, conectados por un puente verde vibrante.", Num=11)
        self.bienestar_estudiantil = Node("Bienestar Estudiantil", descripcion="El complejo está compuesto por tres bloques con diseños diversos. El primero tiene paneles metálicos verdes, el segundo es completamente acristalado y el tercero tiene una terraza.", Num=12)
        self.bienestar_campestre = Node("Bienestar Campestre", descripcion="Espacio al aire libre con techos verdes y mesas.",  Num=13)
        self.auditorio_galan = Node("Auditorio José Antonio Galán", descripcion="Teatrino pequeño con graderías al aire libre en dos lados, de cinco y seis filas respectivamente. Las gradas son de ladrillo pequeño.", Num=14)
        self.casona = Node("Casona La Perla", descripcion="Edificio de un solo piso de estilo colonial, con techo de tejas de barro y pisos rojizos.", Num=15)
        self.tienda_universitaria = Node("Tienda Universitaria", descripcion="Tiene un letrero con su nombre en la fachada, es de color blanco y azul celeste y está ubicada enfrente del edificio de humanas 2.", Num=16)
        self.humanas2 = Node("Humanas 2", descripcion="Edificio de 9 plantas, color amarillo mostaza, ubicado frente de la portería de la carrera 27.", Num=17)
        self.mecanica = Node("Ingeniería Mecánica", descripcion="Edificio blanco de tres pisos, ubicado frente a biblioteca y al lado del auditorio Luis Eduardo Lobo, tiene tres entradas.", Num=18)
        self.humanas1 = Node("Humanas 1", descripcion="Edificio de cinco pisos, con muro de ladrillo, se identifica por su planetario en la última planta.", Num=19)
        self.lab_livianos = Node("Laboratorio de Livianos", descripcion="Construcción de cuatro pisos, de color blanco, ubicado después del edificio de humanas y unido por un pasillo al tercer piso del Camilo Torres.", Num=20)
        self.edic = Node("EDIC", descripcion="El Edificio de Investigaciones de la Facultad de Ciencias, está constituido por 8 niveles, se distingue por su color crema, casi amarillo, y por su fachada con pequeñas ventanas blancas y cafés. Está ubicado junto al Laboratorio de Livianos.", Num=21)
        self.auditorio_lobo = Node("Auditorio Luis Eduardo Lobo", descripcion="Este auditorio, de estructura semicircular, se encuentra junto al edificio Camilo Torres. Su techo es de color gris y el resto de la fachada es blanca.", Num=22)
        self.biblioteca = Node("Biblioteca", descripcion="Edificio de cuatro plantas con una estructura de lápices verticales y con vista al interior.", Num=23)
        self.instituto_lenguas = Node("Instituto de Lenguas", descripcion="Este edificio actualmente se encuentra en construcción.", Num=24)
        self.federico = Node("Federico Mamitza Bayer", descripcion="Edificio de muro de ladrillo, 3 plantas y reja amplia para el ingreso.", Num=25)
        self.ingenieria_industrial = Node("Ingeniería Industrial", descripcion="Este edificio cuenta con 5 pisos, tiene en su entrada un letrero con su nombre 'Ingeniería Industrial'. Es de color blanco y gris, cuenta con una rampa a la derecha y escaleras al frente para el ingreso.", Num=26)
        self.ingenieria_e3t = Node("Ingeniería E3T", descripcion="En este edificio se encuentran la Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones y cuenta con 4 pisos. Es de color blanco y gris, con puertas de vidrio, y se identifica por su letrero de 'E3T' en la parte superior izquierda de su entrada. Está ubicado junto al edificio de Ingeniería Industrial.", Num=27)
        self.diseno_industrial = Node("Diseño Industrial", descripcion="Construcción de un solo piso, con tejado visible.", Num=28)
        self.alta_tension = Node("Laboratorios de Alta Tensión", descripcion="Este edificio es de color blanco y tiene dos pisos.", Num=29)
        self.camilo_torres = Node("Camilo Torres", descripcion="Este edificio de 5 pisos está construido en ladrillo de color rojizo, se destaca por tener en su fachada la imagen del sacerdote y activista colombiano Camilo Torres.", Num=30)
        self.centic = Node("CENTIC", descripcion="Edificio de cómputo de la universidad, pintado de blanco y 4 pisos, con cristales en el exterior en la parte frontal y trasera.", Num=31)
        self.ingenieria_quimica = Node("Ingeniería Química", descripcion="Este edificio cuenta con dos niveles, se reconoce por su nombre en letras rojas en la parte superior y por la escultura llamada Torre de Destilación ubicada en su entrada, que representa una torre utilizada en los laboratorios de procesos de ingeniería química. Su fachada es de color blanco.", Num=32)
        self.jorge_bautista_vesga = Node("Jorge Bautista Vesga", descripcion="Edificio de escuela de Ingeniería Metalúrgica y Ciencia de Materiales, 3 pisos, con muro de ladrillo y al final de la calle.", Num=33)
        self.fisicomecanica = Node("Ingenierías Físico-Mecánicas", descripcion="Esta facultad cuenta con 4 niveles, está construida en ladrillo de color rojizo, en su entrada se puede apreciar un letrero con su nombre y se identifica principalmente por la figura denominada Corte de construcción al Viento construida en hierro y PVC.", Num=34)
        self.uisalud = Node("Uisalud", descripcion="Este edificio cuenta con 3 pisos, tiene su nombre en grande en la fachada, es de colores gris y blanco, y cuenta con varios ventanales. Está ubicado detrás del CENTIC y junto al Aula Máxima de Ciencias.", Num=35)

        
        self.dicNodos = {"Portería 25": self.porteria25,"Portería 30": self.porteria30,"Portería 27": self.porteria27,
            "Coliseo UIS": self.coliseo, "Luis A. Calvo": self.luis_a_calvo, "Residencias de Estudiantes": self.residencias,
            "Estadio 1ero de marzo": self.estadio, "Canchas Múltiples": self.canchas, "Administración 1": self.admin1,                      
            "Administración 2": self.admin2, "Administración 3": self.admin3, "Bienestar Estudiantil": self.bienestar_estudiantil,  
            "Bienestar Campestre": self.bienestar_campestre, "Auditorio José Antonio Galán": self.auditorio_galan, 
            "Casona La Perla": self.casona, "Tienda Universitaria": self.tienda_universitaria, "Humanas 2": self.humanas2,                           
            "Ingeniería Mecánica": self.mecanica, "Humanas 1": self.humanas1, "Laboratorio de Livianos": self.lab_livianos,         
            "EDIC": self.edic, "Auditorio Luis Eduardo Lobo": self.auditorio_lobo, "Biblioteca": self.biblioteca, "Instituto de Lenguas": self.instituto_lenguas,       
            "Federico Mamitza Bayer": self.federico, "Ingeniería Industrial": self.ingenieria_industrial, "Ingeniería E3T": self.ingenieria_e3t,                
            "Diseño Industrial": self.diseno_industrial, "Laboratorios de Alta Tensión": self.alta_tension, "Camilo Torres": self.camilo_torres,                  
            "CENTIC": self.centic, "Ingeniería Química": self.ingenieria_quimica, "Jorge Bautista Vesga": self.jorge_bautista_vesga,    
            "Ingenierías Físico-Mecánicas": self.fisicomecanica,  
            "Uisalud": self.uisalud
            }
    def imprimirNodos(self):
                for nombre, nodo in self.dicNodos.items():
                    print(f"Nodo {nodo.Num}: {nombre}")

    def buscarNodoPorNumero(self, numero):
        lugar_encontrado = None  
        for nodo in self.dicNodos.values():
            if nodo.Num == numero:
                lugar_encontrado = nodo  
                break 

        if lugar_encontrado is None:  
            print("Ese lugar no se encuentra en el mapa")
            return None  

        
        return lugar_encontrado.name 
        
    def asignarHijo(self,padre,hijo):
        self.dicNodos[padre].append(self.dicNodos[hijo])

    def mostrarArbol(self, nombre_porteria):
        if nombre_porteria == "Portería 27":
            print_tree(self.porteria27)
        if nombre_porteria == "Portería 30":
            print_tree(self.porteria30)
        if nombre_porteria == "Portería 25":
            print_tree(self.porteria25)

    def obtenerRuta(self,lugar_inicial, lugar_final):
        ruta = self.dicNodos[lugar_inicial].go_to(self.dicNodos[lugar_final])
        #print([node.node_name for node in ruta])
        return ruta


porteria27 = Arbol()
porteria27.asignarHijo('Portería 27', 'Tienda Universitaria')
porteria27.asignarHijo('Portería 27', 'Humanas 1')
porteria27.asignarHijo('Portería 27', 'Humanas 2')
porteria27.asignarHijo('Portería 27', 'Coliseo UIS')
porteria27.asignarHijo('Tienda Universitaria', 'Laboratorio de Livianos')
porteria27.asignarHijo('Tienda Universitaria', 'Luis A. Calvo')
porteria27.asignarHijo('Humanas 1', 'EDIC')
porteria27.asignarHijo('Humanas 2', 'Ingeniería Mecánica')
porteria27.asignarHijo('Luis A. Calvo', 'Estadio 1ero de marzo')
porteria27.asignarHijo('Luis A. Calvo', 'Administración 1')
porteria27.asignarHijo('Coliseo UIS', 'Residencias de Estudiantes')
porteria27.asignarHijo('Residencias de Estudiantes', 'Canchas Múltiples')
porteria27.asignarHijo('Administración 1', 'Administración 3')
porteria27.asignarHijo('Administración 3', 'Administración 2')
porteria27.asignarHijo('Administración 3', 'Auditorio José Antonio Galán')
porteria27.asignarHijo('Administración 2', 'Bienestar Campestre')
porteria27.asignarHijo('Administración 2', 'Bienestar Estudiantil')
porteria27.asignarHijo('Ingeniería Mecánica', 'Auditorio Luis Eduardo Lobo')
porteria27.asignarHijo('Auditorio Luis Eduardo Lobo', 'Biblioteca')
porteria27.asignarHijo('Biblioteca', 'Instituto de Lenguas')
porteria27.asignarHijo('Instituto de Lenguas', 'Casona La Perla')
porteria27.asignarHijo('Laboratorio de Livianos', 'Camilo Torres')
porteria27.asignarHijo('Camilo Torres', 'CENTIC')
porteria27.asignarHijo('Camilo Torres', 'Jorge Bautista Vesga')
porteria27.asignarHijo('Camilo Torres', 'Ingeniería Química')
porteria27.asignarHijo('CENTIC', 'Uisalud')
porteria27.asignarHijo('CENTIC', 'Federico Mamitza Bayer')
porteria27.asignarHijo('Jorge Bautista Vesga', 'Ingenierías Físico-Mecánicas')
porteria27.asignarHijo('Federico Mamitza Bayer', 'Ingeniería Industrial')
porteria27.asignarHijo('Federico Mamitza Bayer', 'Laboratorios de Alta Tensión')
porteria27.asignarHijo('Laboratorios de Alta Tensión', 'Diseño Industrial')
porteria27.asignarHijo('Federico Mamitza Bayer', 'Ingeniería E3T')


porteria25 = Arbol()
porteria25.asignarHijo('Portería 25', 'Jorge Bautista Vesga')
porteria25.asignarHijo('Portería 25', 'EDIC')
porteria25.asignarHijo('Jorge Bautista Vesga', 'Ingenierías Físico-Mecánicas')
porteria25.asignarHijo('Jorge Bautista Vesga', 'Ingeniería Química')
porteria25.asignarHijo('Ingeniería Química', 'CENTIC')
porteria25.asignarHijo('Ingeniería Química', 'Uisalud')
porteria25.asignarHijo('CENTIC', 'Biblioteca')
porteria25.asignarHijo('CENTIC', 'Auditorio Luis Eduardo Lobo')
porteria25.asignarHijo('Auditorio Luis Eduardo Lobo', 'Administración 1')
porteria25.asignarHijo('Auditorio Luis Eduardo Lobo', 'Luis A. Calvo')
porteria25.asignarHijo('Luis A. Calvo', 'Coliseo UIS')
porteria25.asignarHijo('Coliseo UIS', 'Residencias de Estudiantes')
porteria25.asignarHijo('Uisalud', 'Laboratorios de Alta Tensión')
porteria25.asignarHijo('Uisalud', 'Federico Mamitza Bayer')
porteria25.asignarHijo('Laboratorios de Alta Tensión', 'Diseño Industrial')
porteria25.asignarHijo('Federico Mamitza Bayer', 'Ingeniería E3T')
porteria25.asignarHijo('Federico Mamitza Bayer', 'Instituto de Lenguas')
porteria25.asignarHijo('Ingeniería E3T', 'Ingeniería Industrial')
porteria25.asignarHijo('Instituto de Lenguas', 'Casona La Perla')
porteria25.asignarHijo('Instituto de Lenguas', 'Auditorio José Antonio Galán')
porteria25.asignarHijo('Casona La Perla', 'Bienestar Estudiantil')
porteria25.asignarHijo('Casona La Perla', 'Administración 2')
porteria25.asignarHijo('Bienestar Estudiantil', 'Bienestar Campestre')
porteria25.asignarHijo('Bienestar Estudiantil', 'Canchas Múltiples')
porteria25.asignarHijo('Auditorio José Antonio Galán', 'Administración 3')
porteria25.asignarHijo('Administración 3', 'Estadio 1ero de marzo')
porteria25.asignarHijo('EDIC', 'Camilo Torres')
porteria25.asignarHijo('EDIC', 'Humanas 1')
porteria25.asignarHijo('Camilo Torres', 'Ingeniería Mecánica')
porteria25.asignarHijo('Camilo Torres', 'Humanas 2')
porteria25.asignarHijo('Humanas 1', 'Tienda Universitaria')

porteria30 = Arbol()
porteria30.asignarHijo('Portería 30', 'Coliseo UIS')
porteria30.asignarHijo('Portería 30', 'Luis A. Calvo')
porteria30.asignarHijo('Coliseo UIS', 'Residencias de Estudiantes')
porteria30.asignarHijo('Residencias de Estudiantes', 'Estadio 1ero de marzo')
porteria30.asignarHijo('Residencias de Estudiantes', 'Canchas Múltiples')
porteria30.asignarHijo('Estadio 1ero de marzo', 'Administración 1')
porteria30.asignarHijo('Estadio 1ero de marzo', 'Administración 2')
porteria30.asignarHijo('Estadio 1ero de marzo', 'Administración 3')
porteria30.asignarHijo('Estadio 1ero de marzo', 'Bienestar Estudiantil')
porteria30.asignarHijo('Estadio 1ero de marzo', 'Bienestar Campestre')
porteria30.asignarHijo('Administración 3', 'Auditorio José Antonio Galán')
porteria30.asignarHijo('Bienestar Estudiantil', 'Casona La Perla')
porteria30.asignarHijo('Luis A. Calvo', 'Tienda Universitaria')
porteria30.asignarHijo('Luis A. Calvo', 'Humanas 2')
porteria30.asignarHijo('Luis A. Calvo', 'Ingeniería Mecánica')
porteria30.asignarHijo('Tienda Universitaria', 'Humanas 1')
porteria30.asignarHijo('Humanas 1', 'Laboratorio de Livianos')
porteria30.asignarHijo('Humanas 1', 'EDIC')
porteria30.asignarHijo('Humanas 2', 'Auditorio Luis Eduardo Lobo')
porteria30.asignarHijo('Auditorio Luis Eduardo Lobo', 'Biblioteca')
porteria30.asignarHijo('Biblioteca', 'Instituto de Lenguas')
porteria30.asignarHijo('Biblioteca', 'Federico Mamitza Bayer')
porteria30.asignarHijo('Instituto de Lenguas', 'Ingeniería Industrial')
porteria30.asignarHijo('Instituto de Lenguas', 'Ingeniería E3T')
porteria30.asignarHijo('Federico Mamitza Bayer', 'Diseño Industrial')
porteria30.asignarHijo('Federico Mamitza Bayer', 'Laboratorios de Alta Tensión')
porteria30.asignarHijo('Ingeniería Mecánica', 'Camilo Torres')
porteria30.asignarHijo('Camilo Torres', 'CENTIC')
porteria30.asignarHijo('Camilo Torres', 'Ingeniería Química')
porteria30.asignarHijo('Ingeniería Química', 'Jorge Bautista Vesga')
porteria30.asignarHijo('Ingeniería Química', 'Ingenierías Físico-Mecánicas')
porteria30.asignarHijo('Ingeniería Química', 'Uisalud')


arboles = [porteria25,porteria27,porteria30]

# función Ruta mas corta
def encontrarRutaMasCorta(lugar_inicial, lugar_final):

    temporal = 10000
    ruta_mas_corta = None
    for arbol in arboles:
            ruta = arbol.obtenerRuta(lugar_inicial,lugar_final)
            distancia = len(ruta)
            if distancia<temporal:
                temporal = distancia
                ruta_mas_corta = ruta 
            
    return ruta_mas_corta


def menu():
    
    while True:
        print("\nMenú:")
        print("0. Mostrar arboles")
        print("1. Añadir lugar actual y destino")
        print("2. Ruta más corta")
        print("3. Todas las rutas")
        print("4. Mostrar descripciones")
        print("5. Salir")
        
        opcion = input("¿Qué función desea utilizar? ")

        if opcion == '1':
            porteria25.imprimirNodos()
            NumIni = int(input("¿En qué edificio se encuentra actualmente?(Escriba simplemente el numero) "))
            NumFin = int(input("¿A dónde quiere llegar?: "))
            lugar_inicial = porteria25.buscarNodoPorNumero(NumIni)
            lugar_final = porteria25.buscarNodoPorNumero(NumFin)
            print(f"Lugar inicial: {lugar_inicial}")
            print(f"Lugar final: {lugar_final}")
            print("Datos guardados exitosamente, regrese al menu principal para encontrar los caminos")
            
        elif opcion == '0':
            numeroPorteria = input('Ingrese el número de la porteria del arbol, 25, 27 o 30: ')
            if numeroPorteria == '25':
                porteria25.mostrarArbol("Portería 25")
            elif numeroPorteria == '27':
                porteria27.mostrarArbol("Portería 27")
            elif numeroPorteria == '30':
                porteria30.mostrarArbol("Portería 30")
            else:
                print('Ingrese un número válido')
            
        elif opcion == '2':
            if lugar_inicial != None and lugar_final != None:
                print(f"Ruta más corta de {lugar_inicial} a {lugar_final}")
                ruta_mas_corta = encontrarRutaMasCorta(lugar_inicial,lugar_final)
                print([node.node_name for node in ruta_mas_corta])
            else:
                print("Primero debes añadir el lugar inicial y final.")
                
        elif opcion == '3':
            if lugar_inicial != None and lugar_final != None:
                print(f"Todas las rutas de {lugar_inicial} a {lugar_final}")
                rutas = []
                contadorRutas = 1
                for arbol in arboles:
                    rutas.append(arbol.obtenerRuta(lugar_inicial,lugar_final)) 
                for ruta in rutas:
                    print('Ruta '+str(contadorRutas)+':')
                    print([node.node_name for node in ruta])
                    contadorRutas += 1
            else:
                print("Primero debes añadir el lugar inicial y final.")
        elif opcion == '4':
            ruta_mas_corta = encontrarRutaMasCorta(lugar_inicial,lugar_final)
            contadorRutas = 1
            for lugar in ruta_mas_corta:
                print("Ruta mas corta con descripción: ")
                print(str(contadorRutas)+'.')
                print('Nombre: '+lugar.node_name)
                print('Descripción: '+lugar.get_attr("descripcion"))
                print(' ')            
                contadorRutas += 1
        elif opcion == '5':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción correcta.")

        seguir = input("¿Deseas volver al menú principal? (Sí o No): ").lower()
        if seguir not in ['Sí', 'Si', 'si', 'sí']:
            print("Saliendo ")
            break


#Llamada a la función del menú
menu()
