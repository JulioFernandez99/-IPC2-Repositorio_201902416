from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    #renderizan una template
    path('buscarEmpleado',views.buscarEmpleados,name='BuscarEmpleado'),
    path('reporteEmpleados',views.Reporte_Empleados,name='reporteEmpleados'),
    #realizan una peticion al servidor en flask
    path('agregarEmpleado',views.AgregarEmpleado,name='agregarEmpleado'),
    path('modificarEmpleado',views.modificarEmpleado,name="modificarEmpleado"),
    path('eliminarEmpleado',views.eliminarEmpleado,name="eliminarEmpleado"),
    #renderizan un template realizando una peticion al servidor
    path('verEmpleados',views.prueba,name='verEmpleados'),
    path('buscarNombre/',views.peticion_Buscar_Nombre,name='buscarNombre'),
    path('buscarDepartamento/',views.peticion_Buscar_Departamento,name='buscarDepartamento'),
    path('buscarSalario/',views.peticion_Buscar_Sueldo,name='buscarSalario'),
    path('agregandoEmpleado/',views.Peticion_Agregar_Empleado,name="agregandoEmpleado"),
    path('modificandoEmpleado/',views.peticion_Modificar_Empleado,name="modificandoEmpleado"),
    path('eliminandoEmpleado/',views.peticion_Eliminar_Empleado,name="eliminandoEmpleado"),
]