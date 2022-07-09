from django import forms

class FormularioNombre(forms.Form):
    nombre = forms.CharField(label='nombre')

class FormularioDepartamento(forms.Form):
    departamento = forms.CharField(label='departamento')

class FormularioSalario(forms.Form):
    salario = forms.CharField(label = 'salario')

class FormularioAgregar(forms.Form):
    departamento = forms.CharField(label="departamento")
    id = forms.CharField(label="id")
    nombre = forms.CharField(label="nombre")
    puesto = forms.CharField(label="puesto")
    salario = forms.CharField(label="salario")

class FormularioModificar(forms.Form):
    id = forms.CharField(label="id")
    nombre = forms.CharField(label="nombre")
    puesto = forms.CharField(label="puesto")
    salario = forms.CharField(label="salario")

class FormularioEliminar(forms.Form):
    id = forms.CharField(label="id")