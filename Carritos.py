from Nodo import *

class Carritos:

    def __init__(self):
        self.cabeza=None
        self.cola=None

    def vacia(self):
        return self.cabeza==None

    def crearCarritos(self,NumeroCarritos):
        c = 1
        while c<=NumeroCarritos:
            nuevoNodo = Nodo(c)
            if (self.vacia()):
                self.cabeza = self.cola = nuevoNodo
                c =c+1
            else:
                nuevoNodo.siguiente = self.cabeza
                self.cabeza = nuevoNodo
                c = c + 1


    def verCarritos(self):
        cadena=""
        actual=self.cabeza
        while actual!=None:
            cadena=cadena+"->"+"["+str(actual.dato)+"]"
            actual=actual.siguiente
        return cadena

    def numeroCarritos(self):
        contador=0
        actual=self.cabeza
        while actual!=None:
            contador=contador+1
            actual=actual.siguiente
        return contador

    def retCabeza(self):
        val=self.cabeza.dato
        return str(val)

    def correrCabeza(self):
        self.cabeza=self.cabeza.siguiente

    def agregarFin(self,dato):
        nuevoNodo=Nodo(dato)
        if(self.cabeza==None):
            self.cabeza=self.cola=nuevoNodo
            return

        self.cola.siguiente=nuevoNodo
        self.cola=nuevoNodo


    def agregarInicio(self,dato):
        nuevoNodo=Nodo(dato)
        nuevoNodo.siguiente=self.cabeza
        self.cabeza=nuevoNodo



carrito=Carritos()