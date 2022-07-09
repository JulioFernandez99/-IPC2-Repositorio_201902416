from subprocess import check_output
from flask import Flask, jsonify, request
import xml.etree.ElementTree as ET

app=Flask(__name__)
#-----------------------------------Opciones de discos----------------------------------
#Aca estan todas las peticiones (GET y POST)

#Get /discos/
#Devuelve todos los discos en formato Json
@app.route('/discos/')
def discos():
    doc = ET.parse("archivos/discos.xml")
    raizDiscos = doc.getroot()
    #print(raizDiscos)
    lista=[]
    
    for cd in raizDiscos:
            diccionario={
                "title":cd.findall("title")[0].text,
                "artist":cd.findall("artist")[0].text,
                "country":cd.findall("country")[0].text,
                "company":cd.findall("company")[0].text,
                "price":cd.findall("price")[0].text,
                "year":cd.findall("year")[0].text
                }
            lista.append(diccionario)
    
    return jsonify({"discos":lista})


#Post /discoTitulo/
#Recibe un json con el titulo del disco y devule su informacion
@app.route('/discoTitulo/',methods=["POST"])
def discoTitulo():
    jsonres=request.get_json()
    try:
        title=jsonres["title"]
    except:
        return jsonify({"error":"Error en el json"})
    
    doc = ET.parse("archivos/discos.xml")
    raizDiscos = doc.getroot()
    for cd in raizDiscos:
            if(cd.findall("title")[0].text.lower()==title.lower()):
                diccionario={
                "artist":cd.findall("artist")[0].text,
                "country":cd.findall("country")[0].text,
                "company":cd.findall("company")[0].text,
                "price":cd.findall("price")[0].text,
                "year":cd.findall("year")[0].text
                }
                return jsonify({"disco":diccionario})
    return jsonify({"mensaje":"No existe un disco con este titulo"})
                
#Post /discoYear/
#Recibe un json con el año un año y devuelve tods los discos con esa fecha
@app.route('/discoYear/',methods=["POST"])
def discoYear():
    jsonres=request.get_json()
    try:
        year=str(jsonres["year"])
    except:
        return jsonify({"error":"Error en el json"})
    doc = ET.parse("archivos/discos.xml")
    raizDiscos = doc.getroot()
    lista=[]
    rs=False
    for cd in raizDiscos:
            if(cd.findall("year")[0].text==year):
                rs=True
                diccionario={
                "title":cd.findall("title")[0].text,
                "artist":cd.findall("artist")[0].text,
                "country":cd.findall("country")[0].text,
                "company":cd.findall("company")[0].text,
                "price":cd.findall("price")[0].text,
                "year":cd.findall("year")[0].text
                }
                lista.append(diccionario)
    if rs:
        return jsonify({"disco":lista})
    else:
        return jsonify({"mensaje":"No se encontraron discos con ese año"})

    
#Post /discoArtista/
#Recibe un Json con un artista y devuelve todos sus discos
@app.route('/discoArtista/',methods=["POST"])
def discoArtista():
    jsonres=request.get_json()
    
    try:
        artista=jsonres["artist"]
    except:
        return jsonify({"error":"Error en el json"})
    
    doc = ET.parse("archivos/discos.xml")
    raizDiscos = doc.getroot()
    lista=[]
    rs=False
    for cd in raizDiscos:
            if(cd.findall("artist")[0].text.lower()==artista.lower()):
                rs=True
                diccionario={
                "artist":cd.findall("artist")[0].text,
                "title":cd.findall("title")[0].text,
                "year":cd.findall("year")[0].text,
                "country":cd.findall("country")[0].text,
                "company":cd.findall("company")[0].text,
                "price":cd.findall("price")[0].text
                }
                lista.append(diccionario)
    if rs:
        return jsonify({"artista":lista})
    else:
        return jsonify({"mensaje":"No se encontraron discos de este artista"})
    
    
