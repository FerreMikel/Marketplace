from django.db.models import fields
from .models import Valoracion
from django import forms
from django.utils.translation import ugettext_lazy as _


class ValoracionForm(forms.ModelForm):
    class Meta:
        model = Valoracion
        fields = ['username', 'texto']
        