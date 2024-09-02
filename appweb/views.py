from django.shortcuts import get_object_or_404, render,redirect
from .models import Producto ,Categorias
from .carrito import Cart

# Create your views here.
"""VISTAS PARA EL CATALOGO DE PRODUCTOS"""
def index(request):
    listaProducto = Producto.objects.all()
    listaCategorias = Categorias.objects.all()
    print(listaProducto)
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
    
    