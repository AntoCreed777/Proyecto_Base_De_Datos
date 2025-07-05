# 🗄️ Proyecto Base de Datos

<div align="center">

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Un sistema de gestión académica desarrollado con Django y PostgreSQL

</div>

## 👥 Integrantes del Equipo

| Nombre | GitHub | Matrícula |
|--------|--------|-----------|
| Valeria Paulette Quiroga Carrere | [@vq00001](https://github.com/vq00001) | 2023453609 |
| Antonio Jesus Benavides Puentes | [@AntoCreed777](https://github.com/AntoCreed777) | 2023455954 |
| Lucas Daniel Morales Oyanedel | [@Falling-Bridge](https://github.com/Falling-Bridge) | 2023441490 |
| Pablo Esteban Villagran Hermanns | [@Pvilla14](https://github.com/Pvilla14) | 2023439231 |

## 📋 Tabla de Contenidos

- [🚀 Inicio Rápido](#-inicio-rápido)
- [📋 Requisitos Previos](#-requisitos-previos)
- [⚙️ Instalación](#️-instalación)
- [🔧 Configuración](#-configuración)
- [🗄️ Base de Datos](#️-base-de-datos)
- [▶️ Ejecución](#️-ejecución)
- [🛠️ Solución de Problemas](#️-solución-de-problemas)
- [🤝 Contribuir](#-contribuir)

## 🚀 Inicio Rápido

```bash
# Clonar el repositorio
git clone https://github.com/AntoCreed777/Proyecto_Base_De_Datos
cd Proyecto_Base_De_Datos

# Configurar entorno virtual
source init_venv.sh

# Configurar base de datos PostgreSQL (ver sección Base de Datos)
# Editar proyecto_base_de_datos/settings.py con tus credenciales

# Preparar base de datos
python3 manage.py migrate
python3 manage.py populate_db

# Ejecutar servidor
python3 manage.py runserver
```

## 📋 Requisitos Previos

- **Python 3.8+** 
- **PostgreSQL** (con pgAdmin4 recomendado)
- **Git**
- Terminal compatible con bash (Git Bash, WSL, Terminal de macOS/Linux)

## ⚙️ Instalación

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/AntoCreed777/Proyecto_Base_De_Datos
cd Proyecto_Base_De_Datos
```

### 2️⃣ Configurar Entorno Virtual

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar e instalar dependencias automáticamente
source init_venv.sh
```

<details>
<summary>🔧 Activación manual del entorno</summary>

**Linux/macOS:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
pip install -r requirements.txt
```

</details>

## 🔧 Configuración

### Configuración de la Base de Datos

Edita el archivo `proyecto_base_de_datos/settings.py` y configura la conexión a PostgreSQL:

```python
# Configuración de la base de datos en settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'proyecto_bd',              # Nombre de tu base de datos
        'USER': 'tu_usuario_postgresql',    # Tu usuario de PostgreSQL
        'PASSWORD': 'tu_contraseña',        # Tu contraseña de PostgreSQL
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Ejemplo de configuración

```python
# Ejemplo real de configuración
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'proyecto_bd',
        'USER': 'postgres',
        'PASSWORD': 'mipassword123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Otras configuraciones importantes

También puedes modificar en `settings.py`:

```python
# Configuración regional
TIME_ZONE = 'America/Santiago'
LANGUAGE_CODE = 'es-cl'

# Para desarrollo local
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
```

> ⚠️ **Importante:** Para producción, asegúrate de cambiar `DEBUG = False` y configurar `ALLOWED_HOSTS` apropiadamente.

## 🗄️ Base de Datos

### Configuración de PostgreSQL

1. **Instalar pgAdmin4:** [Descargar aquí](https://www.pgadmin.org/download/)
   - 📺 [Video tutorial de instalación](https://www.youtube.com/watch?v=w9ax9-s2jbE)

2. **Crear base de datos:**
   - 📺 [Video tutorial](https://www.youtube.com/watch?v=A72owYF4m_c)
   - Usar los valores configurados en tu archivo `.env`

### Preparar la Base de Datos



```bash
# Crear y poblar base de datos
python3 crear_bd.py

# Crear y aplicar migraciones 
python3 manage.py makemigrations
python3 manage.py migrate

```

### Comandos Útiles

```bash
# Crear superusuario
python3 manage.py createsuperuser
```

## ▶️ Ejecución

```bash
# Iniciar servidor de desarrollo
python3 manage.py runserver
```

El servidor estará disponible en: **http://127.0.0.1:8000/**

### Opciones Adicionales

```bash
# Usar puerto personalizado
python3 manage.py runserver 8080

# Permitir acceso desde cualquier IP
python3 manage.py runserver 0.0.0.0:8000
```

## 🛠️ Solución de Problemas

<details>
<summary>❌ Error al instalar psycopg2</summary>

### Problema
```bash
Error: pg_config executable not found.
```

### Solución por Sistema Operativo

**🐧 Linux (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install -y libpq-dev python3-dev
pip install -r requirements.txt
```

**🐧 Linux (Fedora/RHEL/CentOS):**
```bash
sudo dnf install -y postgresql-devel python3-devel
pip install -r requirements.txt
```

**🍎 macOS:**
```bash
brew install postgresql
pip install -r requirements.txt
```

**🚀 Solución Rápida (Desarrollo):**
```bash
pip install psycopg2-binary
```

> ⚠️ `psycopg2-binary` es solo para desarrollo, no para producción.

</details>

<details>
<summary>🐧 Script no ejecuta en Linux</summary>

### Problema
El script `init_venv.sh` no se ejecuta por permisos o formato de líneas.

### Solución
```bash
# Corregir formato de líneas
dos2unix init_venv.sh

# Dar permisos de ejecución
chmod +x init_venv.sh

# Ejecutar
source init_venv.sh
```

</details>

<details>
<summary>🔌 Error de conexión a la base de datos</summary>

### Problema
Django no puede conectarse a PostgreSQL.

### Verificaciones
1. **PostgreSQL está ejecutándose:**
   ```bash
   # Linux/macOS
   sudo systemctl status postgresql
   
   # Windows: Verificar en Servicios
   ```

2. **Credenciales correctas en `settings.py`:**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nombre_correcto_bd',
           'USER': 'usuario_correcto',
           'PASSWORD': 'contraseña_correcta',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Base de datos existe:**
   - Verificar en pgAdmin4 que la base de datos existe
   - El usuario tiene permisos de acceso

</details>

---

<div align="center">

**Desarrollado con ❤️ por el equipo de Base de Datos**

</div>