#Post /agregarDisco/
#Recibe un Json con toda la informacion de un disco y lo agrega
@app.route('/agregarDisco/',methods=["POST"])
def agregarDisco():
    doc = ET.parse("archivos/discos.xml")
    raiz = doc.getroot()
    
    jsonres=request.get_json()
    
    try:
        title=jsonres["title"]
        artist=jsonres["artist"]
        country=jsonres["country"]
        company=jsonres["company"]
        price=jsonres["price"]
        year=jsonres["year"]
    except:
        return jsonify({"error":"Error en el json"})
    
    nuevoDisco = ET.SubElement(raiz,"cd")
    ET.SubElement(nuevoDisco, "title").text = title.lower()
    ET.SubElement(nuevoDisco, "artist").text = artist.lower()
    ET.SubElement(nuevoDisco, "country").text = country.lower()
    ET.SubElement(nuevoDisco, "company").text = company.lower()
    ET.SubElement(nuevoDisco, "price").text = str(price)
    ET.SubElement(nuevoDisco, "year").text = str(year)
    doc.write("archivos/discos.xml", xml_declaration=True,encoding="utf-8")
    return jsonify({"mensaje":"Listo,disco agregado con exito"})
    

#Post /modificarDisco/
#Recibe un Json con todos los datos de un disco, pero primero verifica si exite el titulo
@app.route('/modificarDisco/',methods=["POST"])
def modificarDisco():
    jsonres=request.get_json()
    
    try:
        title=jsonres["title"]
        artist=jsonres["artist"]
        country=jsonres["country"]
        company=jsonres["company"]
        price=jsonres["price"]
        year=jsonres["year"]
    except:
        return jsonify({"error":"Error en el json"})
    
    doc = ET.parse("archivos/discos.xml")
    raizDiscos = doc.getroot()

    for cd in raizDiscos:
        if(cd.findall("title")[0].text.lower()==title.lower()):
            cd.findall("artist")[0].text = artist.lower()
            cd.findall("country")[0].text = country.lower()
            cd.findall("company")[0].text = company.lower()
            cd.findall("price")[0].text = str(price)
            cd.findall("year")[0].text = str(year)
            doc.write("archivos/discos.xml", xml_declaration=True,encoding="utf-8")
            return jsonify({"mensaje":"Disco modificado con exito!"})
    return jsonify({"error":"No existe un disto con este titulo"})

#Post /eliminarDisco/
#Recibe un Json con el titulo a eliminar
@app.route('/eliminarDisco/',methods=["POST"])
def eliminarDisco():
    
    jsonres=request.get_json()
   
    try:
        title=jsonres["title"]
    except:
        return jsonify({"error":"Error en el json"})
    
    doc = ET.parse("archivos/discos.xml")
    raizDiscos = doc.getroot()
    
    for cd in raizDiscos:
        if(cd.findall("title")[0].text.lower()==title.lower()):
            raizDiscos.remove(cd)
            doc.write("archivos/discos.xml", xml_declaration=True,encoding="utf-8")
            return jsonify({"mensaje":"Disco eliminado con exito"})
        
    return jsonify({"mensaje":"No existe un disto con este titulo"})
    
#Get /reporteDiscos/
#Genera un reporte con graphviz de todos los discos
@app.route('/reporteDiscos/')
def reporteDiscos():
    contador = 0
    manf = open('Comandos/ComandosDiscos.dot', 'w')
    
    comando = 'digraph G {\ncharset="latin1"\nnode [shape=square,style="rounded"];\nrankdir="LR";\n'
    
    doc = ET.parse("archivos/discos.xml")
    raizDiscos = doc.getroot()
    
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
                comando += f'nodeTitulo{contador}[label="Title: \\"{format(nuevoTitle)}\\""]\n'
            else:
                comando += f'nodeTitulo{contador}[label="Title:{cd.findall("title")[0].text}"]\n'

            if (artist[0] == '"'):
                nuevoartist = artist.strip('"')
                comando += f'nodeArtista{contador}[label="Artista: \\"{format(nuevoartist)}\\""]\n'
            else:
                comando += f'nodeArtista{contador}[label="Artista:{cd.findall("artist")[0].text}"]\n'
            if (country[0] == '"'):
                nuevocountry = country.strip('"')
                comando += f'nodeCountry{contador}[label="Country: \\"{format(nuevocountry)}\\""]\n'
            else:
                comando += f'nodeCountry{contador}[label="Country:{cd.findall("country")[0].text}"]\n'
            if (company[0] == '"'):
                nuevocompany = company.strip('"')
                comando += f'nodeCompany{contador}[label="Company: \\"{format(nuevocompany)}\\""]\n'
            else:
                comando += f'nodeCompany{contador}[label="Company:{cd.findall("company")[0].text}"]\n'
            if (price[0] == '"'):
                nuevoprice = price.strip('"')
                comando += f'nodePrice{contador}[label="Price: \\"{format(nuevoprice)}\\""]\n'
            else:
                comando += f'nodePrice{contador}[label="Price:{cd.findall("price")[0].text}"]\n'
            if (year[0] == '"'):
                nuevoyear = year.strip('"')
                comando += f'nodeYear{contador}[label="Year: \\"{format(nuevoyear)}\\""]\n'
            else:
                comando += f'nodeYear{contador}[label="Year:{cd.findall("year")[0].text}"]\n'

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
    return jsonify({"mensaje":"Reporte generado con exito"})

