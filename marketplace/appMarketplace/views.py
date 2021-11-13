from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views import View
from .models import Caracteristica, Categoria, Producto, Fabricante, Imagen

# Create your views here.


class Inicio(View):
    def get(self, request):
        return render(request, 'index.html')


class ProductoV(View):
    def get(self, request, slug_fabricante, slug_producto):
        fabricante = get_object_or_404(Fabricante, slug=slug_fabricante)
        producto = get_object_or_404(
            Producto, slug=slug_producto, fabricante=fabricante.pk)
        imagenes = Imagen.objects.filter(producto=producto.pk).all()
        caracteristicas = Caracteristica.objects.filter(
            producto=producto.pk).all()
        return render(request, 'product.html', {'producto': producto, 'imagenes': imagenes, 'caracteristicas': caracteristicas})


class CategoriaV(View):
    def get(self, request, slug_categoria):
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        return render(request, 'category.html', {'categoria': categoria})


class FabricanteV(View):
    def get(self, request, slug_fabricante):
        fabricante = get_object_or_404(Fabricante, slug=slug_fabricante)
        return render(request, 'manufacturer.html', {'fabricante': fabricante})


class Categorias(View):
    def get(self, request):
        categorias = get_list_or_404(Categoria)
        return render(request, 'categories.html', {'categorias': categorias})
