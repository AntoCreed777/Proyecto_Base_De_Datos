from django.shortcuts import render
from API.conexion_bd import *


def login(request):
    return render(request, 'login.html')

def bdd_test(request):

    
    query = query_asistencia(1)

    return render(request, 'bdd_test.html', {'query': query})
