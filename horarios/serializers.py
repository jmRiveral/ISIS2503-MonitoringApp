from rest_framework import serializers
from . import models


class HorarioSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'time')
        model = models.Horario