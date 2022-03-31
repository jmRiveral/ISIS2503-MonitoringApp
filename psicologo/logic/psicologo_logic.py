from ..models import Horario

def get_horarios():
    queryset = Horario.objects.all()
    return (queryset)

def create_horario(form):
    e = form.save()
    e.save()
    return ()