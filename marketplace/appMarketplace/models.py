from django.db import models

# Create your models here. wenas tardes


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre


class Fabricante(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    sitioWeb = models.URLField()
    logoURL = models.URLField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre


class Caracteristica(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    precio = models.IntegerField()
    caracteristicas = models.ManyToManyField(Caracteristica)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre


class Imagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.producto.nombre


class Valoracion(models.Model):
    producto =  models.ForeignKey(Producto, on_delete=models.CASCADE)
    estrellas = models.FloatField()
    username = models.CharField(max_length=30)
    texto = models.CharField(max_length=250)

    def __str__(self):
        return self.producto.nombre