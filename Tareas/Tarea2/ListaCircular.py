#Nodo
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

#Lista
class Lista:
    def __init__(self):
        self.cabeza=None
        self.cola=None

    def agregar(self,dato):
        nuevoNodo=Nodo(dato)
        if(self.cabeza==None):
            self.cabeza=self.cola=nuevoNodo
            return

        nuevoNodo.siguiente=self.cabeza
        self.cabeza.anterior=nuevoNodo
        self.cabeza=nuevoNodo

        #Enlace de la cola a la cabeza
        self.cola.siguiente=self.cabeza

        #Enlace de la cabeza a la cola
        self.cabeza.anterior=self.cola

    def verLista(self):
        print("-------Lista completa-------")
        actual = self.cabeza
        while actual!=None:
            print(actual.dato)
            actual=actual.siguiente
            if (actual == self.cabeza):
                break

    def buscar(self, dato):
        actual = self.cabeza
        while actual != None:
           if (actual.dato==dato):
               return actual
           else:
               actual=actual.siguiente
               if(actual==self.cabeza):
                   return False



lista=Lista()
lista.agregar(2)
lista.agregar(10)
lista.agregar(33)
lista.agregar(51)
lista.agregar(89)
lista.verLista()

numero=int(input("Seleccione un numero: "))

dato=lista.buscar(numero)
if(dato==False):
    print("No existe este dato")
else:
    print(f"Anterior:{dato.anterior.dato} | Actual:{dato.dato} "
    f"| Siguiente:{dato.siguiente.dato}")


