from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import os
from Empleados.forms import FormularioAgregar, FormularioNombre,FormularioDepartamento,FormularioSalario,FormularioModificar,FormularioEliminar
import requests

end_point='http://localhost:3000/'


def home(request):
    return render(request, 'index.html')
    
# renderizado con peticion 
def prueba(request):
    respuesta = requests.get(end_point+'empleados/')
    respuesta.content
    respuesta= respuesta.content.decode("utf-8")
    respuesta = json.loads(respuesta)
    empresa = respuesta['empresa']
    departamentos = list(empresa.keys())
    empleados = list(empresa.values())
    contenxt={
        "title":"Empleados",
        "departamentos":departamentos,
        "empleados":empleados,
    }
    return render(request,'verEmpleados.html',context=contenxt)
def AgregarEmpleado(request):
    departamentos, empleados = solicitarEmpleados()
    contenxt={
        "title":'Empleados',
        "departamentos":departamentos,
        "empleados":empleados,
        'res':{'mensaje':"no"}
    }
    return render(request,'AgregarEmpleado.html',context=contenxt)
def modificarEmpleado(request):
    context={
        'title':"Empleados"
    }
    departamentos, empleados = solicitarEmpleados()
    context={
        'title':"Empleados",
        'departamentos':departamentos,
        'empleados':empleados,
        'men':{'mensaje':'no'}
    }
    return render(request,'ModificarEmpleado.html',context)
def eliminarEmpleado(request):
    context={
        'title':"Empleados"
    }
    departamentos, empleados = solicitarEmpleados()
    context={
        'title':"Empleados",
        'departamentos':departamentos,
        'empleados':empleados,
        'men':{'mensaje':'no'}
    }
    return render(request,'EliminarEmpleado.html',context)
def Reporte_Empleados(request):
    context={
        'title':"Empleados"
    }
    ruta = os.path.abspath('Empleados/static/reportes')
    res = requests.get(end_point+'reporteEmpleadosFront/',json={'ruta':ruta})
    data = res.content.decode('utf-8')
    return render(request,'ReporteEmpleados.html',context)
#renderizado
def buscarEmpleados(request):
    contenxt={
        "title":"Empleados",
    }
    return render(request,'BusquedaEmpleado.html',context=contenxt)

#renderizado despues de peticion
def peticion_Buscar_Nombre(request):
    form = FormularioNombre(request.POST)
    context ={}
    if request.method=="POST":
        if form.is_valid():
            data = form.cleaned_data
            if data != '':
                respuesta= requests.post(end_point+'empleadoNombre/',json=data)
                respuesta = respuesta.content.decode("utf-8")
                respuesta = json.loads(respuesta)
                if "nombre" in respuesta:
                    empleado = respuesta['nombre']
                    print(empleado)
                    context = {
                        'title':"Empleado",
                        'empleado' : empleado,
                        'medio':{'tipo':'nombre'},
                        'empleados_Departamento' : [],
                        'depto' : {'depto':'no info'},
                        'empleados_Salario':[]
                    }
                    print(context)
                else:
                    context = {
                        'title':"Empleado",
                        'empleado' : [],
                        'medio':{'tipo':'nombre'},
                        'empleados_Departamento' : [],
                        'depto' : {'depto':'no info'},
                        'empleados_Salario':[]
                    }
            else:
                context = {
                        'title':"Empleado",
                        'empleado' : [],
                        'medio':{'tipo':'nombre'},
                        'empleados_Departamento' : [],
                        'depto' : {'depto':'no info'},
                        'empleados_Salario':[]
                    }

    return render(request,'BusquedaEmpleado.html',context=context)

def peticion_Buscar_Departamento(request):
    form = FormularioDepartamento(request.POST)
    context ={}
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data['departamento']
            res = requests.post(end_point+"empleadosDepartamento/",json={'departamento':data})
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'deparmento' in res:
                res = res['deparmento']
                context = {
                        'title':"Empleado",
                        'empleado' :{},
                        'medio':{'tipo':'departamento'},
                        'empleados_Departamento' : res,
                        'depto' : {'depto':data},
                        'empleados_Salario':[]
                    }
            else:
                context = {
                        'title':"Empleado",
                        'empleado' :{},
                        'medio':{'tipo':'departamento'},
                        'empleados_Departamento' : [],
                        'depto' : {'depto':data},
                        'empleados_Salario':[]
                    }
            


    return render(request,'BusquedaEmpleado.html',context=context)

def peticion_Buscar_Sueldo(request):
    context ={}
    form = FormularioSalario(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data['salario']
            res = requests.post(end_point+'empleadosSueldo/',json={'sueldo':data})
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'sueldo' in res:
                res = res['sueldo']
                context = {
                        'title':"Empleado",
                        'empleado' :{},
                        'medio':{'tipo':'salario'},
                        'empleados_Departamento' : [],
                        'depto' : {'depto':'no info'},
                        'empleados_Salario':res
                    }
            else:
                context = {
                        'title':"Empleado",
                        'empleado' :{},
                        'medio':{'tipo':'salario'},
                        'empleados_Departamento' : [],
                        'depto' : {'depto':'no info'},
                        'empleados_Salario':[]
                    }

    return render(request,'BusquedaEmpleado.html',context=context)

def Peticion_Agregar_Empleado(request):
    form = FormularioAgregar(request.POST)
    contenxt={
        "title":'Empleados'
    }
    if form.is_valid():
        data = form.cleaned_data
        send = {
            'departamento' : data['departamento'],
            'id':data['id'],
            'nombre' : data['nombre'],
            'puesto' : data['puesto'],
            'salario' : data['salario']
           }
        respuesta = requests.post(end_point+'agregarEmpleado/',json=send)
        respuesta = respuesta.content.decode('utf-8')
        respuesta = json.loads(respuesta)
        respuesta = respuesta['mensaje']
        departamentos, empleados = solicitarEmpleados()
        contenxt={
        "title":'Empleados',
        "departamentos":departamentos,
        "empleados":empleados,
        'res':{'mensaje':respuesta}
        }

    return render(request,'AgregarEmpleado.html',context=contenxt)

def peticion_Modificar_Empleado(request):
    context = {}
    mensaje = ''
    form = FormularioModificar(request.POST)
    print(form.is_valid())
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            res = requests.post(end_point+'modificarEmpleado/',json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'Mensaje' in res:
                mensaje = res['Mensaje']
            else:
                mensaje = 'no'
    departamentos, empleados = solicitarEmpleados()
    context={
        'title':"Empleados",
        'departamentos':departamentos,
        'empleados':empleados,
        'men':{'mensaje':mensaje}
    }
    return render(request,'ModificarEmpleado.html',context)

def peticion_Eliminar_Empleado(request):
    context={}
    men ={} 
    form = FormularioEliminar(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            res = requests.post(end_point+'eliminarEmpleado/',json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)

            if 'mensaje' in res:
                men = { 'mensaje':res['mensaje']}
                print(men)
            else:
                men = { 'mensaje':"error"}
    departamentos, empleados = solicitarEmpleados()
    context={
        'title':"Empleados",
        'departamentos':departamentos,
        'empleados':empleados,
        'men':{'mensaje':men['mensaje']}
    }
    return render(request,'EliminarEmpleado.html',context)

def solicitarEmpleados():
    respuesta = requests.get(end_point+'empleados/')
    respuesta.content
    respuesta= respuesta.content.decode("utf-8")
    respuesta = json.loads(respuesta)
    empresa = respuesta['empresa']
    departamentos = list(empresa.keys())
    empleados = list(empresa.values())
    return departamentos, empleados