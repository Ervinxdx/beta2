from django.db import models

class Categorias(models.Model):
    nombre = models.CharField( max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    # fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) :
        return self.nombre
    class Meta:
        verbose_name_plural = 'Categorias'
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categorias,on_delete=models.RESTRICT) #on_delete=models.RESTRICT SIRVE PARA QUE NO PERMITA ELIMINAR UNA CATEGORIA SI ES QUE HAY PRODUCTOS.
    nombre = models.CharField(max_length=200) #maximo 500 caracteres
    descripcion = models.TextField(null=True) #null = True / permite dejar en blanco
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='producots',blank=True)
    
    def __str__(self):
        return self.nombre



