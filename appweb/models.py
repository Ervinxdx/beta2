from django.db import models
from django.contrib.auth.models import User

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
    
class Cliente(models.Model):
    STATUS_CHOICES = (
    ("M", 'Masculino'),
    ("F",'Femenino')
    )
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    dni = models.CharField(max_length=8)
    sexo = models.CharField(max_length=1,choices=STATUS_CHOICES, default='M')
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.TextField()
    def __str__(self):
        return self.dni

class Pedido(models.Model):
    ESTADO_CHOICES=(
        ('0', 'solicitado'),
        ('1', 'pagado')
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    nro_pedido = models.CharField(max_length=20,null=True)
    monto_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    estado = models.CharField(max_length=1,default='0',choices=ESTADO_CHOICES)
    
    def __str__(self):
        return self.nro_pedido
    
class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT)    
    producto = models.ForeignKey(Producto,on_delete= models.RESTRICT)
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    
    
    def __str__(self):
        return self.pedido
    
    
    


    

