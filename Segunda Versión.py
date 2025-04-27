from bigtree import Node
from bigtree import Node, print_tree
from bigtree import preorder_iter

class Arbol():
    def __init__(self):
        self.porteria = Node("Portería")
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
        self.mecanica = Node("Ingeniería Mecánica")
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
        self.fisicomecanica = Node("Ingenierías Físico-Mecánicas")
        self.uisalud = Node("Uisalud")
        self.dicNodos = {"Portería": self.porteria, "Uisalud": self.uisalud,"Ingenierías Físico-Mecánicas":self.fisicomecanica,"José Bautista Vesga": self.jose_bautista_vesga,
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
porteria27.asignarHijo('Camilo Torres', 'José Bautista Vesga')
porteria27.asignarHijo('Camilo Torres', 'Ingeniería Química')
porteria27.asignarHijo('CENTIC', 'Uisalud')
porteria27.asignarHijo('CENTIC', 'Federico Mamitza Bayer')
porteria27.asignarHijo('José Bautista Vesga', 'Ingenierías Físico-Mecánicas')
porteria27.asignarHijo('Federico Mamitza Bayer', 'Ingeniería Industrial')
porteria27.asignarHijo('Federico Mamitza Bayer', 'Laboratorios de Alta Tensión')
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
porteria30.asignarHijo('Ingeniería Química', 'José Bautista Vesga')
porteria30.asignarHijo('Ingeniería Química', 'Ingenierías Físico-Mecánicas')
porteria30.asignarHijo('Ingeniería Química', 'Uisalud')
porteria30.mostrarArbol()

arboles = [porteria25,porteria27,porteria30]
