from django import forms
from .models import Contenido

class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = '__all__'