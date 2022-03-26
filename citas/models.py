from django.db import models
from estudiantes.models import Estudiante

class Cita(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
    # horario = models.ForeignKey(Horario, on_delete=models.CASCADE, default=None)
    # psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, default=None)
    ubicacion = models.CharField(max_length=50)

    # dateTime pasa a ser atributo de Horario
    # dateTime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return '{}'.format(self.ubicacion)
