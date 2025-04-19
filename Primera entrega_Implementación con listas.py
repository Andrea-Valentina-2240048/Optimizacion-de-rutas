###########################
# Integrantes:
# Andrea Valentina Delgado Ruiz - 2240048
# Vanessa Martínez Angarita - 2241917
# Nelson Andres Urrea Calvo - 2221115
###########################


# Clase Nodo
class Nodo:
    def __init__(self, nombre):
        self.siguiente = None
        self.anterior = None
        self.nombre = nombre  # Nombre del lugar en el mapa

# Clase listaDoblementeEnlazada
class listaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0

    # Verificar si la lista está vacía
    def vacio(self):
        if self.cabeza is None:
            print("Está vacía")
        else:
            print("Lista no vacía")

    # Agregar un elemento (Solo se agregaran por el inicio de la lista)
    def agregarLugar(self, nombre):
        nuevo_nodo = Nodo(nombre)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = self.cabeza
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

        self.contador += 1

    # Contar la cantidad de elementos existentes en la lista
    def contarElementos(self):
        return self.contador

    # Buscar la posición de un elemento en la lista
    def buscarPosicion(self, nombre):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.nombre is nombre:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return 0
    
    def BuscarLugar(self, nombre):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.nombre is nombre:
                #print(nombre+' Si exite, en la posicion: '+str(posicion))
                return True
            actual = actual.siguiente
            posicion += 1
        return False

    # Imprimir rutas
    def imprimirRuta(self):
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía")
            return

        while actual:
            print(actual.nombre, end=" ⇄ ")
            actual = actual.siguiente

        print("None")

    # Imprimir fración de la ruta desde inicio hasta destino
    def imprimirRutaParcial(self, inicio, destino):

        if self.buscarPosicion(inicio)<self.buscarPosicion(destino):
            actual = self.cabeza
            inicioEncontrado = False
            if actual is None:
                print("La lista está vacía")
                return

            while actual:
                if actual.nombre is inicio:
                    print(actual.nombre, end=" ⇄ ")
                    inicioEncontrado = True

                elif inicioEncontrado:
                    print(actual.nombre, end=" ⇄ ")
                    if actual.nombre is destino:
                        break

                actual = actual.siguiente

            print("None")   

        elif self.buscarPosicion(inicio)>self.buscarPosicion(destino): 

            actual = self.cola
            inicioEncontrado = False
            if actual is None:
                print("La lista está vacía")
                return

            while actual:
                if actual.nombre is inicio:
                    print(actual.nombre, end=" ⇄ ")
                    inicioEncontrado = True

                elif inicioEncontrado:
                    print(actual.nombre, end=" ⇄ ")
                    if actual.nombre is destino:
                        break

                actual = actual.anterior
            print("None")

# función Mostrar rutas
def imprimirRutas(rutas):
    contador = 1
    for ruta in rutas:
        print('ruta'+str(contador)+': ')
        ruta.imprimirRuta()
        print('\n')
        contador += 1

# función Ruta mas corta
def encontrarRutaMasCorta(lugar_inicial, lugar_final):
    inicio = lugar_inicial
    destino = lugar_final
    temporal = 10000
    ruta_mas_corta = None
    for ruta in rutas:
        if(ruta.BuscarLugar(inicio)and ruta.BuscarLugar(destino)):
            distancia = abs(ruta.buscarPosicion(inicio)-ruta.buscarPosicion(destino))
            if distancia<temporal:
                temporal = distancia
                ruta_mas_corta = ruta 
        else:
            inicio = None
            destino = None
            print('Digite los lugares correctamente')
    ruta_mas_corta.imprimirRutaParcial(inicio,destino)


# Crear las rutas

ruta1 = listaDoblementeEnlazada()  # Morado
ruta1.agregarLugar('Porteria')
ruta1.agregarLugar('Auditorio Luis A. Calvo')
ruta1.agregarLugar('Residencias')
ruta1.agregarLugar('Canchas multiples')
ruta1.agregarLugar('Bienestar estudiantil')
ruta1.agregarLugar('E3T')
ruta1.agregarLugar('Facultad ing fisicomecanicas')
ruta1.agregarLugar('EDIC')
ruta1.agregarLugar('Camilo Torres')
ruta1.agregarLugar('Administracion3')
ruta1.agregarLugar('Instituto de lenguas')
ruta1.agregarLugar('UISALUD')


ruta2 = listaDoblementeEnlazada()  # Azul 
ruta2.agregarLugar('Porteria')
ruta2.agregarLugar('EDIC')
ruta2.agregarLugar('Facultad ing fisicomecanicas')
ruta2.agregarLugar('E3T')
ruta2.agregarLugar('UISALUD')
ruta2.agregarLugar('Camilo Torres')
ruta2.agregarLugar('Auditorio Luis A. Calvo')
ruta2.agregarLugar('Administracion3')
ruta2.agregarLugar('Instituto de lenguas')
ruta2.agregarLugar('Bienestar estudiantil')
ruta2.agregarLugar('Canchas multiples')
ruta2.agregarLugar('Residencias')

ruta3 = listaDoblementeEnlazada()  # Verde
ruta3.agregarLugar('Canchas multiples')
ruta3.agregarLugar('Bienestar estudiantil')
ruta3.agregarLugar('E3T')
ruta3.agregarLugar('Facultad ing fisicomecanicas')
ruta3.agregarLugar('UISALUD')
ruta3.agregarLugar('Instituto de lenguas')
ruta3.agregarLugar('Administracion3')
ruta3.agregarLugar('Camilo Torres')
ruta3.agregarLugar('EDIC')
ruta3.agregarLugar('Auditorio Luis A. Calvo')
ruta3.agregarLugar('Porteria')
ruta3.agregarLugar('Residencias')


ruta4 = listaDoblementeEnlazada()  # Naranja
ruta4.agregarLugar('Canchas multiples')
ruta4.agregarLugar('Residencias')
ruta4.agregarLugar('Auditorio Luis A. Calvo')
ruta4.agregarLugar('Administracion3')
ruta4.agregarLugar('Bienestar estudiantil')
ruta4.agregarLugar('Instituto de lenguas')
ruta4.agregarLugar('E3T')
ruta4.agregarLugar('UISALUD')
ruta4.agregarLugar('Camilo Torres')
ruta4.agregarLugar('Facultad ing fisicomecanicas')
ruta4.agregarLugar('EDIC')
ruta4.agregarLugar('Porteria')



rutas = [ruta1,ruta2,ruta3,ruta4]

imprimirRutas(rutas)

inicio = 'E3T'
destino = 'Porteria'

encontrarRutaMasCorta(inicio,destino)
encontrarRutaMasCorta(destino,inicio)