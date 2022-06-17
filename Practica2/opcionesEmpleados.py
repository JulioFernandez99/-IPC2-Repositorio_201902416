from xml.etree.ElementTree import *
from subprocess import check_output

class OpcionesEmpleados:
    raizEmpleados = None
    doc = None

    def CargarDatosEmpleados(self):
        global raizEmpleados, doc
        doc = parse("empleados.xml")
        raizEmpleados = doc.getroot()

    def verEmpleado(self, id):
        global raizEmpleados, doc
        for departamento in raizEmpleados:
            for empleado in departamento:
                if (empleado.attrib['id'] == id):
                    print(f'Nombre: {empleado.findall("nombre")[0].text}')
                    print(f'Puesto: {empleado.findall("puesto")[0].text}')
                    print(f'Salario: {empleado.findall("salario")[0].text} \n')
                    return
        print("No existe un usuario con esta id\n")

    def modificarEmpleado(self, id):
        global raizEmpleados, doc
        for departamento in raizEmpleados:
            for empleado in departamento:
                if (empleado.attrib['id'] == id):
                    nombre = input("Nombre: ")
                    puesto = input("Puesto: ")
                    salario = input("Salario: ")

                    empleado.findall("nombre")[0].text = nombre
                    empleado.findall("puesto")[0].text = puesto
                    empleado.findall("salario")[0].text = salario
                    print("Empleado modificado\n")
                    return
        print("No existe un usuario con esta id\n")

    def eliminarEmpleado(self, id):
        global raizEmpleados, doc
        for departamento in raizEmpleados:
            for empleado in departamento:
                if (empleado.attrib['id'] == id):
                    departamento.remove(empleado)

                    print("Empleado eliminado\n")
                    return
        print("No existe un usuario con esa id\n")

    def verTodosEmpleados(self):
        global raizEmpleados
        print("")
        for departamento in raizEmpleados:
            print(f"Departamento de {departamento.attrib['departamento']}")
            for empleado in departamento:
                print(f'\tNombre: {empleado.findall("nombre")[0].text}')
                print(f'\tPuesto: {empleado.findall("puesto")[0].text}')
                print(f'\tSalario: {empleado.findall("salario")[0].text} \n')

    def cerrarDocEmpleados(self):
        global raizEmpleados, doc
        doc.write("empleados.xml",xml_declaration=True,encoding="utf-8")

    def generarReporte(self):
        contador = 0
        manf = open('Comandos/ComandosEmpleados.dot', 'w')
        comando = 'digraph G {\ncharset="latin1"\nnode [shape=square,style="rounded"];\nrankdir="LR";\n'

        for departamento in raizEmpleados:
            comando += f'empresa->"{departamento.attrib["departamento"]}"\n'

            # print(f"Departamento de {departamento.attrib['departamento']}")
            for empleado in departamento:
                contador += 1
                comando += f'nodeNombre{contador}[label="Nombre:{empleado.findall("nombre")[0].text}"]\n'
                comando += f'nodePuesto{contador}[label="Puesto{empleado.findall("puesto")[0].text}"]\n'
                comando += f'nodeSalario{contador}[label="{empleado.findall("salario")[0].text}"]\n'

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




opcEmp = OpcionesEmpleados()
