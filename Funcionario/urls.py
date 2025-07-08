from django.urls import path
from .views import *

urlpatterns = [
    path('', ver_links, name='links'),
    path('asignaturas_docente/', ver_asignaturas_docente, name='asignaturas_docente'),
    path('asignaturas_curso/', ver_asignaturas_y_docente_curso, name='asignaturas_curso'),
    path('crear_alumno/', añadir_alumno, name='añadir_alumno'),
    path('notas_asignatura/', ver_notas_asignatura, name='ver notas')
]