from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('horario/', views.horario_list, name='horarioList'),
    path('horariocreate/', csrf_exempt(views.horario_create), name='horarioCreate'),
]