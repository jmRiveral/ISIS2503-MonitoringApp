from django.db import models
from estudiantes.models import Estudiante

class Cita(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
    ubicacion = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return '{}'.format(self.ubicacion)
