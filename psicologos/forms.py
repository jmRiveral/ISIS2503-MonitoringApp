from django import forms
from .models import Psicologo

class PsicologoForm(forms.ModelForm):
    class Meta:
        model = Psicologo
        fields = [
            'name',
        ]
        labels = {
            'name': 'Name',
        }