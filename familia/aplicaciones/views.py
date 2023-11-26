from django.shortcuts import render
from django.http import request


# def inicio_view(xx):
#     return HttpResponse("BIENVENIDOS, ESTA ES UNA PAGINA DE INICIO SOBRE MIS FAMILIARES: ")

# def padres_view(xx):
#     return HttpResponse("ELLOS SON MIS PADRES: ")

# def hermanos_view(xx):
#     return HttpResponse("ELLOS SON MIS HERMANOS: ")



# familia/views.py

def inicio_view(request):
    return render(request, 'aplicaciones/inicio.html')

def padres_view(request):
    return render(request, 'aplicaciones/padres.html')

def hermanos_view(request):
    return render(request, 'aplicaciones/hermanos.html')
