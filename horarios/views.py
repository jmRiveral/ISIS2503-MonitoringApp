from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import HorarioForm
from .logic.horario_logic import get_horarios, create_horario
from django.contrib.auth.decorators import login_required
#from monitoring.auth0backend import getRole

def horario_list(request):
    horarios = get_horarios()
    context = {
        'horario_list': horarios
    }
    return render(request, 'Horario/horarios.html', context)

#@login_required
def horario_create(request):
    #role = getRole(request)
    #if role == "Psicologo" or role == "Administrador":
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
    #else:
        #return HttpResponse("Unauthorized User")