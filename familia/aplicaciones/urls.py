from django.urls import path
from django.shortcuts import render

def inicio_view(request):
    return "BIENVENIDOS"

urlpatterns = [
    path("inicio/", inicio_view)    
]
