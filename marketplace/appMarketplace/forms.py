from django.db.models import fields
from .models import Valoracion
from django import forms
from django.utils.translation import ugettext_lazy as _


class ValoracionForm(forms.ModelForm):
    class Meta:
        model = Valoracion
        fields = ['username', 'texto']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder' : 'Nombre de usuario','class' : 'myForm nameArea'}),
            'texto': forms.Textarea(attrs={'placeholder' : 'Escribe aquí tu comentario', 'class' : 'myForm myTextArea'}),
        }
        labels = {
            'username' : '',
            'texto' : '',
        }
    
    ##username = forms.CharField(max_length=30)
    ##comentario = forms.CharField(widget=forms.Textarea())
    ##estrellas = forms.IntegerField()
    
    
   ## class Meta:
      ##  model = Valoracion
    ##    fields = ("__all__")
     