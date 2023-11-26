from django.urls import path
from django.http import HttpResponse
from .views import inicio_view, padres_view, hermanos_view


# urlpatterns = [
#     path("inicio/", inicio_view),    
#     path("padres/", padres_view),
#     path("hermanos/", hermanos_view),
# ]
# familia/urls.py


urlpatterns = [
    path('inicio/', inicio_view, name='inicio'),
    path('padres/', padres_view, name='padres'),
    path('hermanos/', hermanos_view, name='hermanos'),
]
