from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomLoginForm
from .utilities import (
    verificar_sesion,
    obtener_usuario_sesion,
    cerrar_sesion
)

def login_view(request):
    """
    Vista de login con manejo de sesiones
    """
    # Si ya está logueado, redirigir
    if verificar_sesion(request):
        messages.info(request, 'Ya tienes una sesión activa')
        return redirect('dashboard')  # Cambiar por la URL del inicio dependiendo del rol del usuario
    
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        
        if form.is_valid():
            datos = form.get_cleaned_data(request)  # Pasar request para crear sesión
            
            if datos:
                # Usuario autenticado exitosamente
                messages.success(request, f"¡Bienvenido! RUN: {datos['run']}")
                messages.info(request, f"Sesión iniciada: {datos.get('session_id', 'N/A')}")
                return redirect('dashboard')  # Cambiar por la URL del inicio dependiendo del rol del usuario
            else:
                messages.error(request, 'Error al procesar los datos de autenticación')
        else:
            # Mostrar errores específicos del formulario
            if form.non_field_errors():
                for error in form.non_field_errors():
                    messages.error(request, error)
            else:
                messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = CustomLoginForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    """
    Vista para cerrar sesión
    """
    usuario_run = obtener_usuario_sesion(request)
    cerrar_sesion(request)
    
    if usuario_run:
        messages.success(request, f'Sesión cerrada exitosamente. ¡Hasta luego {usuario_run}!')
    else:
        messages.info(request, 'Sesión cerrada')
    
    return redirect('login')

def dashboard_view(request):
    """
    Vista del dashboard (página principal después del login)
    """
    # Verificar si está logueado
    if not verificar_sesion(request):
        messages.warning(request, 'Debes iniciar sesión para acceder a esta página')
        return redirect('login')
    
    # Obtener datos del usuario de la sesión
    usuario_run = obtener_usuario_sesion(request)
    
    context = {
        'usuario_run': usuario_run,
        'session_id': request.session.get('session_id'),
        'fecha_login': request.session.get('fecha_login'),
        'title': 'Dashboard - Proyecto Base de Datos'
    }
    
    return render(request, 'accounts/dashboard.html', context)
