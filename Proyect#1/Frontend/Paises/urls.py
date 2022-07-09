from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('verPaises',views.verPaises,name="verPaises"),
    path('buscarPaises',views.buscarPaises,name="buscarPaises"),
    path('agregarPais',views.agregarPais,name="agregarPais"),
    path('modificarPais',views.modificarPais,name="modificarPais"),
    path('reportePaises',views.reportePaises,name='reportePaises'),
    path('peticion_Buscar_Moneda/',views.peticion_Buscar_Moneda,name="peticion_Buscar_Moneda"),
    path('peticion_Buscar_Idioma/',views.peticion_Buscar_Idioma,name="peticion_Buscar_Idioma"),
    path('peticion_Buscar_Continente/',views.peticion_Buscar_Continente,name="peticion_Buscar_Continente"),
    path('peticio_Agregar_Pais/',views.peticio_Agregar_Pais,name="peticio_Agregar_Pais"),
    path('peticion_Modificar_Pais/',views.peticion_Modificar_Pais,name="peticion_Modificar_Pais"),
]