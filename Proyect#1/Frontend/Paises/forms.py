from django import forms

class FormularioMoneda(forms.Form):
    moneda = forms.CharField(label = 'moneda')

class FormularioIdioma(forms.Form):
    idioma = forms.CharField(label = 'idioma')

class FormularioContinente(forms.Form):
    continente = forms.CharField(label = 'continente')

class FormularioAgregar(forms.Form):
    continente = forms.CharField(label="continente")
    moneda = forms.CharField(label="moneda")
    nombre = forms.CharField(label="nombre")
    capital = forms.CharField(label="capital")
    idioma = forms.CharField(label="idioma")

class FormularioModificar(forms.Form):
    continente = forms.CharField(label="continente")
    moneda = forms.CharField(label="moneda")
    nombre = forms.CharField(label="nombre")
    capital = forms.CharField(label="capital")
    idioma = forms.CharField(label="idioma")
