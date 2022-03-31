from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import HorarioForm
from .logic.horario_logic import get_horarios, create_horario

def estudiante_list(request):
    horarios = get_horarios()
    context = {
        'horario_list': horarios
    }
    return render(request, 'Horario/horario.html', context)

def horario_create(request):
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            create_horario(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created horario')
            return HttpResponseRedirect(reverse('horarioCreate'))
        else:
            print(form.errors)
    else:
        form = HorarioForm()

    context = {
        'form': form,
    }
    return render(request, 'Horario/horarioCreate.html', context)