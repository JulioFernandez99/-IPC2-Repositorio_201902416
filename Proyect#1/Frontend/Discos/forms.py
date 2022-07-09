from django import forms

class FormularioTitulo(forms.Form):
    title = forms.CharField(label='titulo')

class FormularioYear(forms.Form):
    year = forms.CharField(label='year')

class FormularioArtista(forms.Form):
    artist = forms.CharField(label = 'artist')

class FormularioAgregar(forms.Form):
    title = forms.CharField(label='title')
    artist = forms.CharField(label='artist')
    company = forms.CharField(label='company')
    country = forms.CharField(label='country')
    price = forms.CharField(label='price')
    year = forms.CharField(label='year')

class FormularioModificar(forms.Form):
    title = forms.CharField(label='title')
    artist = forms.CharField(label='artist')
    company = forms.CharField(label='company')
    country = forms.CharField(label='country')
    price = forms.CharField(label='price')
    year = forms.CharField(label='year')

class FormularioEliminar(forms.Form):
    title = forms.CharField(label='title')