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

## Comandos previos

Antes de iniciar el servidor, es necesario aplicar las migraciones de la base de datos para asegurar que la estructura esté actualizada. 

Ejecuta el siguiente comando:

```bash
python3 manage.py migrate
```
Esto preparará la base de datos para el correcto funcionamiento del proyecto.

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
