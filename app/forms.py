from django import forms
from django.forms import ModelForm, Form
from .models import *


class ProveedorBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    ruc = forms.CharField(label='RUC:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'ruc'}),required=False)
    nombre = forms.CharField(label='NOMBRE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre'}),required=False)
    telefono = forms.CharField(label='TELEFONO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'telefono'}),required=False)
    provincia = forms.ModelChoiceField(label='PROVINCIA:',queryset=Provincias.objects.all(),
        widget=forms.Select(attrs={'class':'form-control','id':'provincia'}),required=False)
    localidad = forms.CharField(label='LOCALIDAD:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'localidad'}),required=False)
    empresa = forms.CharField(label='EMPRESA:',
        widget=forms.CheckboxInput(attrs={'class':'form-check-input','id':'empresa', 'name':'empresa'}),required=False)


class ClienteBusqueda(Form):
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
        fields = '__all__'

class ClienteClienteInsertar(ModelForm):
    class Meta:
        model = Clientes
        fields = ('codformapago',)
        widgets = {
            'codformapago': forms.Select(attrs={'class': 'form-control'})
        }

class ProveedorProveedorInsertar(ModelForm):
    class Meta:
        model = Proveedores
        fields = ('ruc',)
        widgets = {
            'ruc': forms.TextInput(attrs={'class': 'form-control'})
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
            'tipo':forms.TextInput(attrs={'class':'form-control'}),
            'codprovincia':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'localidad':forms.TextInput(attrs={'class': 'form-control'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control'}),
            'codpostal':forms.TextInput(attrs={'class': 'form-control'}),
            'cuentabancaria':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control'}),
            'movil':forms.TextInput(attrs={'class': 'form-control'}),
            'web':forms.TextInput(attrs={'class': 'form-control'}),
        }

#ARTICULOS

class ArticuloBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    referencia = forms.CharField(label='REFERENCIA:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'referencia'}),required=False)
    familia = forms.ModelChoiceField(label='FAMILIA:',queryset=Familia.objects.all(),
        widget=forms.Select(attrs={'class':'form-control','id':'familia'}),required=False)
    descripcion = forms.CharField(label='DESCRIPCION:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'descripcion'}),required=False)
    proveedor = forms.ModelChoiceField(label='PROVEEDOR:',queryset=Proveedores.objects.all(),
        widget=forms.Select(attrs={'class':'form-control','id':'proveedor'}),required=False)
    ubicacion = forms.ModelChoiceField(label='UBICACION:',queryset=Ubicaciones.objects.all(),
        widget=forms.Select(attrs={'class':'form-control','id':'ubicacion'}),required=False)

class DateInput(forms.DateInput):
    input_type = 'date'
<<<<<<< HEAD
    
=======

>>>>>>> d6844f24a833337c098c50d02750604353db798d
class AgregarArticulo(ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'
        widgets = {
            'referencia':forms.TextInput(attrs={'class':'form-control'}),
            'familia':forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'impuesto':forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'proveedor1':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'proveedor2':forms.TextInput(attrs={'class': 'form-select form-select-sm'}),
            'descripcion_corta':forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion':forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'stock':forms.TextInput(attrs={'class': 'form-control'}),
            'stock_minimo':forms.TextInput(attrs={'class': 'form-control'}),
            'aviso_minimo':forms.TextInput(attrs={'class': 'form-select form-select-sm'}),
            'datos_producto':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_alta':DateInput(),
            'embalaje':forms.TextInput(attrs={'class': 'form-select form-select-sm'}),
            'unidades_por_caja':forms.TextInput(attrs={'class': 'form-control'}),
            'precio_ticket':forms.TextInput(attrs={'class': 'form-select form-select-sm'}),
            'modificar_ticker':forms.TextInput(attrs={'class': 'form-select form-select-sm'}),
            'observaciones':forms.TextInput(attrs={'class': 'form-control'}),
            'precio_compra':forms.TextInput(attrs={'class': 'form-control'}),
            'precio_almacen':forms.TextInput(attrs={'class': 'form-control'}),
            'precio_tienda':forms.TextInput(attrs={'class': 'form-control'}),
            'precio_con_iva':forms.TextInput(attrs={'class': 'form-control'}),
            'imagen':forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
<<<<<<< HEAD
=======

>>>>>>> d6844f24a833337c098c50d02750604353db798d
#CATEGORIAS

class FamiliaBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    nombre = forms.CharField(label='NOMBRE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre'}),required=False)
  

class AgregarFamilia(ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'})
        }

# ELEMENTO VENTA

class NuevoElemento(Form):
    codigocliente = forms.CharField(label='CODIGO CLIENTE:',
        widget=forms.TextInput(attrs={'class':'form-control form-control-sm','id':'codigocliente', 'name':'codigocliente'}),required=False)
    nombrecliente = forms.CharField(label='NOMBRE CLIENTE:',
        widget=forms.TextInput(attrs={'class':'form-control form-control-sm','id':'nombrecliente'}),required=False)
    fecha = forms.DateField(label='FECHA:',
        widget=forms.DateInput(attrs={'class':'form-control form-control-sm','id':'codigo'}),required=False)
    iva = forms.CharField(label='IVA:',
        widget=forms.TextInput(attrs={'class':'form-control form-control-sm','id':'codigo'}),required=False)
    codigoarticulo = forms.DecimalField(label='CODIGO ARTICULO:',
        widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','id':'codigoarticulo'}),required=False)
    precio = forms.DecimalField(label='PRECIO (S/.):',
        widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','id':'codigo'}),required=False)
    cantidad = forms.IntegerField(label='CANTIDAD:',
        widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','id':'codigo'}),required=False)
    descuento = forms.DecimalField(label='Dcto:',
        widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','id':'codigo'}),required=False)
    importe = forms.DecimalField(label='Importe (S/.):',
        widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','id':'codigo'}),required=False)
     

