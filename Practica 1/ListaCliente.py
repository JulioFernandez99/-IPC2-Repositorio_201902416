
from Nodo import *

class cliente:
    def __init__(self):
        self.cabeza=None
        self.cola=None

    def agregar(self,dato):
        nuevoNodo=Nodo(dato)
        if(self.cabeza==None):
            self.cabeza=self.cola=nuevoNodo
            return

        nuevoNodo.siguiente=self.cabeza
        self.cabeza=nuevoNodo

    def verLista(self):
        actual=self.cabeza
        cadena=""
        while actual!=None:
            cadena=cadena+f',  {actual.dato["Nombre"]} - Carrito {actual.dato["Carrito"]}'
            actual=actual.siguiente
        return cadena


    def buscar(self,dato):
        actual=self.cabeza
        res=None
        while actual!=None:
            if(dato==actual.dato["id"]):
                res=actual.dato
                break
            else:
                actual=actual.siguiente
        return res

    def buscarID(self):
        ids=[]
        actual=self.cabeza
        rs=False
        while actual!=None:
            ids.append(actual.dato["id"])
            actual=actual.siguiente
        return ids


    def borrar(self, dato):
        actual = self.cabeza
        anterior = None
        encontrado = False
        while not encontrado:
            if (actual != None):
                if (actual.dato == dato):
                    encontrado = True
                else:
                    anterior = actual
                    actual = actual.siguiente
            else:
                break
        if (actual != None):
            if (anterior == None):
                self.cabeza = actual.siguiente
            else:
                anterior.siguiente=actual.siguiente


