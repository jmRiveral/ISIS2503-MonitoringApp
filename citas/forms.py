from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'estudiante',
            'horario',
            'psicologo',
            'ubicacion',
        ]

        labels = {
            'estudiante' : 'Estudiante',
            'horario' : 'Horario',
            'psicologo' : 'Psicologo',
            'ubicacion' : 'Ubicacion',
        }
