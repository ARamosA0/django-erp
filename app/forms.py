from django import forms
from django.forms import ModelForm, Form
from .models import *


class ProveedorBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    ruc = forms.CharField(label='RUC:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'ruc'}),required=False)
    nombre = forms.CharField(label='NOMBRE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre','list':'proveedores','autocomplete':'off'}),required=False)
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


class ProveedorInsertar(ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'

class ClienteClienteInsertar(ModelForm):
    class Meta:
        model = Clientes
        fields = ('codformapago','ruc')
        labels = {
            'codformapago':'Forma de pago',
            'ruc':'RUC',
        }
        widgets = {
            'codformapago': forms.Select(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'})
        }

class ProveedorProveedorInsertar(ModelForm):
    class Meta:
        model = Proveedores
        fields = ('ruc',)
        labels = {
            'ruc':'RUC',
        }
        widgets = {
            'ruc': forms.TextInput(attrs={'class': 'form-control'})
        }

class AgregarPersona(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        labels = {
            'dni':'DNI',
            'codprovincia':'Provincia',
            'direccion':'Dirección',
            'codpostal':'Código Postal',
            'cuentabancaria':'Cuenta Bancaria',
            'telefono':'Teléfono',
            'movil':'Móvil'
        }
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
        labels = {
            'estructurajuridica': 'Estructura jurídica',
            'ruc':'RUC',
            'codprovincia':'Provincia',
            'direccion':'Dirección',
            'codpostal':'Código Postal',
            'cuentabancaria':'Cuenta Bancaria',
            'telefono':'Teléfono',
            'movil':'Móvil'
        }
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

#PRODUCTOS

class ProductoBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    nombre = forms.CharField(label='NOMBRE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre'}),required=False)

class AgregarProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'cantidad','descripcion_producto','color','talla','precio_horas_manufactura','horas_manufactura','costos_extra')
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control form-control'}),
            'descripcion_producto':forms.TextInput(attrs={'class':'form-control form-control'}),
            'color':forms.TextInput(attrs={'class':'form-control form-control'}),
            'talla':forms.TextInput(attrs={'class':'form-control form-control'}),
            'precio_horas_manufactura':forms.NumberInput(attrs={'class':'form-control form-control', 'step': 0.1}),
            'horas_manufactura':forms.NumberInput(attrs={'class':'form-control form-control'}),
            'costos_extra':forms.NumberInput(attrs={'class':'form-control form-control', 'step': 0.1})
        }

#ARTICULOS

class ArticuloBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    nombre = forms.CharField(label='NOMBRE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre'}),required=False)
    familia = forms.ModelChoiceField(label='FAMILIA:',queryset=Familia.objects.all(),
        widget=forms.Select(attrs={'class':'form-control','id':'familia'}),required=False)
    descripcion = forms.CharField(label='DESCRIPCION:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'descripcion'}),required=False)
    tipo = forms.CharField(label='TIPO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'tipo'}),required=False)
    proveedor = forms.ModelChoiceField(label='PROVEEDOR:',queryset=Proveedores.objects.all(),
        widget=forms.Select(attrs={'class':'form-control','id':'proveedor'}),required=False)
    ubicacion = forms.ModelChoiceField(label='UBICACION:',queryset=Ubicaciones.objects.all(),
        widget=forms.Select(attrs={'class':'form-control','id':'ubicacion'}),required=False)

class DateInput(forms.DateInput):
    input_type = 'date'
class AgregarArticulo(ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'familia':forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'impuesto':forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'proveedor':forms.TextInput(attrs={'class':'form-select form-select-sm awesomplete','list':'proveedores','autocomplete':'off'}),
            'descripcion_corta':forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion':forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'stock':forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_minimo':forms.NumberInput(attrs={'class': 'form-control'}),
            'aviso_minimo':forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'datos_producto':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_alta':DateInput(attrs={'class': 'form-control col-sm'}),
            'embalaje':forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'unidades_por_caja':forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones':forms.TextInput(attrs={'class': 'form-control'}),
            'precio_compra':forms.NumberInput(attrs={'class': 'form-control', 'step':0.1}),
            'precio_tienda':forms.NumberInput(attrs={'class': 'form-control', 'step':0.1}),
            'imagen':forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

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

#PROVINCIA
class ProvinciaBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    nombreprovincia = forms.CharField(label='PROVINCIA:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre'}),required=False)

class AgregarProvincia(ModelForm):
    class Meta:
        model = Provincias
        fields = '__all__'
        labels = {
            'nombreprovincia':'Nombre'
        }
        widgets = {
            'nombreprovincia':forms.TextInput(attrs={'class':'form-control'})
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
    
     
class NuevaFactura(ModelForm):
    class Meta:
        model = Factura
        fields = ('fecha', 'iva')
        widgets = {
            'fecha':DateInput(attrs={'class':'form-control'}),
            'iva':forms.TextInput(attrs={'class':'form-control', 'value':'18'})
        }
        
#REMISION
class RemisionBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    factura = forms.CharField(label='NRO FACTURA:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'factura'}),required=False)
    cliente = forms.CharField(label='NOMBRE CLIENTE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'cliente'}),required=False)
    empresa = forms.CharField(label='EMPRESA:',
        widget=forms.CheckboxInput(attrs={'class':'form-check-input','id':'empresa', 'name':'empresa'}),required=False)

#REMISION PROVEEDORES
class RemisionProvBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    factura = forms.CharField(label='NRO FACTURA:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'factura'}),required=False)
    proveedor = forms.CharField(label='NOMBRE PROVEEDOR:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'proveedor'}),required=False)

class AgregarRemisionProv(ModelForm):
    class Meta:
        model = Remision_linea_prov
        fields = '__all__'
        widgets = {
            'factura_proveedor':forms.Select(attrs={'class': 'form-select form-select-sm'}),
        }

#FORMA DE PAGO
class FormasPagoBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    fpago = forms.CharField(label='FORMA DE PAGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'fpago'}),required=False)

class AgregarFormaPago(ModelForm):
    class Meta:
        model = Formapago
        fields = '__all__'
        labels = {
            'nombrefp':'Nombre'
        }
        widgets = {
            'nombrefp':forms.TextInput(attrs={'class': 'form-control form-control'}),
        }

#IMPUESTO
class ImpuestoBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    nombre = forms.CharField(label='NOMBRE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre'}),required=False)
    valor = forms.FloatField(label='VALOR:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'valor'}),required=False)

class AgregarImpuesto(ModelForm):
    class Meta:
        model = Impuestos
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control form-control'}),
            'valor':forms.NumberInput(attrs={'class':'form-control form-control', 'step': 0.1})
        }
  
#UBICACIONES
class UbicacionesBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    nombre = forms.CharField(label='NOMBRE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre'}),required=False)

class AgregarUbicaciones(ModelForm):
    class Meta:
        model = Ubicaciones
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'})
        }

#EMBALAJES
class EmbalajeBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    nombre = forms.CharField(label='NOMBRE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre'}),required=False)
  
class AgregarEmbalaje(ModelForm):
    class Meta:
        model = Embalajes
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'})
        }

