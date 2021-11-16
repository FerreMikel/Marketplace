from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views import View
from django.http import Http404
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
        productos = Producto.objects.filter(categoria=categoria.pk).all()
        for producto in productos:
            imagenes = Imagen.objects.filter(producto=producto.pk).all()
            producto.imagen = imagenes.first()
        return render(request, 'category.html', {'categoria': categoria, 'productos': productos})


class FabricanteV(View):
    def get(self, request, slug_fabricante):
        fabricante = get_object_or_404(Fabricante, slug=slug_fabricante)
        productos = Producto.objects.filter(fabricante=fabricante.pk).all()
        for producto in productos:
            imagenes = Imagen.objects.filter(producto=producto.pk).all()
            producto.imagen = imagenes.first()
        return render(request, 'manufacturer.html', {'fabricante': fabricante, 'productos': productos})


class Categorias(View):
    def get(self, request):
        categorias = get_list_or_404(Categoria)
        for categoria in categorias:
            productos = Producto.objects.filter(
                categoria=categoria.pk).all()[:4]
            for producto in productos:
                producto.imagen = (Imagen.objects.filter(
                    producto=producto.pk).all()).first()
            categoria.productos = productos
        return render(request, 'categories.html', {'categorias': categorias})
