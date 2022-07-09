from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import os
from Paises.forms import *
import requests

end_point='http://localhost:3000/'

def verPaises(request):
    context = {}
    continentes,paises = pet_Paises()
    context = {
        'continentes':continentes,
        'paises':paises,
    }
    return render(request,'verPaises.html',context=context)

def buscarPaises(request):
    context ={
        'resultados':[],
        'mensaje':{'mensaje':'no','tipo':'moneda'}
    }
    return render(request,'buscarPaises.html',context=context)

def agregarPais(request):
    context = {}
    continentes,paises = pet_Paises()
    context ={
        'continentes':continentes,
        'paises':paises,
        'men':{'mensaje':'no'}
    }
    return render(request,'agregarPaises.html',context=context)

def modificarPais(request):
    context = {}
    continentes,paises = pet_Paises()
    context = {
        'continentes':continentes,
        'paises':paises,
        'men':{'mensaje':'no'}
    }
    return render(request,'ModificarPais.html',context=context)

def reportePaises(request):
    context={
        'title':"Paises"
    }
    ruta = os.path.abspath('Paises/static/reportes')
    res = requests.get(end_point+'reporteRegionesFront/',json={'ruta':ruta})
    data = res.content.decode('utf-8')
    return render(request,'reportePaises.html',context)

#-------------------------------------------


# ------------------------------------------
def peticion_Buscar_Moneda(request):
    context = {}
    formulario = FormularioMoneda(request.POST)
    if request.method == "POST":
        if formulario.is_valid():
            data = formulario.cleaned_data
            res = requests.post(end_point+'paisMoneda/',json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'Moneda' in res:
                res = res['Moneda']
                context = {
                    'resultados':res,
                    'mensaje':{'mensaje':'no','tipo':'moneda'}
                }
            else:
                context = {
                    'resultados':[],
                    'mensaje':{'mensaje':'si','tipo':'moneda'}
                }
                
    return render(request,'buscarPaises.html',context=context)

def peticion_Buscar_Idioma(request):
    context = {}
    formulario = FormularioIdioma(request.POST)
    if request.method == "POST":
        if formulario.is_valid():
            data = formulario.cleaned_data
            res = requests.post(end_point+'paisIdioma/',json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'idioma' in res:
                res = res['idioma']
                context ={
                    'resultados':res,
                    'mensaje':{'mensaje':'no','tipo':'idioma'}
                }
            else:
                context ={
                    'resultados':[],
                    'mensaje':{'mensaje':'si','tipo':'idioma'}
                }
    return render(request,'buscarPaises.html',context=context)

def peticion_Buscar_Continente(request):
    context ={}
    formulario = FormularioContinente(request.POST)
    if request.method == "POST":
        if formulario.is_valid():
            data = formulario.cleaned_data
            res = requests.post(end_point+'paisContinente/',json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'continente' in res:
                res = res['continente']
                context ={
                    'resultados':res,
                    'mensaje':{'mensaje':'no','tipo':'continente'}
                } 
            else:
                context ={
                    'resultados':[],
                    'mensaje':{'mensaje':'si','tipo':'continente'}
                }
    return render(request,'buscarPaises.html',context=context)

def peticio_Agregar_Pais(request):
    context = {}
    formulario = FormularioAgregar(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            data = formulario.cleaned_data
            res = requests.post(end_point+'agregarPais/',json=data)
            res = res.content.decode('utf-8')
            res= json.loads(res)
            if 'mensaje' in res :
                continentes,paises = pet_Paises()
                context ={
                    'continentes':continentes,
                    'paises':paises,
                    'men':{'mensaje':res['mensaje']}
                }
            else:
                continentes,paises = pet_Paises()
                context ={
                    'continentes':continentes,
                    'paises':paises,
                    'men':{'mensaje':'Error Al guardar'}
                } 
    return render(request,'agregarPaises.html',context=context)

def peticion_Modificar_Pais(request):
    context = {}
    formulario = FormularioModificar(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            data = formulario.cleaned_data
            res = requests.post(end_point+'modificarPais/',json=data)
            res = res.content.decode('utf-8')
            res = json.loads(res)
            if 'mensaje' in res:
                res = res['mensaje']
                continentes,paises = pet_Paises()
                context = {
                    'continentes':continentes,
                    'paises':paises,
                    'men':{'mensaje':res}
                }
            else:
                context = {
                    'continentes':continentes,
                    'paises':paises,
                    'men':{'mensaje':'si'}
                }
    return render(request,'ModificarPais.html',context=context)

def pet_Paises():
    res = requests.get(end_point+'paises/')
    res = res.content.decode('utf-8')
    res = json.loads(res)
    res = res['mundo']
    continente = list(res.keys())
    paises = list(res.values())
    return continente,paises