
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

class colaClientes:
    def __init__(self):
        self.cabeza=None
        self.cola=None

    def vacia(self):
        return self.cabeza==None

    def agregar(self,dato):
        nuevoNodo=Nodo(dato)
        if(self.vacia()):
            self.cabeza=self.cola=nuevoNodo
            return

        nuevoNodo.siguiente=self.cabeza
        self.cabeza=nuevoNodo

    def verCola(self):
        actual=self.cabeza
        cadena=""
        while actual!=None:
            cadena=cadena+","+str(actual.dato["Nombre"])+" - carrito "+str(actual.dato["Carrito"])
            actual=actual.siguiente
        return cadena


    def borrarUltimo(self):
        if (self.vacia()):
            print("La cola esta vacia")
            return
        if (self.cabeza == self.cola):
            self.cabeza = self.cola = None

        else:
            actual = self.cabeza
            while actual.siguiente != self.cola:
                actual = actual.siguiente

            actual.siguiente = None
            self.cola = actual





'''caja=colaClientes()
lista=[{"id":31}]
caja.agregar(lista)
lista=[{"id":41}]
caja.agregar(lista)
print(caja.verCola())'''