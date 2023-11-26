from django.urls import path
from django.http import HttpResponse

def inicio_view(xx):
    return HttpResponse("BIENVENIDOS, ESTA ES UNA PAGINA DE INICIO SOBRE MIS FAMILIARES: ")

def padres_view(xx):
    return HttpResponse("ELLOS SON MIS PADRES: ")

def hermanos_view(xx):
    return HttpResponse("ELLOS SON MIS HERMANOS: ")






urlpatterns = [
    path("inicio/", inicio_view),    
    path("padres/", padres_view),
    path("hermanos/", hermanos_view),
]
