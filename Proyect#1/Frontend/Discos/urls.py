from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('verDiscos',views.verDiscos,name="verDiscos"),
    path('buscarDiscos',views.buscarDiscos,name="buscarDiscos"),
    path('agregarDiscos',views.agregarDiscos,name="agregarDiscos"),
    path('modificarDiscos',views.modificarDiscos,name="modificarDiscos"),
    path('eliminarDiscos',views.eliminarDiscos,name="eliminarDiscos"),
    path('reporteDiscos',views.reporteDiscos,name="reporteDiscos"),

    path('peticion_Buscar_Year/',views.peticion_Buscar_Year,name="peticion_Buscar_Year"),
    path('peticion_Buscar_Titulo/',views.peticion_Buscar_Titulo,name="peticion_Buscar_Titulo"),
    path('peticion_Buscar_Artista/',views.peticion_Buscar_Artista,name="peticion_Buscar_Artista"),
    path('peticion_Agregar_Disco/',views.peticion_Agregar_Disco,name="peticion_Agregar_Disco"),
    path('peticion_Modificar_Disco/',views.peticion_Modificar_Disco,name="peticion_Modificar_Disco"),
    path('peticion_Eliminar_Discos/',views.peticion_Eliminar_Discos,name="peticion_Eliminar_Discos"),
]