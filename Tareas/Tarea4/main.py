import xml.etree.ElementTree as ET

discos = None


class Discos:
    def __init__(self):
        self.doc = ET.parse("discos.xml")
        self.raizDiscos = self.doc.getroot()

    def verDiscos(self):
        rs = False
        year = input("Ingrese el año : ")
        for cd in self.raizDiscos:
            if cd.findall("year")[0].text == year:
                print(f'Title: {cd.findall("title")[0].text}')
                print(f'Artist: {cd.findall("artist")[0].text}')
                print(f'Country: {cd.findall("country")[0].text}')
                print(f'Company: {cd.findall("company")[0].text}')
                print(f'Price: {cd.findall("price")[0].text}')
                print(f'Year: {cd.findall("year")[0].text} \n')
                rs = True
        if not rs:
            print("No se encontro ningun disco con esa fecha\n")


def menu():
    global discos
    print(" -------------Menu--------------")
    print("| 1.Cargar datos                |")
    print("| 2.Buscar disco                |")
    print("| 3.Salir                       |")
    print(" -------------------------------")
    op = input("->")

    if op == "1":
        if discos is None:
            discos = Discos()
            print("Datos cargados\n")
            menu()
        else:
            print("Los datos ya estan cargados\n")
            menu()

    elif op == "2":
        if discos is None:
            print("Primero cargue los datos\n")
            menu()
        else:
            discos.verDiscos()
            menu()
    elif op == "3":
        print(" -----------------------------------------")
        print("|     Gracias por utilizar mi programa    |")
        print(" -----------------------------------------")
        exit()
    else:
        print("Ingrese una opcion valida\n")
        menu()


menu()
