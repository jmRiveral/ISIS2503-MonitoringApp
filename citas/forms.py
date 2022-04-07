from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'estudiante',
            'psicologo',
            'horario',
            'tipo'
        ]
        labels = {
            'estudiante' : 'Estudiante',
            'psicologo' : 'Psicologo',
            'horario' : 'Horario',
            'tipo': 'Tipo'
        }