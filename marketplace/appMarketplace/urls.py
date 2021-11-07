from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio.as_view(), name='index')
]
