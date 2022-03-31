from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EstudianteForm
from .logic.estudiante_logic import get_estudiantes, create_estudiante

def estudiante_list(request):
    estudiantes = get_estudiantes()
    context = {
        'estudiante_list': estudiantes
    }
    return render(request, 'Estudiante/horario.html', context)

def estudiante_create(request):
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