from django.db import models

class Horario(models.Model):

    dateTime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return '{}'.format(self.dateTime)

