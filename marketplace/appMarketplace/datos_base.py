# app/datos_base.py

def categorias(request):
    from .models import Categoria
    return {'categorias': Categoria.objects.all()}
