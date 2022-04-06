from ..models import Estudiante

def get_estudiantes():
    queryset = Estudiante.objects.all()
    return (queryset)

def create_estudiante(form):
    e = form.save()
    e.save()
    return ()