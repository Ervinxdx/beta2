"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('productosPorCategoria/<int:categoria_id>', views.productosCategoria,name='productoPorCategoria'),
    path('productosPorNombre', views.productosPorNombre,name='productosPorNombre'),
    path('producto/<int:producto_id>', views.productoDetalle, name='producto'),
    path('carrito',views.carritoDeCompras, name='carrito'),
    path('agregarCarrito/<int:producto_id>',views.agregarCarrito, name='agregarCarrito'),
    path('eliminarProductoCarrito/<int:producto_id>', views.eliminarProductoCarrito,name='eliminarProductoCarrito'),
    path('limpiarCarrito',views.limpiarCarrito, name='limpiarCarrito'),
    path('crearUsuario',views.crearUsuario,name='crearUsuario'),
    path('cuenta',views.cuentaUsuario,name='cuentaUsuario'),
    path('actualizarCliente',views.actualizarCliente,name='actualizarCliente'),
    path('login',views.loginUsuario,name='loginUsuario'),
    path('logout',views.logoutUsuario,name='logoutUsuario'),
    path('registrarPedido', views.registrarPedido,name='registrarPedido')
    
]