@app.route('/reporteDiscosFront/')
def reporteDiscosFront():
    jsonres=request.get_json()
    try:
        ruta=jsonres["ruta"]
    except:
        return jsonify({"error":"Error en el json"})

    contador = 0
    manf = open('Comandos/ComandosDiscos.dot', 'w')
    
    comando = 'digraph G {\ncharset="latin1"\nnode [shape=square,style="rounded"];\nrankdir="LR";\n'
    
    doc = ET.parse("archivos/discos.xml")
    raizDiscos = doc.getroot()
    
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
                comando += f'nodeTitulo{contador}[label="Title: \\"{format(nuevoTitle)}\\""]\n'
            else:
                comando += f'nodeTitulo{contador}[label="Title:{cd.findall("title")[0].text}"]\n'

            if (artist[0] == '"'):
                nuevoartist = artist.strip('"')
                comando += f'nodeArtista{contador}[label="Artista: \\"{format(nuevoartist)}\\""]\n'
            else:
                comando += f'nodeArtista{contador}[label="Artista:{cd.findall("artist")[0].text}"]\n'
            if (country[0] == '"'):
                nuevocountry = country.strip('"')
                comando += f'nodeCountry{contador}[label="Country: \\"{format(nuevocountry)}\\""]\n'
            else:
                comando += f'nodeCountry{contador}[label="Country:{cd.findall("country")[0].text}"]\n'
            if (company[0] == '"'):
                nuevocompany = company.strip('"')
                comando += f'nodeCompany{contador}[label="Company: \\"{format(nuevocompany)}\\""]\n'
            else:
                comando += f'nodeCompany{contador}[label="Company:{cd.findall("company")[0].text}"]\n'
            if (price[0] == '"'):
                nuevoprice = price.strip('"')
                comando += f'nodePrice{contador}[label="Price: \\"{format(nuevoprice)}\\""]\n'
            else:
                comando += f'nodePrice{contador}[label="Price:{cd.findall("price")[0].text}"]\n'
            if (year[0] == '"'):
                nuevoyear = year.strip('"')
                comando += f'nodeYear{contador}[label="Year: \\"{format(nuevoyear)}\\""]\n'
            else:
                comando += f'nodeYear{contador}[label="Year:{cd.findall("year")[0].text}"]\n'

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
    comand = "dot -Tjpg Comandos/ComandosDiscos.dot -o {}/ReporteDiscos.jpg".format(ruta)
    check_output(comand, shell=True)
    return jsonify({"mensaje":"Reporte generado con exito"})

#-----------------------------------------------------------------------------------------   

#----------------------------------Opciones empleados-------------------------------------
#Acaa estan todas las peticiones (get y post)
    
#Get /empleados/
#Devuelve todos los empleados en formato json
@app.route('/empleados/') 
def empleados():
    doc = ET.parse("archivos/empleados.xml")
    raizEmpleados = doc.getroot()
    departamentos={}
    
    for departamento in raizEmpleados:
        depto=departamento.attrib['departamento']
        empleadosDepto=[]
        for empleado in departamento:
            dic={
                'id': empleado.attrib['id'],
                "nombre":empleado.findall("nombre")[0].text ,
                "puesto":empleado.findall("puesto")[0].text ,
                "salario":empleado.findall("salario")[0].text
            }
            empleadosDepto.append(dict(dic))
        departamentos[depto]=empleadosDepto
    return jsonify({"empresa":departamentos})

