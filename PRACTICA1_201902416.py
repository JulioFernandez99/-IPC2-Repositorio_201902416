
from Carritos import *
from CajaRegistradora import *
from ListaCliente import *

listaCliente=cliente()

'''carrito.crearCarritos(6)
print(carrito.verCarritos())
print(carrito.retCabeza())



print(lista)
print(carrito.retCabeza())'''



primerRegistro=False
caja = colaClientes()
carritosCreados=False

def menu():
    global carritosCreados
    global primerRegistro
    op=None

    print("-----------------------")
    print("|      Kaizen Store     |")
    print("|                       |")
    print("| 1. ingreso de datos   |")
    print("| 2. Nuevo cliente      |")
    print("| 3. Ver Clientes       |")
    print("| 4. Caja registradora  |")
    print("| 5. Visualizar datos   |")
    print("| 6. Salir              |")
    print("-----------------------")
    op=input("->")


    if(op=="1"):
       if(carritosCreados==True):
           print(f"Actualmente tiene {carrito.numeroCarritos()} carritos disponibles")
           menu()

       if carritosCreados==False:
        numeroCarritos=int(input("Ingrese la cantidad de carritos: "))
        carrito.crearCarritos(numeroCarritos)
        carritosCreados=True
        menu()

    elif(op=="2"):
        if (carrito.cabeza!=None):
            id=int(input("Ingrese el id: "))
            listaIds=listaCliente.buscarID()
            #print(listaIds)

            if(id in listaIds):
                print("Ya existe un usuario con esta id")
                menu()
            else:
                nombre=input("Ingrese su nombre: ")
                dic={"id":id,"Nombre":nombre,"Carrito":carrito.retCabeza()}
                listaCliente.agregar(dic)
                carrito.correrCabeza()
                print(listaCliente.verLista())
                menu()

        else:
             print("No hay carritos disponibles")
             menu()


    elif(op=="3"):
        idBusqueda=int(input("Ingrese el id: "))
        busqueda=listaCliente.buscar(idBusqueda)
        if(busqueda==None):
            print("No un cliente con esta id")
        else:
            print(f'ID:{busqueda["id"]}')
            print(f'Nombre:{busqueda["Nombre"]}')
            print(f'Carrito:{busqueda["Carrito"]}')
            print("----Opciones----")
            print("| 1. Avanzar    |")
            print("| 2. Regresar   |")
            print("----------------")
            opc = input("->")

            if (opc == "1"):
                caja.agregar(busqueda)
                listaCliente.borrar(busqueda)
                menu()
            elif (opc == "2"):
                menu()

            else:
                print("Eligio una opcion quen no existe")
                menu()


        menu()


    elif (op == "4"):
        if(caja.cabeza!=None):
            print(caja.verCola())
            print("----Opciones----")
            print("| 1. Avanzar    |")
            print("| 2. Regresar   |")
            print("----------------")
            opc=input("->")

            if(opc=="1"):
                dato=caja.cola.dato #Entro al diccionario
                #print(dato["Carrito"])
                enviar=dato["Carrito"]
                caja.borrarUltimo()
                carrito.agregarInicio(enviar)

                menu()
            elif(opc=="2"):
                menu()

            else:
                print("Eligio una opcion quen no existe")
                menu()
        else:
            print("No hay clientes en la cola")
            menu()


    elif(op=="5"):
        cadena=""
        print(f"Pila carritos: {carrito.verCarritos()}")
        print(f"Cola: {caja.verCola()}")
        print(f"Usuarios: {listaCliente.verLista()}")
        menu()

    elif(op=="6"):
        print("Gracias por visitar nuestra tienda")
        exit()
    else:
        print("Elija una opcion valida")
        menu()


menu()


