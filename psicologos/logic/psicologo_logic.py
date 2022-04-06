from ..models import Psicologo

def get_psicologos():
    queryset = Psicologo.objects.all()
    return (queryset)

def create_psicologo(form):
    p = form.save()
    p.save()
    return ()