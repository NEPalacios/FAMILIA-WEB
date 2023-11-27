# tarea numero 3
1. python -m django startproject familia #crea carpeta 'familia' con contenido django

2. python manage.py startapp aplicaciones # dentro de la carpeta 'familia' correr el comando. crea la carpeta 'aplicaciones'.

3. python manage.py runserver #servidor ya funcionando

4. crear archivo urls.py en 'aplicaciones'. Cargarle un url donde va atender la bienvenida o index.
    importar httpresponse #from django.http import HttpResponse#

4. A) registrar 'aplicaciones' en settings.py\familia

    B) crear la funcion que va servir la bienvenida 
     #def inicio_view(xx):
    return HttpResponse("Inicio")#

    C) urls.py\familia\ importar INCLUDE. E incluir en la linea las aplicaciones de 'aplicaciones'
    #path('aplicaciones/', include('aplicaciones.urls')),#

5.  cortar los views hechos en urls.py\aplicaciones y pegarlos en views.py\aplicaciones. #from django.http import httresponse\\\\  from views import *VIEWS* #


6. crear los archivos.html que vayan a responder en cada view. Ya que ahora los vamos a cambiar desde una carpeta nueva TEMPLATES\APLICACIONES\TEMPLATES

  EJ:     return render(request, 'aplicaciones/inicio.html') ###archivo views.py###
    ###urlpatterns = [
    path('inicio/', inicio_view, name='inicio'),###