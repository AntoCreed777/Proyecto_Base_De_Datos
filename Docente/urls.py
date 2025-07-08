from django.urls import path
from .views import *

urlpatterns = [
    path('', ver_links, name='links'),
    path('asistencia/', ver_asistencia_curso, name='asistencias'),
    path('Lista_curso/', ver_lista_curso, name='lista_curso'),
    path('horario_curso/', ver_horario_asignaturas_curso, name='horario_curso'),
]