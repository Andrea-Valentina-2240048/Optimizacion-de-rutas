from bigtree import Node
from bigtree import Node, print_tree
from bigtree import preorder_iter

class Arbol():
    def __init__(self):
        self.porteria = Node("Portería")
        self.coliseo = Node("Coliseo UIS", "Esta ubicado al sureste del campus, cuenta con una cancha polifuncional, camerinos, oficinas y gradería. Tiene 2 pisos y su fachada es en ladrillo rojizo, tiene unas lineas de colores y su techo tiene un estilo semicurvo.")
        self.luis_a_calvo = Node("Luisa A. Calvo", "Edificio de 20 metros de altura con una fachada curva en semióvalo y sin ventanas visibles. Está construido en ladrillo rojizo.")
        self.residencias = Node("Residencias de Estudiantes", "Edificio de varios pisos con fachada blanca y paneles verticales marrones. Las escaleras laterales conectan todos los niveles.")
        self.estadio = Node("Estadio 1ero de marzo", "Estadio con pista de atletismo de ocho carriles, alternando azul claro y oscuro que rodea el campo central.")
        self.canchas = Node("Canchas Múltiples", "Área deportiva con varias canchas al aire libre para diversas disciplinas.")
        self.admin1 = Node("Administración 1", "Edificio blanco con detalles grises, está compuesto por dos bloques de cuatro y dos pisos. 2 pasillos conectan los bloques en los primeros dos pisos. Tiene ventanas oscuras.")
        self.admin2 = Node("Administración 2", "Estructura de cinco pisos de color blanco, con bloques conectados por escaleras.")
        self.admin3 = Node("Administración 3", "Compuesto por dos bloques amarillos mostaza, conectados por un puente verde vibrante.")
        self.bienestar_estudiantil = Node("Bienestar Estudiantil", "El complejo está compuesto por tres bloques con diseños diversos. El primero tiene paneles metálicos verdes, el segundo es completamente acristalado y el tercero tiene una terraza.")
        self.bienestar_campestre = Node("Bienestar Campestre", "Espacio al aire libre con techos verdes y mesas.")
        self.auditorio_galan = Node("Auditorio José Antonio Galán", "Teatrino pequeño con graderías al aire libre en dos lados, de cinco y seis filas respectivamente. Las gradas son de ladrillo pequeño.")
        self.casona = Node("Casona La Perla", "Edificio de un solo piso de estilo colonial, con techo de tejas de barro y pisos rojizos. ")
        self.tienda_universitaria = Node("Tienda Universitaria", "Tiene un letrero con su nombre en la fachada, es de color blanco y azul celeste y esta ubicada enfrente del edificio de humanas 2.")
        self.humanas2 = Node("Humanas 2", "Edificio de 9 plantas, color amarillo mostaza, ubicado frente de la portería de la carrera 27.")
        self.mecanica = Node("Ingeniería Mecánica", "Edificio blanco de tres pisos, ubicado frente a biblioteca y al lado del auditorio Luis Eduardo Lobo, tiene tres entradas.")
        self.humanas1 = Node("Humanas 1", "Edificio de cinco pisos, con muro de ladrillo, se identifica por su planetario en la última planta.")
        self.lab_livianos = Node("Laboratorio de Livianos", "Construcción de cuatro pisos,de color blanco, ubicado después del edificio de humanas y unido por un pasillo al tercer piso del Camilo Torres.")
        self.edic = Node("EDIC", "El Edificio de Investigaciones de la Facultad de Ciencias, esta constituido por 8 niveles se distingue por su color crema, casi amarillo, y por su fachada con pequeñas ventanas blancas y cafés. Está ubicado junto al Laboratorio de Livianos.")
        self.auditorio_lobo = Node("Auditorio Luis Eduardo Lobo", "Este auditorio, de estructura semicircular, se encuentra junto al edificio Camilo Torres. Su techo es de color gris y el resto de la fachada es blanca.")
        self.biblioteca = Node("Biblioteca", "Edificio de cuatro plantas con una estructura de lápices verticales y con vista al interior.")
        self.instituto_lenguas = Node("Instituto de Lenguas", "Este edificio actualmente se encuentra en construcción.")
        self.federico = Node("Federico Mamitza Bayer", "Edificio de muro de ladrillo, 3 plantas y reja amplia para el ingreso.")
        self.ingenieria_industrial = Node("Ingeniería Industrial", "Este edificio cuenta con 5 pisos, tiene en su entrada un letrero con su nombre “Ingeniería industrial”. Es de color blanco y gris, cuenta con una rampa a la derecha y escaleras al frente para el ingreso.")
        self.ingenieria_e3t = Node("Ingeniería E3T", "En este edificio se encuentran la Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones y cuenta con 4 pisos. Es de color blanco y gris, con puertas de vidrio, y se identifica por su letrero de “E3T” en la parte superior izquierda de su entrada. Está ubicado junto al edificio de Ingeniería Industrial.")
        self.diseno_industrial = Node("Diseño Industrial", "Construcción de un solo piso, con tejado visible.")
        self.alta_tension = Node("Laboratorios de Alta Tensión", "Este edificio es de color blanco y tiene dos pisos.")
        self.camilo_torres = Node("Camilo Torres", "Este edificio de 5 pisos está construido en ladrillo de color rojizo, se destaca por tener en su fachada la imagen del sacerdote y activista colombiano Camilo Torres.")
        self.centic = Node("CENTIC", "Edificio de cómputo de la universidad, pintado de blanco y 4 pisos, con cristales en el exterior en la parte frontal y trasera.")
        self.ingenieria_quimica = Node("Ingeniería Química", "Este edificio cuenta con dos niveles, se reconoce por su nombre en letras rojas en la parte superior y por la escultura llamada Torre de Destilación ubicada en su entrada, que representa una torre utilizada en los laboratorios de procesos de ingeniería química. Su fachada es de color blanco.")
        self.jorge_bautista_vesga = Node("Jorge Bautista Vesga", "Edificio de escuela de Ingeniería Metalúrgica y Ciencia de Materiales, 3 pisos, con muro de ladrillo y al final de la calle.")
        self.fisicomecanica = Node("Ingenierías Físico-Mecánicas", "Esta facultad cuenta con 4 niveles, está construida en ladrillo de color rojizo, en su entrada se puede apreciar un letrero con su nombre y se identifica principalmente por la figura denominada Corte de construcción al Viento construida en hierro y PVC.")
        self.uisalud = Node("Uisalud", "Este edificio cuenta con 3 pisos, tiene su nombre en grande en la fachada, es de colores gris y blanco, y cuenta con varios ventanales. Está ubicado detrás del CENTIC y junto al Aula Máxima de Ciencias.")
        self.dicNodos = {"Portería": self.porteria, "Uisalud": self.uisalud,"Ingenierías Físico-Mecánicas":self.fisicomecanica,"Jorge Bautista Vesga": self.jorge_bautista_vesga,
            "Coliseo UIS": self.coliseo, "Luisa A. Calvo": self.luis_a_calvo, "Residencias de Estudiantes": self.residencias, "Estadio 1ero de marzo": self.estadio, 
            "Canchas Múltiples": self.canchas, "Administración 1": self.admin1, "Administración 2": self.admin2, "Administración 3": self.admin3, 
            "Bienestar Estudiantil": self.bienestar_estudiantil, "Bienestar Campestre": self.bienestar_campestre, "Auditorio José Antonio Galán": self.auditorio_galan,
            "Casona La Perla": self.casona, "Tienda Universitaria": self.tienda_universitaria, "Humanas 2": self.humanas2, "Ingeniería Mecánica": self.mecanica, 
            "Humanas 1": self.humanas1, "Laboratorio de Livianos": self.lab_livianos, "EDIC": self.edic, "Auditorio Luis Eduardo Lobo": self.auditorio_lobo,
            "Biblioteca": self.biblioteca, "Instituto de Lenguas": self.instituto_lenguas, "Federico Mamitza Bayer": self.federico, "Ingeniería Industrial": self.ingenieria_industrial,
            "Ingeniería E3T": self.ingenieria_e3t, "Diseño Industrial": self.diseno_industrial, "Laboratorios de Alta Tensión": self.alta_tension,
            "Camilo Torres": self.camilo_torres, "CENTIC": self.centic, "Ingeniería Química": self.ingenieria_quimica
        }
        
    def asignarHijo(self,padre,hijo):
        self.dicNodos[padre].append(self.dicNodos[hijo])

    def mostrarArbol(self):
        print_tree(self.porteria)
