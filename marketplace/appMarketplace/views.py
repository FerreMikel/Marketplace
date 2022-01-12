
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views import View
from django.http import Http404
from .models import Caracteristica, Categoria, Producto, Fabricante, Imagen, Valoracion
from .forms import ValoracionForm
from django.http import HttpResponse

# Create your views here.


class Inicio(View):
    def get(self, request):
        indexContent = [{
            'title': "Orbea Ebike Wild FS",
            'subtitle': "Take back your wild.",
            'bgImageUrl': "https://www.todomountainbike.net/images/articles/2019/orbea-wild-fs-2020.jpg",
            'actionBtn': "VER BICICLETA",
            'link': "/orbea/ebike-wild"
        },
            {
            'title': "Trek",
            'subtitle': "Relentless progression",
            'bgImageUrl': "https://trek.scene7.com/is/image/TrekBicycleProducts/Carbon_Tech_Mold_16x9?$responsive-pjpg$&cache=on,on&wid=1920&hei=1440&fit=constrain,1",
            'actionBtn': "VER FABRICANTE",
            'link': "/trek"
        },
            {
            'title': "Niños",
            'subtitle': "Disfruta de la bici en familia",
            'bgImageUrl': "https://www.orbea.com/img/products/imagenes-menu/context-kids.jpg",
            'actionBtn': "VER CATEGORÍA",
            'link': "/categorias/ninos"
        }]
        return render(request, 'index.html', {'indexContent': indexContent})


class ProductoV(View):
    def post(self, request, slug_fabricante, slug_producto):
        fabricante = get_object_or_404(Fabricante, slug=slug_fabricante)
        producto = get_object_or_404(
            Producto, slug=slug_producto, fabricante=fabricante.pk)
        imagenes = Imagen.objects.filter(producto=producto.pk).all()
        caracteristicas = Caracteristica.objects.filter(
            producto=producto.pk).all()
        valoraciones = Valoracion.objects.filter(producto = producto.pk).all()
        if(Valoracion.objects.filter(producto = producto.pk).exists()):
            valoracionId = Valoracion.objects.filter(producto = producto.pk).all().last().pk
        else:
            valoracionId = Valoracion.objects.all().last().pk
            ##Valoracion.objects.all().last.pk
        
        form = ValoracionForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            comentario = form.cleaned_data['texto']
            
            estrellas = 5
            productoPk = producto.pk
            val = Valoracion(valoracionId+1 ,productoPk, estrellas, username, comentario)
            val.save()       
                
        
        return render(request, 'product.html',  {'producto': producto, 'imagenes': imagenes, 'caracteristicas': caracteristicas,'valoraciones': valoraciones, 'form': form})
        

    def get(self, request, slug_fabricante, slug_producto):
    
        fabricante = get_object_or_404(Fabricante, slug=slug_fabricante)
        producto = get_object_or_404(
            Producto, slug=slug_producto, fabricante=fabricante.pk)
        imagenes = Imagen.objects.filter(producto=producto.pk).all()
        caracteristicas = Caracteristica.objects.filter(
            producto=producto.pk).all()
        valoraciones = Valoracion.objects.filter(producto = producto.pk).all()
        form = ValoracionForm()
        
        return render(request, 'product.html', {'producto': producto, 'imagenes': imagenes, 'caracteristicas': caracteristicas,'valoraciones': valoraciones, 'form': form})
   
            


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