#ENTIDADES
class EntidadBusqueda(Form):
    codigo = forms.CharField(label='CODIGO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'codigo'}),required=False)
    nombreentidad = forms.CharField(label='NOMBRE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'nombre'}),required=False)

class AgregarEntidad(ModelForm):
    class Meta:
        model = Entidades
        fields = '__all__'
        labels = {
            'nombreentidad':'Nombre'
        }
        widgets = {
            'nombreentidad':forms.TextInput(attrs={'class':'form-control'})
        }

#FACTURA
class FacturaBusqueda(Form):
    dnicliente = forms.CharField(label='DNI CLIENTE:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'dnicliente'}),required=False)
    numfactura = forms.CharField(label='NUMERO DE FACTURA:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'numfactura'}),required=False)
    fechafac = forms.DateField(label='FECHA:',
        widget=DateInput(attrs={'class':'form-control','id':'fechafac'}),required=False)

class EditarFactura(ModelForm):
    class Meta:
        model = Factura
        fields = ('fecha',)
        widgets = {
            'fecha':forms.DateInput(attrs={'class':'form-control'})
        }

# ORDEN DE COMPRA
TRUE_FALSE_CHOICES = (
    ('', '--------'),
    (True, 'Completo'),
    (False, 'Incompleto')
)

class OrdenCompraBusqueda(Form):
    rucproveedor = forms.CharField(label='RUC PROVEEDOR:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'rucproveedor'}),required=False)
    numorden = forms.CharField(label='NUMERO DE ORDEN:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'numorden'}),required=False)
    fechaorden = forms.DateField(label='FECHA:',
        widget=DateInput(attrs={'class':'form-control','id':'fechaorden'}),required=False)
    estado = forms.CharField(label='ESTADO:',
        widget=forms.Select(choices = TRUE_FALSE_CHOICES, attrs={'class':'form-select','id':'estado'}),required=False)

class EditarCompra(ModelForm):
    class Meta:
        model = Compra_prov
        fields = ('imagen_factura_compra','estado', 'detaller_entrega')
        widgets = {
            'estado':forms.Select(choices = TRUE_FALSE_CHOICES,attrs={'class':'form-select form-select-sm'}),
            'imagen_factura_compra':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'detaller_entrega':forms.Textarea(attrs={'class':'form-control'}),
        }


class DateFormSearch(Form):
    fecha = forms.DateTimeField(label='FECHA CIERRE:',
        widget=DateInput(attrs={'class':'form-control form-date', 'id':'fechabusqueda'}),required=False)


class NuevaCaja(ModelForm):
    class Meta:
        model = Caja_diaria
        fields = ('__all__')

#LIBRO DIARIO
class LibroDiarioBusqueda(Form):
    fecha = forms.DateField(label='FECHA:',
        widget=DateInput(attrs={'class':'form-control','id':'fecha'}),required=False)
    tipo = forms.CharField(label='TIPO:',
        widget=forms.TextInput(attrs={'class':'form-control','id':'tipo'}),required=False)

#SERVICIOS
class AgregarServicio(ModelForm):
    class Meta:
        model = Servicios
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control form-control'}),
            'contratista':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
        }

#ORDEN DE SERVICIO
class AgregarOrdenServicio(ModelForm):
    class Meta:
        model = Orden_compra_servicio
        fields = '__all__'
        widgets = {
            'trabajador':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'fecha_orden_servicio':forms.DateInput(attrs={'class':'form-control'}),
        }

class AgregarServicioEnOrdenCompra(ModelForm):
    class Meta:
        model = Servicio_compra
        fields = '__all__'
        widgets = {
            'contratista':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'orden_compra':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'fecha_compra':forms.DateInput(attrs={'class':'form-control'}),
            'fecha_inicio':forms.DateInput(attrs={'class':'form-control'}),
            'fecha_fin':forms.DateInput(attrs={'class':'form-control'}),
        }

    
#PRODUCCION 
NINGUNO = 'No Iniciado'
PROCESO = 'En proceso'
TERMINADO = 'Terminado'
SALIENDO = 'Saliendo'

PROCESOSPROD = [
    ('', '---------'),
    (NINGUNO, 'No Iniciado'),
    (PROCESO, 'En proceso'),
    (TERMINADO, 'Terminado'),
    (SALIENDO, 'Saliendo')
]

class ProduccioBusqueda(Form):
    fecha_inicio = forms.DateField(label='FECHA DE INICIO:',
        widget=DateInput(attrs={'class':'form-control','id':'fecha_inicio'}),required=False)
    fecha_fin = forms.DateField(label='FECHA DE FIN:',
        widget=DateInput(attrs={'class':'form-control','id':'fecha_fin'}),required=False)
    estado = forms.CharField(label='ESTADO:',
        widget=forms.Select(choices=PROCESOSPROD,attrs={'class':'form-select','id':'estado'}),required=False)
    

