from django.db import models
from estudiantes.models import Estudiante
from psicologos.models import Psicologo
from horarios.models import Horario

class Cita(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, default=None)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, default=None)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.tipo)

