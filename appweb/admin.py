from django.contrib import admin
from .models import Categorias, Cliente, PedidoDetalle, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria','precio')
    search_fields = ('nombre','categoria__nombre')
    list_editable = ('precio',)
    
admin.site.register(Categorias)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(PedidoDetalle)



