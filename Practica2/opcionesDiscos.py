from subprocess import check_output
import xml.etree.ElementTree as ET

class OpcionesDiscos:
    raizEmpleados = None
    doc=None

    def cargarDatosDiscos(self):
        global raizDiscos,doc
        doc = ET.parse("discos.xml")
        raizDiscos = doc.getroot()
        #print(raizDiscos)

    def verDisco(self,title):
        global raizDiscos

        for cd in raizDiscos:
            if(cd.findall("title")[0].text==title):
                print(f'Title: {cd.findall("title")[0].text}')
                print(f'Artist: {cd.findall("artist")[0].text}')
                print(f'Country: {cd.findall("country")[0].text}')
                print(f'Company: {cd.findall("company")[0].text}')
                print(f'Price: {cd.findall("price")[0].text}')
                print(f'Year: {cd.findall("year")[0].text} \n')
                print("")
                return
        print("No existe ningun disco con este titulo\n")

    def modificarDisco(self,titleBusqueda):
        global raizDiscos
        for cd in raizDiscos:
            if(cd.findall("title")[0].text==titleBusqueda):
                ntitle=input("Ingrese nuevo titulo: ")
                nartist=input("Ingrese nuevo artist: ")
                ncountry=input("Ingrese nuevo country: ")
                ncompany = input("Ingrese nueva company: ")
                nprice = input("Ingrese nuevo price: ")
                nyear = input("Ingrese nuevo year: ")

                cd.findall("title")[0].text=ntitle
                cd.findall("artist")[0].text = nartist
                cd.findall("country")[0].text = ncountry
                cd.findall("company")[0].text = ncompany
                cd.findall("price")[0].text = nprice
                cd.findall("year")[0].text = nyear
                print("Disco modificado\n")
                return
        print("No existe ningun disco con este titulo\n")

    def eliminarDisco(self,title):
        global raizDiscos
        for cd in raizDiscos:
            if(cd.findall("title")[0].text==title):
                raizDiscos.remove(cd)
                print("Disco eliminado\n")
                return
        print("No existe ningun disco con este titulo\n")

    def verTodo(self):
        global raizDiscos
        print("")
        for cd in raizDiscos:
            '''title=cd.findall("title")[0].text
            nuevoTitle=title.strip('"')'''
            print(f'Title: {cd.findall("title")[0].text}')
            print(f'Artist: {cd.findall("artist")[0].text}')
            print(f'Country: {cd.findall("country")[0].text}')
            print(f'Company: {cd.findall("company")[0].text}')
            print(f'Price: {cd.findall("price")[0].text}')
            print(f'Year: {cd.findall("year")[0].text} \n')

    def cerrarDocDiscos(self):
        global raizDiscos,doc
        doc.write("discos.xml",xml_declaration=True,encoding="utf-8")

    def generarReporte(self):
        contador = 0
        manf = open('Comandos/ComandosDiscos.dot', 'w')
        comando = 'digraph G {\ncharset="latin1"\nnode [shape=square,style="rounded"];\nrankdir="LR";\n'
        for cd in raizDiscos:
            title = cd.findall("title")[0].text
            nuevoTitle = title.strip('"')

            contador += 1
            comando += f'"catalogo"->"cd{contador}"\n'
            comando += f'"cd{contador}"->"{format(nuevoTitle)}"\n'
            comando += f'"{format(nuevoTitle)}"->"Artist:{cd.findall("artist")[0].text}"\n'
            comando += f'"{format(nuevoTitle)}"->"Country:{cd.findall("country")[0].text}"\n'
            comando += f'"{format(nuevoTitle)}"->"Company:{cd.findall("company")[0].text}"\n'
            comando += f'"{format(nuevoTitle)}"->"Price:{cd.findall("price")[0].text}"\n'
            comando += f'"{format(nuevoTitle)}"->"Year:{cd.findall("year")[0].text}"\n'
        comando += "}"

        #print(comando)
        manf.write(comando)
        manf.close()
        comand = "dot -Tjpg Comandos/ComandosDiscos.dot -o Reportes/ReporteDiscos.jpg"
        check_output(comand, shell=True)


opcDisc=OpcionesDiscos()





