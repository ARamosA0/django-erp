from django import forms
from django.forms import ModelForm, Form
from .models import *


class ProveedorBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    dni = forms.CharField(label='DNI:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'dni'}),required=False)
    nombre = forms.CharField(label='NOMBRE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre'}),required=False)
    telefono = forms.CharField(label='TELEFONO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'telefono'}),required=False)
    provincia = forms.ModelChoiceField(label='PROVINCIA:',queryset=Provincias.objects.all(),
        widget=forms.Select(attrs={'class':'form-control','id':'provincia'}),required=False)
    localidad = forms.CharField(label='LOCALIDAD:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'localidad'}),required=False)

class ProveedorInsertar(ModelForm):
    class Meta:
        model = Proveedores
        fields = ('__all__')

class ClienteClienteInsertar(ModelForm):
    class Meta:
        model = Clientes
        fields = ('codformapago',)
        widgets = {
            'codformapago': forms.Select(attrs={'class': 'form-control'})
        }


class AgregarPersona(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'dni':forms.TextInput(attrs={'class': 'form-control'}),
            'codprovincia':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'localidad':forms.TextInput(attrs={'class': 'form-control'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control'}),
            'codpostal':forms.TextInput(attrs={'class': 'form-control'}),
            'cuentabancaria':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control'}),
            'movil':forms.TextInput(attrs={'class': 'form-control'}),
            'web':forms.TextInput(attrs={'class': 'form-control'}),
        }

class AgregarEmpresa(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'estructurajuridica':forms.TextInput(attrs={'class':'form-control'}),
            'ruc':forms.TextInput(attrs={'class':'form-control'}),
            'codprovincia':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'localidad':forms.TextInput(attrs={'class': 'form-control'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control'}),
            'codpostal':forms.TextInput(attrs={'class': 'form-control'}),
            'cuentabancaria':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control'}),
            'movil':forms.TextInput(attrs={'class': 'form-control'}),
            'web':forms.TextInput(attrs={'class': 'form-control'}),
        }