#Post /empleadonombre/
#Recibe el nombre del empleado y muestra su informacion
@app.route('/empleadoNombre/',methods=["POST"])
def empleadoNombre():
    jsonres=request.get_json()
    
    try:
        nombre=jsonres["nombre"]
    except:
        return jsonify({"error":"Error en el json"})
    
    doc = ET.parse("archivos/empleados.xml")
    raizEmpleados= doc.getroot()
    
    for departamento in raizEmpleados:
            for empleado in departamento:
                depto=departamento.attrib['departamento']
                if (empleado.findall("nombre")[0].text.lower() == nombre.lower()):
                    diccionario={
                    "Nombre":empleado.findall("nombre")[0].text,
                    "Puesto":empleado.findall("puesto")[0].text,
                    "Salario":empleado.findall("salario")[0].text,
                    "Departamento":depto
                    }
                    lista=[diccionario]
                    return jsonify({"nombre":diccionario})
    return jsonify({"mensaje":"No hay un empleado con ese nombre"})
    
    
    
#Post /empleadosDepartamento/
#Recibe un json con el nombre del departamento
@app.route('/empleadosDepartamento/',methods=["POST"])
def empleadosDepartamento():
    doc = ET.parse("archivos/empleados.xml")
    raizEmpleados = doc.getroot()
    departamentos={}
    jsonres=request.get_json()
    try:
        dept=jsonres["departamento"]
    except:
        return jsonify({"Error":"Error en el json"})
    
    for departamento in raizEmpleados:
        depto=departamento.attrib['departamento']
        empleadosDepto=[]
        for empleado in departamento:
            dic={
                "nombre":empleado.findall("nombre")[0].text ,
                "puesto":empleado.findall("puesto")[0].text ,
                "salario":empleado.findall("salario")[0].text
            }
            empleadosDepto.append(dic)
        if depto==dept:
                return jsonify({"deparmento":empleadosDepto})
    return jsonify({"Mensaje":"Este departamento no existe dentro de la empresa"})    
    
#Post /empleadoSueldo/
#Recibe un json con el sueldo a buscar
@app.route('/empleadosSueldo/',methods=["POST"])
def empleadosSueldo():
    doc = ET.parse("archivos/empleados.xml")
    raizEmpleados = doc.getroot()
    jsonres=request.get_json()
    
    try:
        sueldo=jsonres["sueldo"]
    except:
        return jsonify({"error":"Error en el json"})
    empleados=[]
    rs=False
    
    for departamento in raizEmpleados:
        depto=departamento.attrib['departamento']
        for empleado in departamento:
            if float(empleado.findall("salario")[0].text)==float(sueldo):
                rs=True
                dic={
                    "nombre":empleado.findall("nombre")[0].text ,
                    "puesto":empleado.findall("puesto")[0].text ,
                    "salario":empleado.findall("salario")[0].text,
                    "departamento":depto
                }
                empleados.append(dic)
    if rs:
        return jsonify({f"sueldo":empleados})
    else:
        return jsonify({"mensaje":"No hay ningun empleado con ese salario"})
    
#Post agregarEmpleado/
#Recibe un json con el departamento a agregar y toda la info. del empleado
@app.route('/agregarEmpleado/',methods=["POST"])
def agregarEmpleado():
    doc = ET.parse("archivos/empleados.xml")
    raizEmpleados = doc.getroot()
    rs=False
    contador=0
    
    raizEmpleados = doc.getroot()
    jsonres=request.get_json()
    try:
        depto=jsonres["departamento"]
        id=jsonres["id"]
        nombre=jsonres["nombre"]
        puesto=jsonres["puesto"]
        salario=jsonres["salario"]
    except:
        return jsonify({"mensaje":"Error en el json"})
    
    for departamento in raizEmpleados:
                if departamento.attrib['departamento'].lower()==depto.lower() and rs==False:
                            rs=True
                            nuevo=ET.SubElement(departamento,"empleado",id=f"{id}")
                            ET.SubElement(nuevo, "nombre").text = nombre.lower()
                            ET.SubElement(nuevo, "puesto").text = puesto.lower()
                            ET.SubElement(nuevo, "salario").text = str(salario)
                            doc.write("archivos/empleados.xml", xml_declaration=True,encoding="utf-8")
                            return jsonify({"mensaje":"Empelado agregado con exito"})
    
    return jsonify({"mensaje":"No existe un departamento con este nombre"})


