from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio.as_view(), name='index'),
    path('categorias', views.Categorias.as_view(), name='categories'),
    path('categorias/<slug:slug_categoria>',
         views.CategoriaV.as_view(), name='category'),
    path('<slug:slug_fabricante>',
         views.FabricanteV.as_view(), name='manufacturer'),
    path('<slug:slug_fabricante>/<slug:slug_producto>',
         views.ProductoV.as_view(), name='product'),
]
