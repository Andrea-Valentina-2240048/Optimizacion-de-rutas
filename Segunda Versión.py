from bigtree import Node
from bigtree import Node, print_tree
from bigtree import preorder_iter

class Arbol():
    def __init__(self):
        self.porteria = Node("porteria")
        self.coliseo = Node("Coliseo UIS")
        self.luis_a_calvo = Node("Luisa A. Calvo")
        self.residencias = Node("Residencias de Estudiantes")
        self.estadio = Node("Estadio 1ero de marzo")
        self.canchas = Node("Canchas Múltiples")
        self.admin1 = Node("Administración 1")
        self.admin2 = Node("Administración 2")
        self.admin3 = Node("Administración 3")
        self.bienestar_estudiantil = Node("Bienestar Estudiantil")
        self.bienestar_campestre = Node("Bienestar Campestre")
        self.auditorio_galan = Node("Auditorio José Antonio Galán")
        self.casona = Node("Casona La Perla")
        self.tienda_universitaria = Node("Tienda Universitaria")
        self.humanas2 = Node("Humanas 2")
        self.mecanica = Node("Ingeniería mecánica")
        self.humanas1 = Node("Humanas 1")
        self.lab_livianos = Node("Laboratorio de Livianos")
        self.edic = Node("EDIC")
        self.auditorio_lobo = Node("Auditorio Luis Eduardo Lobo")
        self.biblioteca = Node("Biblioteca")
        self.instituto_lenguas = Node("Instituto de Lenguas")
        self.federico = Node("Federico Mamitza Bayer")
        self.ingenieria_industrial = Node("Ingeniería Industrial")
        self.ingenieria_e3t = Node("Ingeniería E3T")
        self.diseno_industrial = Node("Diseño Industrial")
        self.alta_tension = Node("Laboratorios de Alta Tensión")
        self.camilo_torres = Node("Camilo Torres")
        self.centic = Node("CENTIC")
        self.ingenieria_quimica = Node("Ingeniería Química")
        self.jose_bautista_vesga = Node("José Bautista Vesga")
        self.fisicomecanica = Node("Ingeniería Físico-Mecánicas")
        self.uisalud = Node("Uisalud")
        self.dicNodos = {"Uisalud": self.uisalud,"Ingeniería Físico-Mecánicas":self.fisicomecanica,"José Bautista Vesga": self.jose_bautista_vesga}
        
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
porteria27.asignarHijo('Uisalu','Ingeniería Físico-Mecánicas')
porteria27.mostrarArbol()


porteria25 = Arbol()

porteria30 = Arbol()


arboles = [porteria25,porteria27,porteria30]