#Post /modificarEmpleado/
#Recibe la id del empleado y todos sus datos a modificar
@app.route('/modificarEmpleado/',methods=["POST"])
def modificarEmpleado():
    
    doc = ET.parse("archivos/empleados.xml")
    raizEmpleados = doc.getroot()
    
    jsonres=request.get_json()
    
    try:
        id=jsonres["id"]
        nombre=jsonres["nombre"]
        puesto=jsonres["puesto"]
        salario=jsonres["salario"]
    except:
        return jsonify({"Error":"Error en el json"})
    
    for departamento in raizEmpleados:
            for empleado in departamento:
                if (empleado.attrib['id'] == id):
                    empleado.findall("nombre")[0].text = nombre
                    empleado.findall("puesto")[0].text = puesto
                    empleado.findall("salario")[0].text = salario
                    doc.write("archivos/empleados.xml", xml_declaration=True,encoding="utf-8")
                    return jsonify({"Mensaje":"Empleado modificado con exito"})
    return jsonify({"Mensaje":"No existe un empleado con esa id"})


#Post /eliminarEmpleado/
#Recibe un json con el id del empleado a eliminar
@app.route('/eliminarEmpleado/',methods=["POST"])
def eliminarEmpleado():
    
    doc = ET.parse("archivos/empleados.xml")
    raizEmpleados = doc.getroot()
    
    jsonres=request.get_json()
    try:
        id=jsonres["id"]
    except:
        return jsonify({"error":"Error en el json"})
    
    
    for departamento in raizEmpleados:
            for empleado in departamento:
                if (int(empleado.attrib['id']) == int(id)):
                    departamento.remove(empleado)
                    doc.write("archivos/empleados.xml", xml_declaration=True,encoding="utf-8")
                    return jsonify({"mensaje":"Empleado eliminado con exito"})
    return jsonify({"mensaje":"No existe un empleado con esa id"})




#Post /reporteEmpleados/
#Genera un reporte en graphviz con todos los departamentos y empleados de la empresa
@app.route('/reporteEmpleados/')
def reporteEmpleados():
    #obteniendo ruta para realizar el renderizado en carpeta static/ Django
        doc = ET.parse("archivos/empleados.xml")
        raizEmpleados = doc.getroot()

        contador = 0
        manf = open('Comandos/ComandosEmpleados.dot', 'w')
        comando = 'digraph G {\ncharset="latin1"\nnode [shape=square,style="rounded"];\nrankdir="LR";\n'

        for departamento in raizEmpleados:
            comando += f'empresa->"{departamento.attrib["departamento"]}"\n'

            # print(f"Departamento de {departamento.attrib['departamento']}")
            for empleado in departamento:
                contador += 1
                comando += f'nodeNombre{contador}[label="Nombre:{empleado.findall("nombre")[0].text}"]\n'
                comando += f'nodePuesto{contador}[label="Puesto:{empleado.findall("puesto")[0].text}"]\n'
                comando += f'nodeSalario{contador}[label="Salario:{empleado.findall("salario")[0].text}"]\n'

                comando += f'"{departamento.attrib["departamento"]}"->Empleado{contador}\n'
                comando += f'"Empleado{contador}"->nodeNombre{contador}\n'
                comando += f'"Empleado{contador}"->nodePuesto{contador}\n'
                comando += f'"Empleado{contador}"->nodeSalario{contador}\n'

        comando += "}"

        #print(comando)
        manf.write(comando)
        manf.close()
        comand = "dot -Tjpg Comandos/ComandosEmpleados.dot -o Reportes/ReporteEmpleados.jpg"
        check_output(comand, shell=True)
        return jsonify({"mensaje":"Reporte generado con exito"})

