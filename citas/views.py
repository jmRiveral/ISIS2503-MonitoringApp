from django.shortcuts import render
from .forms import CitaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_cita import create_cita, get_citas

def cita_list(request):
    citas = get_citas()
    context = {
        'cita_list': citas
    }
    return render(request, 'Cita/citas.html', context)

def cita_create(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            create_cita(form)
            messages.add_message(request, messages.SUCCESS, 'Cita create successful')
            return HttpResponseRedirect(reverse('citaCreate'))
        else:
            print(form.errors)
    else:
        form = CitaForm()

    context = {
        'form': form,
    }

    return render(request, 'Cita/citaCreate.html', context)