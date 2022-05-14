from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EstudianteForm
from .logic.estudiante_logic import get_estudiantes, create_estudiante
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def estudiante_list(request):
    role = getRole(request)
    if role == "Psicologo" or role == "Administrador":
        estudiantes = get_estudiantes()
        context = {
            'estudiante_list': estudiantes
        }
        return render(request, 'Estudiante/estudiantes.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def estudiante_create(request):
    role = getRole(request)
    if role == "Administrador":
        if request.method == 'POST':
            form = EstudianteForm(request.POST)
            if form.is_valid():
                create_estudiante(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created estudiante')
                return HttpResponseRedirect(reverse('estudianteCreate'))
            else:
                print(form.errors)
        else:
            form = EstudianteForm()

        context = {
            'form': form,
        }
        return render(request, 'Estudiante/estudianteCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")