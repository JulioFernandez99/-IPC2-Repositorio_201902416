from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import os
import requests
from Discos.forms import FormularioTitulo,FormularioYear,FormularioArtista,FormularioAgregar,FormularioModificar,FormularioEliminar
end_point='http://localhost:3000/'
def verDiscos(request):
    res = requests.get(end_point+'discos/')
    res = res.content.decode('utf-8')
    res = json.loads(res)
    discos = res['discos']
    context = {
        'discos':discos
    }
    return render(request,'verDiscos.html',context=context)

def buscarDiscos(request):
    context = {
        'title':'discos',
        'type':{'tipo_consulta':"None"}
    }
    return render(request,'BuscarDiscos.html',context=context)

def agregarDiscos(request):
    discos = pet_Discos()
    context = {
        'discos_Existentes':discos,
        'nota':{"mensaje":"no"}
    }
    return render(request,'agregarDiscos.html',context=context)

def modificarDiscos(request):
    discos = pet_Discos()
    context={
        'discos':discos,
        'men':{'mensaje':'no'}
    }
    return render(request,'ModificarDiscos.html',context=context)

def eliminarDiscos(request):
    discos = pet_Discos()
    context={
        'discos':discos,
        'men':{'mensaje':'no'}
    }
    return render(request,'eliminarDiscos.html',context=context)

def reporteDiscos(request):
    context={
        'title':"Empleados"
    }
    ruta = os.path.abspath('Discos/static/reportes')
    res = requests.get(end_point+'reporteDiscosFront/',json={'ruta':ruta})
    data = res.content.decode('utf-8')
    return render(request,'reporteDiscos.html',context)

def peticion_Buscar_Titulo(request):
    context = {}
    form = FormularioTitulo(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            res = requests.post(end_point+'discoTitulo/',json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'disco' in res:
                context = {
                'title':'discos',
                'type':{'tipo_consulta':"titulo"},
                'disco_titulo':res['disco'],
                'discos_year':[],
                'disocs_artist':[]
                }
                print(res)
            else:
                context = {
                'title':'discos',
                'type':{'tipo_consulta':"titulo"},
                'disco_titulo':{},
                'discos_year':[],
                'disocs_artist':[]
                }
    return render(request,'BuscarDiscos.html',context=context)

def peticion_Buscar_Year(request):
    context = {}
    form = FormularioYear(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data =form.cleaned_data
            res = requests.post(end_point+'discoYear/',json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'disco' in res:
                res = res['disco']
                context = {
                'title':'discos',
                'type':{'tipo_consulta':"year"},
                'disco_titulo':{},
                'discos_year':res,
                'disocs_artist':[]
                }
            elif 'mensaje' in res:
                context = {
                'title':'discos',
                'type':{'tipo_consulta':"year"},
                'disco_titulo':{},
                'discos_year':[],
                'disocs_artist':[]
                }

    return render(request,'BuscarDiscos.html',context=context)
def peticion_Buscar_Artista(request):
    context = {}
    form = FormularioArtista(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data =form.cleaned_data
            res = requests.post(end_point+"discoArtista/",json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'artista' in res:
                context = {
                'title':'discos',
                'type':{'tipo_consulta':"artista"},
                'disco_titulo':{},
                'discos_year':[],
                'disocs_artist':res['artista']
                }
            else:
                context = {
                'title':'discos',
                'type':{'tipo_consulta':"artista"},
                'disco_titulo':{},
                'discos_year':[],
                'disocs_artist':[]
                }
    return render(request,'BuscarDiscos.html',context=context)

def peticion_Agregar_Disco(request):
    context ={}
    form = FormularioAgregar(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            res = requests.post(end_point+"agregarDisco/",json=data)
            res = res.content.decode('utf-8')
            res =json.loads(res)
            if "mensaje" in res:
                res = res['mensaje']
                discos = pet_Discos()
                context = {
                'discos_Existentes':discos,
                'nota':{"mensaje":res}
                }
            else:
                discos = pet_Discos()
                context = {
                'discos_Existentes':discos,
                'nota':{"mensaje":"Error"}
                }
    return render(request,'agregarDiscos.html',context=context)        

def peticion_Modificar_Disco(request):
    context = {}
    form = FormularioModificar(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            res = requests.post(end_point+"modificarDisco/",json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if "mensaje" in res:
                res = res['mensaje']
                discos = pet_Discos()
                context={
                    "discos":discos,
                    'men':{'mensaje':res}
                }
            else:
                context={
                    "discos":discos,
                    'men':{'mensaje':'error'}
                }
    return render(request,'ModificarDiscos.html',context=context)

def peticion_Eliminar_Discos(request):
    context = {}
    formulario = FormularioEliminar(request.POST)
    if request.method == "POST":
        if formulario.is_valid():
            data = formulario.cleaned_data
            res = requests.post(end_point+'eliminarDisco/',json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'mensaje' in res:
                discos = pet_Discos()
                context = {
                    'discos':discos,
                    'men':{'mensaje':res['mensaje']}
                }
            else:
                discos = pet_Discos()
                context = {
                    'discos':discos,
                    'men':{'mensaje':'no'}
                }
    return render(request,'eliminarDiscos.html',context=context)      

def pet_Discos():
    res = requests.get(end_point+'discos/')
    res = res.content.decode('utf-8')
    res = json.loads(res)
    discos = res['discos']
    return discos