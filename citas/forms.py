from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'estudiante',
            'ubicacion',
            'dateTime',
        ]

        labels = {
            'estudiante' : 'Estudiante',
            'ubicacion' : 'Ubicacion',
            'dateTime' : 'Date Time',
        }
