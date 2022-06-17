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
            contador += 1
            title = cd.findall("title")[0].text
            artist = cd.findall("artist")[0].text
            country = cd.findall("country")[0].text
            company = cd.findall("company")[0].text
            price = cd.findall("price")[0].text
            year = cd.findall("year")[0].text
            if (title[0] == '"'):
                nuevoTitle = title.strip('"')
                comando += f'nodeTitulo{contador}[label=" \\"{format(nuevoTitle)}\\""]\n'
            else:
                comando += f'nodeTitulo{contador}[label="{cd.findall("title")[0].text}"]\n'
            if (artist[0] == '"'):
                nuevoartist = artist.strip('"')
                comando += f'nodeArtista{contador}[label=" \\"{format(nuevoartist)}\\""]\n'
            else:
                comando += f'nodeArtista{contador}[label="{cd.findall("artist")[0].text}"]\n'
            if (country[0] == '"'):
                nuevocountry = country.strip('"')
                comando += f'nodeCountry{contador}[label=" \\"{format(nuevocountry)}\\""]\n'
            else:
                comando += f'nodeCountry{contador}[label="{cd.findall("country")[0].text}"]\n'
            if (company[0] == '"'):
                nuevocompany = company.strip('"')
                comando += f'nodeCompany{contador}[label=" \\"{format(nuevocompany)}\\""]\n'
            else:
                comando += f'nodeCompany{contador}[label="{cd.findall("company")[0].text}"]\n'
            if (price[0] == '"'):
                nuevoprice = price.strip('"')
                comando += f'nodePrice{contador}[label=" \\"{format(nuevoprice)}\\""]\n'
            else:
                comando += f'nodePrice{contador}[label="{cd.findall("price")[0].text}"]\n'
            if (year[0] == '"'):
                nuevoyear = year.strip('"')
                comando += f'nodeYear{contador}[label=" \\"{format(nuevoyear)}\\""]\n'
            else:
                comando += f'nodeYear{contador}[label="{cd.findall("year")[0].text}"]\n'

            # Apuntando nodos
            comando += f'"catalogo"->"cd{contador}"\n'
            comando += f'cd{contador}->nodeTitulo{contador}\n'
            comando += f'nodeTitulo{contador}->nodeArtista{contador}\n'
            comando += f'nodeTitulo{contador}->nodeCountry{contador}\n'
            comando += f'nodeTitulo{contador}->nodeCompany{contador}\n'
            comando += f'nodeTitulo{contador}->nodePrice{contador}\n'
            comando += f'nodeTitulo{contador}->nodeYear{contador}\n'
        comando += "}"

        #print(comando)
        manf.write(comando)
        manf.close()
        comand = "dot -Tjpg Comandos/ComandosDiscos.dot -o Reportes/ReporteDiscos.jpg"
        check_output(comand, shell=True)


opcDisc=OpcionesDiscos()





