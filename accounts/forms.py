from django import forms
# Importar las funciones de base de datos
from API.conexion_bd import (
    consultar_credenciales_usuario
)
from .utilities import (
    crear_sesion,
    crear_sesion_con_token
)

class CustomLoginForm(forms.Form):
    run = forms.CharField(
        required=True,
        label="RUN",
        max_length=12,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'RUN (ej: 12345678-9)'
        })
    )
    password = forms.CharField(
        required=True,
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Contraseña'
        })
    )
    # captcha = CaptchaField()  # Descomenta si tienes django-simple-captcha instalado

    def clean(self):
        cleaned_data = super().clean()
        run = cleaned_data.get('run')
        password = cleaned_data.get('password')
        
        if run and password:
            # NO hay que pasarle el cursor manualmente
            credenciales_validas = consultar_credenciales_usuario(run, password)
            if not credenciales_validas:
                raise forms.ValidationError("RUN o contraseña incorrectos.")
        
        return cleaned_data
    
    def get_cleaned_data(self, request=None):
        """
        🔥 PUNTO DE AUTENTICACIÓN 🔥
        """
        if self.is_valid():
            datos_limpios = {
                'run': self.cleaned_data['run'].strip(),
                'password': self.cleaned_data['password'],
            }
            
            # Si se pasa request, crear sesión Django
            if request:
                session_id = crear_sesion(request, datos_limpios['run'])
                datos_limpios['session_id'] = session_id
            else:
                # Si no hay request, crear token personalizado
                token = crear_sesion_con_token(datos_limpios['run'])
                datos_limpios['token'] = token
            
            return datos_limpios
        return None
