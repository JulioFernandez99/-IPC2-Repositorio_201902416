import os

from opcionesEmpleados import *
from opcionesDiscos import *

carg=False
rs=False

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def menu():
    global carg,rs
    print(" --------------Menu--------------")
    print("| 1.Cargar datos                 |")
    print("| 2.Gestion de empleados         |")
    print("| 3.Gestión de discos            |")
    print("| 4.Reportes                     |")
    print("| 5.Salir                        |")
    print(" --------------------------------")
    op=input("->")

    if(op=="1"):
        if(carg==False):
            opcEmp.CargarDatosEmpleados()
            opcDisc.cargarDatosDiscos()
            print("Carga de datos exitosa\n")
            carg=True
            rs=True
            menu()
        else:
            print("Los datos ya estan cargados\n")
            menu()

    #Opciones de empleados
    elif(op=="2"):
        clearConsole()
        print(" --------Opciones de empleados----------")
        print("| a.Ver empleado                        |")
        print("| b.Modificacion                        |")
        print("| c.Eliminacion                         |")
        print("| d.Ver todo                            |")
        print("| e.Generar archivo                     |")
        print(" ---------------------------------------")
        p=input("->")

        if(p.lower()=="a"):
            if(rs!=False):
                clearConsole()
                id = input("Ingrese el id del cliente: ")
                opcEmp.verEmpleado(id)
                menu()
            else:
                clearConsole()
                print("Primero cargue los datos\n")
                menu()


        elif(p.lower()=="b"):
            if (rs != False):
                clearConsole()
                id = input("Ingrese el id del cliente: ")
                opcEmp.modificarEmpleado(id)
                menu()
            else:
                clearConsole()
                print("Primero cargue los datos\n")
                menu()

        elif (p.lower() == "c"):
            if (rs != False):
                clearConsole()
                id=input("Ingrese la id del empleado: ")
                opcEmp.eliminarEmpleado(id)
                menu()
            else:
                clearConsole()
                print("Primero cargue los datos\n")
                menu()


        elif (p.lower() == "d"):
            if (rs != False):
                clearConsole()
                opcEmp.verTodosEmpleados()
                print("")
                menu()
            else:
                clearConsole()
                print("Primero cargue los datos\n")
                menu()

        elif (p.lower() == "e"):
            if (rs != False):
                clearConsole()
                opcEmp.cerrarDocEmpleados()
                print("Archivo generado\n")
                #carg=False
                menu()

        else:
            clearConsole()
            print("Ingrese una opcion valida\n")
            menu()

    #Ociones de discos
    elif(op=="3"):
        clearConsole()
        print(" --------Opciones de discos----------")
        print("| a.Ver disco                        |")
        print("| b.Modificar disco                  |")
        print("| c.Eliminar disco                   |")
        print("| d.Ver Ttodo                        |")
        print("| e.Generar Archivo                  |")
        print(" ------------------------------------")
        p=input("->")

        if(p=="a"):
            if(rs!=False):
                clearConsole()
                titulo=input("Ingrese el titulo del disco: ")
                opcDisc.verDisco(titulo)
                menu()
            else:
                clearConsole()
                print("Primero cargue los datos\n")
                menu()

        if(p=="b"):
            if (rs != False):
                clearConsole()
                titulo=input("Ingrese el titulo del disco: ")
                opcDisc.modificarDisco(titulo)
                menu()
            else:
                clearConsole()
                print("Primero cargue los datos\n")
                menu()

        if (p == "c"):
            if (rs != False):
                clearConsole()
                titulo = input("Ingrese el titulo del disco: ")
                opcDisc.eliminarDisco(titulo)
                menu()
            else:
                clearConsole()
                print("Primero cargue los datos\n")
                menu()



        elif (p == "d"):
            if (rs != False):
                clearConsole()
                opcDisc.verTodo()
                menu()
            else:
                clearConsole()
                print("Primero cargue los datos\n")
                menu()


        elif(p=="e"):
            if (rs != False):
                clearConsole()
                opcDisc.cerrarDocDiscos()
                print("Archivo generado\n")
                menu()
            else:
                clearConsole()
                print("Primero cargue los datos\n")
                menu()

        else:
            clearConsole()
            print("Elige una opcion valida \n")
            menu()

    elif(op=="4"):
        clearConsole()
        print("a. Reporte de empleados")
        print("b. Reporte de discos")
        opc=input("->")
        if(opc=="a"):
            if(carg):
                opcEmp.generarReporte()
                print("Reporte generado con exito\n")
                menu()
            else:
                print("Primero carge los datos\n")
                menu()
        elif (opc == "b"):
            if (carg):
                opcDisc.generarReporte()
                print("Reporte generado con exito\n")
                menu()
            else:
                print("Primero carge los datos\n")
                menu()

        else:
            print("Ingreso una opcion invalida\n")


    elif(op=="5"):
        print("Gracias por utilizar mi programa")
        exit()
    else:
        print("Ingrese una opcion valida\n")
        menu()

menu()