@app.route('/reporteEmpleadosFront/')
def reporteEmpleadosFront():
    #obteniendo ruta para realizar el renderizado en carpeta static/ Django
        jsonres=request.get_json()

        try:
            ruta=jsonres["ruta"]
        except:
            return jsonify({"error":"Error en el json"})

        doc = ET.parse("archivos/empleados.xml")
        raizEmpleados = doc.getroot()

        contador = 0
        manf = open('Comandos/ComandosEmpleados.dot', 'w')
        comando = 'digraph G {\ncharset="latin1"\nnode [shape=square,style="rounded"];\nrankdir="LR";\n'

        for departamento in raizEmpleados:
            comando += f'empresa->"{departamento.attrib["departamento"]}"\n'

            # print(f"Departamento de {departamento.attrib['departamento']}")
            for empleado in departamento:
                contador += 1
                comando += f'nodeNombre{contador}[label="Nombre:{empleado.findall("nombre")[0].text}"]\n'
                comando += f'nodePuesto{contador}[label="Puesto:{empleado.findall("puesto")[0].text}"]\n'
                comando += f'nodeSalario{contador}[label="Salario:{empleado.findall("salario")[0].text}"]\n'

                comando += f'"{departamento.attrib["departamento"]}"->Empleado{contador}\n'
                comando += f'"Empleado{contador}"->nodeNombre{contador}\n'
                comando += f'"Empleado{contador}"->nodePuesto{contador}\n'
                comando += f'"Empleado{contador}"->nodeSalario{contador}\n'

        comando += "}"

        #print(comando)
        manf.write(comando)
        manf.close()
        comand = "dot -Tjpg Comandos/ComandosEmpleados.dot -o {}/ReporteEmpleados.jpg".format(ruta)
        check_output(comand, shell=True)
        return jsonify({"mensaje":"Reporte generado con exito"})
#-----------------------------------------------------------------------------------------

#-----------------------------------------Paises------------------------------------------

#Get /paises/
@app.route('/paises/')
def paises():
    doc = ET.parse("archivos/paises.xml")
    raizPaises = doc.getroot()
    continentes={}
    
    for continente in raizPaises:
        cont=continente.attrib['name']
        paises=[]
        for pais in continente:
            diccionario={
                "pais":pais.findall('nombre')[0].text,
                "capital":pais.findall('capital')[0].text,
                "idioma":pais.findall('idioma')[0].text,
                "moneda":pais.attrib['moneda']
            }
            paises.append(diccionario)
        continentes[cont]=paises
    return jsonify({"mundo":continentes})
        
            
#Post /paisMoneda/
@app.route('/paisMoneda/',methods=["POST"])
def paisMoneda():
    doc = ET.parse("archivos/paises.xml")
    raizPaises = doc.getroot()
    jsonres=request.get_json()
    
    try:    
        moneda=jsonres["moneda"]
    except:
        return jsonify({"error":"Error en el json"})
    
    continentes={}
    rs=False
    
    lista=[]
    
    for continente in raizPaises:
        cont=continente.attrib['name']
        for pais in continente:
            if pais.attrib['moneda'].lower()==moneda.lower():
                rs=True
                diccionario={
                "pais":pais.findall('nombre')[0].text,
                "capital":pais.findall('capital')[0].text,
                "idioma":pais.findall('idioma')[0].text,
                "continente":cont,
                "moneda":pais.attrib['moneda']
                }
                lista.append(diccionario)
    if rs:
        return jsonify({"Moneda":lista})
    else:
        return jsonify({"mensaje":"No hay un pais con esa moneda"})

#Post /paisIdioma/     
@app.route('/paisIdioma/',methods=["POST"])
def paisIdioma():
    doc = ET.parse("archivos/paises.xml")
    raizPaises = doc.getroot()

    jsonres=request.get_json()
    
    try:    
        idioma=jsonres["idioma"]
    except:
        return jsonify({"error":"Error en el json"})
    
    continentes={}
    rs=False
    lista=[]
    
    for continente in raizPaises:
        cont=continente.attrib['name']
        for pais in continente:
            if pais.findall('idioma')[0].text.lower()==idioma.lower():
                rs=True
                diccionario={
                "pais":pais.findall('nombre')[0].text,
                "capital":pais.findall('capital')[0].text,
                "idioma":pais.findall('idioma')[0].text,
                "moneda":pais.attrib['moneda'],
                "continente":cont
                }
                lista.append(diccionario)
    if rs:
        return jsonify({"idioma":lista})
    else:
        return jsonify({"mensaje":"No hay un pais con esa moneda"})
    
    
