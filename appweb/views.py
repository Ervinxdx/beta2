from django.shortcuts import get_object_or_404, render,redirect
from .models import Producto ,Categorias,Cliente
from .carrito import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.
"""VISTAS PARA EL CATALOGO DE PRODUCTOS"""
def index(request):
    listaProducto = Producto.objects.all()
    listaCategorias = Categorias.objects.all()
    context = {
        'productos' : listaProducto,
        'categorias' : listaCategorias,
    }
    return render(request,'index.html', context)


#VISTA PARA FILTRAR PRODUCTOS POR CATEGORIA
def productosCategoria(request,categoria_id):
    objCategoria = Categorias.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()
    
    listaCategorias = Categorias.objects.all()
    
    context = {
        'categorias': listaCategorias,
        'productos' : listaProductos
    }
    return render(request,'index.html',context)



#Busqueda de productos por input type search

def productosPorNombre(request):
    nombre = request.POST['nombre']
    
    listaProductos = Producto.objects.filter(nombre__contains=nombre)
    listaCategorias = Categorias.objects.all()
    
    context = {
        'categorias': listaCategorias,
        'productos': listaProductos
    }
    return render(request,'index.html', context)

#VISTAS PARA E LCARRITO DE COMPRAS
def carritoDeCompras(request):
    return render(request,'carrito.html')

#VISTA PARA EL REGISTRO 
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


from .forms import ClienteForm

def crearUsuario(request):
    if request.method == 'POST':
        dataUsuario = request.POST['nuevoUsuario']
        dataPassword = request.POST['nuevoPassword']
        
        nuevoUsuaio = User.objects.create_user(username=dataUsuario, password=dataPassword)
        if nuevoUsuaio is not None: #SE VERFICA SI NO ES VACIO
            login(request,nuevoUsuaio)
            return redirect('/cuenta')
        
        
    return render(request,'login.html')


def cuentaUsuario(request):
    try:
        
        clienteEditar = Cliente.objects.get(usuario= request.user)
        
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email,
            'direccion':clienteEditar.direccion,
            'telefono': clienteEditar.telefono,
            'dni':clienteEditar.dni,
            'fecha_nacimiento':clienteEditar.fecha_nacimiento
        }
    except:
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email
        }
        
        
    formCliente = ClienteForm(dataCliente)
    
    context = {
        'formCliente':formCliente
    }
    
    return render(request,'cuenta.html',context)


def actualizarCliente(request):
    mensaje = ""
    
    if request.method == "POST":
        formCliente = ClienteForm(request.POST)
        if formCliente.is_valid():
            dataCliente = formCliente.cleaned_data  #PREPARA PARA EVNIAR A LA BASE DE DATOS
            #actualizar usuario
            actUsuario = User.objects.get(pk=request.user.id)
            actUsuario.first_name = dataCliente["nombre"]
            actUsuario.last_name = dataCliente["apellidos"]
            actUsuario.email = dataCliente["email"]
            actUsuario.save()
            
            #registrar cliente
            
            nuevoCliente  = Cliente()
            nuevoCliente.usuario = actUsuario
            nuevoCliente.dni = dataCliente["dni"]
            nuevoCliente.direccion = dataCliente["direccion"]
            nuevoCliente.telefono = dataCliente["telefono"]
            nuevoCliente.sexo = dataCliente["sexo"]
            nuevoCliente.fecha_nacimiento = dataCliente["fecha_nacimiento"]
            nuevoCliente.save()
            
            mensaje = "Datos registrados"
    context = {
        'mensaje':mensaje,
        'formCliente':formCliente,
    }        
        
    return render(request,'cuenta.html',context)

def loginUsuario(request):
    paginaDestino = request.GET.get('next',None)
    context= {
        'destino':paginaDestino,
    }
    
    if request.method == 'POST':
        dataUsuario = request.POST['usuario']
        dataPassword = request.POST['password']
        dataDestino = request.POST['destino']
        
        usuarioAuth = authenticate(request,username=dataUsuario,password=dataPassword)
        if usuarioAuth is not None:
            login(request,usuarioAuth)
            
            if dataDestino != 'None':
                return redirect(dataDestino)
                  
            
            return redirect('/cuenta')
        else:
            context = {
            'mensajeError' :'Datos incorrectos' 
            }
    return render(request,'login.html',context)


def logoutUsuario(request):
    logout(request)
    return render(request,'login.html')


    




    

def productoDetalle(request,producto_id):
    objProducto = get_object_or_404(Producto,pk=producto_id)
    # objProducto = Producto.objects.get(pk=producto_id)
    context = {
        'producto': objProducto
    }
    return render(request,'producto.html',context)

def agregarCarrito(request,producto_id):
    if request.method  == "POST":
        cantidad = int(request.POST['cantidad'])
    else:
        cantidad = 1
        
    
    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,cantidad)
    
    if request.method == 'GET':
        return redirect('/')
    
    return render(request,'carrito.html')


def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.delete(objProducto)
    
    return render(request,'carrito.html')

def limpiarCarrito(request):
        carritoProducto = Cart(request)
        carritoProducto.clear()
        
        return render(request,'carrito.html')
    



#REGISTRAR PEDIDO PERO CON AUTENTICACION
@login_required(login_url='/login')
def registrarPedido(request):
    try:
        
        clienteEditar = Cliente.objects.get(usuario= request.user)
        
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email,
            'direccion':clienteEditar.direccion,
            'telefono': clienteEditar.telefono,
            'dni':clienteEditar.dni,
            'fecha_nacimiento':clienteEditar.fecha_nacimiento
        }
    except:
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email
        }
        
        
    formCliente = ClienteForm(dataCliente)
    
    context = {
        'formCliente':formCliente
    }
    
    return render(request,'pedido.html', context)