# Mostrar árbol
#print_tree(root)
#print_tree(porteria30)
#ruta = porteria30.go_to(auditorio_lobo)
##print(ruta)
#print([node.node_name for node in ruta])

porteria27 = Arbol()
porteria27.asignarHijo('Portería', 'Tienda Universitaria')
porteria27.asignarHijo('Portería', 'Humanas 1')
porteria27.asignarHijo('Portería', 'Humanas 2')
porteria27.asignarHijo('Portería', 'Coliseo UIS')
porteria27.asignarHijo('Tienda Universitaria', 'Laboratorio de Livianos')
porteria27.asignarHijo('Tienda Universitaria', 'Luisa A. Calvo')
porteria27.asignarHijo('Humanas 1', 'EDIC')
porteria27.asignarHijo('Humanas 2', 'Ingeniería Mecánica')
porteria27.asignarHijo('Luisa A. Calvo', 'Estadio 1ero de marzo')
porteria27.asignarHijo('Luisa A. Calvo', 'Administración 1')
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
porteria27.mostrarArbol()


porteria25 = Arbol()

porteria30 = Arbol()
porteria30.asignarHijo('Portería', 'Coliseo UIS')
porteria30.asignarHijo('Portería', 'Luisa A. Calvo')
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
porteria30.asignarHijo('Luisa A. Calvo', 'Tienda Universitaria')
porteria30.asignarHijo('Luisa A. Calvo', 'Humanas 2')
porteria30.asignarHijo('Luisa A. Calvo', 'Ingeniería Mecánica')
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
porteria30.mostrarArbol()

arboles = [porteria25,porteria27,porteria30]
