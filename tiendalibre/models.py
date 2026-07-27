from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50, unique=True)

    class meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering=["-nombre"]



    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos", blank=True, null=True)

    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField(max_length=200)
    stock=models.IntegerField()
    imagen=models.ImageField(upload_to="productos", null=True, blank=True)

    class meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        ordering=["-nombre"]

    def __str__(self):
        return self.nombre



    
    