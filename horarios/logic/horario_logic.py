from ..models import Horario

def get_horarios():
    queryset = Horario.objects.all()
    return (queryset)

def create_horario(form):
    h = form.save()
    h.save()
    return ()