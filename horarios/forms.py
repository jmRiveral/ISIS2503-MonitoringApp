from django import forms
from .models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            'dateTime',
        ]
        labels = {
            'dateTime': 'Date Time',
        }