from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('horario/', views.psicologos_list, name='psicologoList'),
    path('psicologocreate/', csrf_exempt(views.psicologo_create), name='psicologoCreate'),
]