from django.shortcuts import render
from API.conexion_bd import *

<<<<<<< HEAD
def login(request):
    return render(request, 'login.html')

def bdd_test(request):

    
    query = query_asistencia(1)

    return render(request, 'bdd_test.html', {'query': query})
=======
>>>>>>> cbdc2338c39e5c7c516219a725881e733cd46a13
