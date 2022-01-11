from django.contrib import admin

# Register your models here.

from .models import Categoria, Caracteristica, Fabricante, Producto, Imagen, Valoracion

admin.site.register(Categoria)
admin.site.register(Caracteristica)
admin.site.register(Fabricante)
admin.site.register(Producto)
admin.site.register(Imagen)
admin.site.register(Valoracion)
