from django import forms
from .models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            'name',
        ]
        labels = {
            'name': 'Name',
        }