#Post /paisContinente/
@app.route('/paisContinente/',methods=["POST"])
def paisContinente():
    doc = ET.parse("archivos/paises.xml")
    raizPaises = doc.getroot()

    jsonres=request.get_json()
    
    try:    
        conti=jsonres["continente"]
    except:
        return jsonify({"error":"Error en el json"})
    
    lista=[]
    rs=False
    
    for continente in raizPaises:
        cont=continente.attrib['name']
        if cont.lower() ==conti.lower():
            rs=True
            for pais in continente:
                diccionario={
                "pais":pais.findall('nombre')[0].text,
                "capital":pais.findall('capital')[0].text,
                "idioma":pais.findall('idioma')[0].text,
                "moneda":pais.attrib['moneda'],
                "continente":cont
                }
                lista.append(diccionario)
    if rs:
        return jsonify({"continente":lista})
    else:
        return jsonify({"mensaje":"No hay paises registrados en este continente"})
                
#Post /agregarPais/
@app.route('/agregarPais/',methods=["POST"])
def agregarPais():
    doc = ET.parse("archivos/paises.xml")
    raizPaises = doc.getroot()

    jsonres=request.get_json()
    
    try:    
        conti=jsonres["continente"]
        mon=jsonres["moneda"]
        nombre=jsonres["nombre"]
        capital=jsonres["capital"]
        idioma=jsonres["idioma"]
    except :
        return jsonify({"error":"Error en el json"})
    
    rs=False
    
    for continente in raizPaises:
         if continente.attrib['name'].lower()==conti.lower():
            nuevo=ET.SubElement(continente,"pais",moneda=mon.capitalize())
            ET.SubElement(nuevo, "nombre").text = nombre.capitalize()
            ET.SubElement(nuevo, "capital").text = capital.capitalize()
            ET.SubElement(nuevo, "idioma").text = idioma.capitalize()
            doc.write("archivos/paises.xml", xml_declaration=True,encoding="utf-8")
            return jsonify({"mensaje":"Pais agregado con exito"})
    
    return jsonify({"mensaje":"No existe un continente con este nombre"})
       
       
#Post /modificarPais/
@app.route('/modificarPais/',methods=["POST"])
def modificarPais():
    doc = ET.parse("archivos/paises.xml")
    raizPaises = doc.getroot()

    jsonres=request.get_json()
    
    try:    
        continent=jsonres["continente"]
        mon=jsonres["moneda"]
        nombre=jsonres["nombre"]
        capital=jsonres["capital"]
        idioma=jsonres["idioma"]
    except :
        return jsonify({"error":"Error en el json"})
    
    cambioContinente=True
    rs=False
    
    for continente in raizPaises:
        conti=continente.attrib['name']
        for pais in continente:
            if continent.lower()==conti.lower():
                if pais.findall('nombre')[0].text.lower()==nombre.lower():
                    rs=True
                    pais.attrib['moneda']=mon.capitalize()
                    pais.findall('capital')[0].text=capital.capitalize()
                    pais.findall('idioma')[0].text=idioma.capitalize()
                    cambioContinente=False
                    doc.write("archivos/paises.xml", xml_declaration=True,encoding="utf-8")
                    return jsonify({"mensaje":"Pais modificado con exito"})
   
    
    if cambioContinente:
        eliminado=False
        for continente in raizPaises:
            if continente.attrib['name'].lower()==continent.lower():
                
                    for eliminarcont in raizPaises:
                        for eliminarpais in eliminarcont:
                            if eliminarpais.findall('nombre')[0].text.lower()==nombre.lower():
                                eliminarcont.remove(eliminarpais)
                                doc.write("archivos/paises.xml", xml_declaration=True,encoding="utf-8")
                                eliminado=True
            
        if not eliminado:
            return jsonify({"mensaje":"No hay un pais o continente con ese nombre"})
        else:
            
            for continentenuevo in raizPaises:
                if continentenuevo.attrib['name'].lower()==continent.lower():
                    nuevo=ET.SubElement(continentenuevo,"pais",moneda=mon.capitalize())
                    ET.SubElement(nuevo, "nombre").text = nombre.capitalize()
                    ET.SubElement(nuevo, "capital").text = capital.capitalize()
                    ET.SubElement(nuevo, "idioma").text = idioma.capitalize()
                    doc.write("archivos/paises.xml", xml_declaration=True,encoding="utf-8")
                    return jsonify({"mensaje":"Pais modificado con exito"})
                           
    if  rs==False:
        return jsonify({"mensaje":"No hay un pais o continente con ese nombre"})
        
        
                    
                    
