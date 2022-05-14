from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import  PsicologoForm
from .logic.psicologo_logic import get_psicologos, create_psicologo
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def psicologo_list(request):
    role = getRole(request)
    if role == "Administrador":
        psicologos = get_psicologos()
        context = {
            'psicologo_list': psicologos
        }
        return render(request, 'Psicologo/psicologos.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def psicologo_create(request):
    role = getRole(request)
    if role == "Administrador":
        if request.method == 'POST':
            form = PsicologoForm(request.POST)
            if form.is_valid():
                create_psicologo(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created psicologo')
                return HttpResponseRedirect(reverse('psicologoCreate'))
            else:
                print(form.errors)
        else:
            form = PsicologoForm()

        context = {
            'form': form,
        }
        return render(request, 'Psicologo/psicologoCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")