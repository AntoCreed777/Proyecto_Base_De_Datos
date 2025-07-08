from django.utils import timezone
import uuid
import hashlib

def crear_sesion(request, cleaned_run: str):
    """
    Crea una sesión personalizada para el usuario autenticado.
    
    OPCIÓN 1: Usando sesiones nativas de Django (Recomendado)
    """
    # Limpiar sesión anterior si existe
    if hasattr(request, 'session'):
        request.session.flush()
    
    # Crear nueva sesión
    request.session['usuario_run'] = cleaned_run
    request.session['usuario_autenticado'] = True
    request.session['fecha_login'] = timezone.now().isoformat()
    request.session['session_id'] = str(uuid.uuid4())
    
    # Configurar duración de la sesión (opcional)
    request.session.set_expiry(3600)  # 1 hora
    
    return request.session.session_key

def crear_sesion_con_token(cleaned_run: str):
    """
    OPCIÓN 2: Crear un token personalizado (sin usar Django sessions)
    """
    # Generar token único
    timestamp = str(timezone.now().timestamp())
    data = f"{cleaned_run}:{timestamp}"
    token = hashlib.sha256(data.encode()).hexdigest()
    
    session_data = {
        'token': token,
        'run': cleaned_run,
        'created_at': timezone.now(),
        'expires_at': timezone.now() + timezone.timedelta(hours=1)
    }
    
    # TODO: Guardar session_data en tu base de datos
    # guardar_token_sesion(session_data)
    
    return token

def verificar_sesion(request):
    """
    Verifica si el usuario tiene una sesión válida
    """
    return (
        request.session.get('usuario_autenticado', False) and
        request.session.get('usuario_run') is not None
    )

def cerrar_sesion(request):
    """
    Cierra la sesión del usuario
    """
    request.session.flush()

def obtener_usuario_sesion(request):
    """
    Obtiene el RUN del usuario de la sesión actual
    """
    if verificar_sesion(request):
        return request.session.get('usuario_run')
    return None