from django.shortcuts import render
from .models import Producto

def index(request):
    productos = Producto.objects.all()
    context = {
        'productos' : productos
    }
    return render(request, 'index.html',context)

# Create your views here.
