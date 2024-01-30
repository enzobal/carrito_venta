# from django.db import models

# # Create your models here.
# class Producto(models.Model):
#     nombre= models.CharField(max_length=64)
#     categoria= models.CharField(max_length=32)
#     precio= models.IntegerField()

#     def __str__(self):
#         return f'{self.nombre} -> {self.precio}' 


from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    descripcion = models.TextField()
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'



class Producto2(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos2/', null=True, blank=True)
    descripcion = models.TextField()
    precio = models.IntegerField()
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'


# es de index
class Producto3(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos3/', null=True, blank=True)
    descripcion = models.TextField()
    precio = models.IntegerField()
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'