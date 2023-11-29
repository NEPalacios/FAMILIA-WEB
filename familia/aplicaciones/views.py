from django.shortcuts import render
from django.http import HttpResponse


# def inicio_view(xx):
#     return HttpResponse("BIENVENIDOS, ESTA ES UNA PAGINA DE INICIO SOBRE MIS FAMILIARES: ")

# def padres_view(xx):
#     return HttpResponse("ELLOS SON MIS PADRES: ")

# def hermanos_view(xx):
#     return HttpResponse("ELLOS SON MIS HERMANOS: ")



# familia/views.py

def inicio_view(xx):
    return render(xx, 'aplicaciones/inicio.html')

def padres_view(xx):
    return render(xx, 'aplicaciones/padres.html')

def hermanos_view(xx):
    return render(xx, 'aplicaciones/hermanos.html')

def mascotas_view(xx):
    return render(xx, 'aplicaciones/mascotas.html')
