from django import forms
from .models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            'start',
            'end',
        ]
        labels = {
            'start': 'Start',
            'end': 'End',
        }