#Get /reporteRegiones/
@app.route('/reporteRegiones/')
def reporteRegiones():
    doc=ET.parse('archivos/paises.xml')
    raizPaises=doc.getroot()

    contador = 0
    manf = open('Comandos/ComandosPaises.dot', 'w')
    comando = 'digraph G {\ncharset="latin1"\nnode [shape=square,style="rounded"];\nrankdir="LR";\n'

    for continente in raizPaises:
        comando += f'mundo->"{continente.attrib["name"]}"\n'
        for pais in continente:
            contador += 1
            
            comando += f'nodeMoneda{contador}[label="Moneda:{pais.attrib["moneda"]}"]\n'
            
            comando += f'nodeNombre{contador}[label="Nombre:{pais.findall("nombre")[0].text}"]\n'
        
            comando += f'nodeCapital{contador}[label="Capital:{pais.findall("capital")[0].text}"]\n'
            
            comando += f'nodeIdioma{contador}[label="Idioma:{pais.findall("idioma")[0].text}"]\n'

            comando += f'"{continente.attrib["name"]}"->pais{contador}\n'
            comando += f'"pais{contador}"->nodeNombre{contador}\n'
            comando += f'"pais{contador}"->nodeCapital{contador}\n'
            comando += f'"pais{contador}"->nodeIdioma{contador}\n'
            comando += f'"pais{contador}"->nodeMoneda{contador}\n'
            

    comando += "}"

    print(comando)
    manf.write(comando)
    manf.close()
    comand = "dot -Tjpg Comandos/ComandosPaises.dot -o Reportes/ReportePaises.jpg"
    check_output(comand, shell=True) 
    return jsonify({"mensaje":"Reporte generado con exito"})   

@app.route('/reporteRegionesFront/')
def reporteRegionesFront():
    jsonres=request.get_json()
    try:
        ruta=jsonres["ruta"]
    except:
        return jsonify({"error":"Error en el json"})


    doc=ET.parse('archivos/paises.xml')
    raizPaises=doc.getroot()

    contador = 0
    manf = open('Comandos/ComandosPaises.dot', 'w')
    comando = 'digraph G {\ncharset="latin1"\nnode [shape=square,style="rounded"];\nrankdir="LR";\n'

    for continente in raizPaises:
        comando += f'mundo->"{continente.attrib["name"]}"\n'
        for pais in continente:
            contador += 1
            
            comando += f'nodeMoneda{contador}[label="Moneda:{pais.attrib["moneda"]}"]\n'
            
            comando += f'nodeNombre{contador}[label="Nombre:{pais.findall("nombre")[0].text}"]\n'
        
            comando += f'nodeCapital{contador}[label="Capital:{pais.findall("capital")[0].text}"]\n'
            
            comando += f'nodeIdioma{contador}[label="Idioma:{pais.findall("idioma")[0].text}"]\n'

            comando += f'"{continente.attrib["name"]}"->pais{contador}\n'
            comando += f'"pais{contador}"->nodeNombre{contador}\n'
            comando += f'"pais{contador}"->nodeCapital{contador}\n'
            comando += f'"pais{contador}"->nodeIdioma{contador}\n'
            comando += f'"pais{contador}"->nodeMoneda{contador}\n'
            

    comando += "}"

    print(comando)
    manf.write(comando)
    manf.close()
    comand = "dot -Tjpg Comandos/ComandosPaises.dot -o {}/ReportePaises.jpg".format(ruta)
    check_output(comand, shell=True) 
    return jsonify({"mensaje":"Reporte generado con exito"})   
#-----------------------------------------------------------------------------------------
                     
if __name__=='__main__':
    app.run(debug=True,port=3000)
