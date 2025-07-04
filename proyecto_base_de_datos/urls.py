"""
URL configuration for proyecto_base_de_datos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import login
from Docente.views import ver_asistencia_curso, ver_lista_curso, ver_horario_asignaturas_curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('asistencia/', ver_asistencia_curso, name='asistencias'),
    path('Lista_curso/', ver_lista_curso, name='lista_curso'),
    path('horario_curso', ver_horario_asignaturas_curso, name='horario_curso'),
]
