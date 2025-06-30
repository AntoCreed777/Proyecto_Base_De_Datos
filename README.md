# Proyecto Base de Datos
## Integrantes del grupo
- [Valeria Paulette Quiroga Carrere](https://github.com/vq00001) **(2023453609)**
- [Antonio Jesus Benavides Puentes](https://github.com/AntoCreed777) **(2023455954)**
- [Lucas Daniel Morales Oyanedel](https://github.com/Falling-Bridge) **(2023441490)**
- [Pablo Esteban Villagran Hermanns](https://github.com/Pvilla14) **(2023439231)**

## Tecnologías utilizadas en el proyecto

<div align="center">

### Herramientas de desarrollo y control de versiones
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,github,vscode&perline=5" />
</a>

### Base de datos y lenguaje de programación
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=postgres,python&perline=5" />
</a>

### Framework utilizado
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=django&perline=5" />
</a>

</div>

## Requisitos previos

- Python 3 instalado
- Git Bash, WSL, macOS Terminal, o cualquier terminal compatible con bash

## Instalación y configuración

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/AntoCreed777/Proyecto_Base_De_Datos
   cd Proyecto_Base_De_Datos
   ```

2. **Crea un entorno virtual llamado `venv`:**
   ```bash
   python3 -m venv venv
   ```

3. **Inicializa el entorno virtual e instala las dependencias:**
   ```bash
   source init_venv.sh
   ```
   El script detecta automáticamente tu sistema operativo y activa el entorno virtual correctamente en Windows, Linux o macOS.

> [!NOTE]
> - Si el script no se ejecuta por permisos (en Linux/macOS), asígnale permisos de ejecución:
>   ```bash
>   chmod +x init_venv.sh
>   ```
> - En Windows, si tienes problemas, puedes activar el entorno manualmente y luego instalar las dependencias:
>   ```powershell
>   .\venv\Scripts\Activate.ps1
>   pip install -r requirements.txt
>   ```

> [!WARNING]
> Si en linux no se ejecuta el script, intente con el siguiente comando antes de volver a intentarlo
> ``` bash
> dos2unix init_venv.sh
> ```

## Solución a problemas comunes durante la Instalación

<details>
  <summary>Error al instalar psycopg2</summary>

Si encuentras el siguiente error al intentar instalar las dependencias del proyecto:

```bash
Error: pg_config executable not found.
```

Esto ocurre porque `psycopg2` requiere que las bibliotecas de desarrollo de PostgreSQL estén instaladas en el sistema. Sigue estos pasos para solucionarlo según tu sistema operativo:

#### **Linux (Debian/Ubuntu)**
1. Instala las dependencias necesarias:
   
    ```bash
    sudo apt update
    sudo apt install -y libpq-dev python3-dev
    ````

2. Vuelve a instalar las dependencias del proyecto:
   
    ```bash
    pip install -r requirements.txt
    ```

#### **Linux (Fedora/RHEL/CentOS)**

1. Instala las dependencias necesarias:

    ```bash
    sudo dnf install -y postgresql-devel python3-devel
    ```

2. Vuelve a instalar las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

#### **macOS**

1. Si usas Homebrew, instala PostgreSQL:

    ```bash
    brew install postgresql
    ```

2. Vuelve a instalar las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

#### **Alternativa: Usar `psycopg2-binary`**

Si no puedes instalar las bibliotecas mencionadas o necesitas una solución rápida, puedes instalar la versión binaria de `psycopg2`:

```bash
pip install psycopg2-binary
```

> **Nota:** Esta versión es adecuada para desarrollo, pero no se recomienda para entornos de producción.

Con estas soluciones, deberías poder instalar `psycopg2` y continuar con la configuración del proyecto. Si el problema persiste, revisa que tu entorno virtual esté correctamente activado y que las dependencias estén actualizadas.
</details>

## Importar la base de datos PostgreSQL

Para utilizar el programa es necesario hacer la conexion con nuestra base de datos, que en este caso es local.  

1. Primero descargar el programa pgAdmin4 en este link [Descargar PgAdmin](https://www.pgadmin.org/download/). Para el proceso de instalacion ver [este video](https://www.youtube.com/watch?v=w9ax9-s2jbE).

2. Luego necesitaremos crear una base de datos para el proyecto. 
[Ver explicación en video](https://www.youtube.com/watch?v=A72owYF4m_c). Usar los valores de abajo al momento de crearla.


En el archivo `/Proyecto_Base_De_Datos/settings.py`, asegúrate de configurar:

```python
NAME =     "Proyecto-BDD"
USER =     "postgres"
PASSWORD = "tu_contraseña_en_PgAdmin4"
```

## Comandos previos

Antes de iniciar el servidor, es necesario aplicar las migraciones de la base de datos para asegurar que la estructura esté actualizada. 

Ejecuta los siguientes comandos:
```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```
Esto preparará la base de datos para el correcto funcionamiento del proyecto.

Luego, para poblar la base de datos con datos de prueba ejecutar:

```bash
python3 manage.py populate_db
```

En el caso de querer eliminar los datos se puede usar el comando: 
```bash
python3 manage.py clear_db
```

## Ejecución del proyecto

Para iniciar el servidor de desarrollo de Django, ejecuta:

```bash
python3 manage.py runserver
```

Esto levantará el servidor en `http://127.0.0.1:8000/` por defecto.

> [!NOTE]
> Si el puerto 8000 ya está en uso o tienes algún conflicto, puedes cambiar el puerto por cualquier otro disponible agregándolo al comando. Por ejemplo, para usar el puerto 8080:
> ```bash
> python3 manage.py runserver 8080
> ```
> También puedes especificar la IP y el puerto:
> ```bash
> python3 manage.py runserver 0.0.0.0:8080
> ```
