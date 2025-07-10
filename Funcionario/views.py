from django.shortcuts import render
from django.db import connection

#ñ = Ã±

# Create your views here.

def arreglar_palabras(palabras):
    datos_arreglados = []
    for item in palabras:
        corregido = item[1].encode('latin1').decode('utf-8')
        datos_arreglados.append((item[0], corregido))
    return datos_arreglados

def ver_asignaturas_docente(request):
    resultados = []
    docente_id = None

    if request.method == 'POST':
        docente_id = request.POST.get('docente_id')

        if docente_id:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM proyecto_bd.obtener_docente_dicta_asignatura(%s);",[docente_id])
                resultados_raw = cursor.fetchall()

                resultados = [
                    {
                        'Id' : fila[0],
                        'nombre' : fila[1],
                        'curso' : fila[2],
                    }
                    for fila in resultados_raw
                ]
    return render(request, 'Funcionario/Asignaturas_Docente.html', {
        'asignaturas' : resultados,
        'docente_id' : docente_id
    })

def ver_asignaturas_y_docente_curso(request):
    resultados = []
    curso_id = None

    if request.method == 'POST':
        curso_id = request.POST.get('curso_id')

        if curso_id:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM proyecto_bd.obtener_asignaturas_y_docentes_curso(%s);",[curso_id])
                resultados_raw = cursor.fetchall()

                resultados = [
                    {
                        'NAsignatura' : fila[0],
                        'NDocente' : fila[1],
                    }
                    for fila in resultados_raw
                ]
    return render(request, 'Funcionario/Asignatura_y_docente_curso.html', {
        'asignaturas_docentes' : resultados,
        'docente_id' : curso_id
    })

def obtener_generos():
    with connection.cursor() as gen:
        gen.execute("SELECT * FROM proyecto_bd.Genero")
        return gen.fetchall()
    
def obtener_nacionalidad():
    with connection.cursor() as naci:
        naci.execute("SELECT * FROM proyecto_bd.Nacionalidad")
        return naci.fetchall()
    
def obtener_religion():
    with connection.cursor() as rel:
        rel.execute("SELECT * FROM proyecto_bd.Religion")
        return rel.fetchall()
    
def obtener_familias():
    with connection.cursor() as fam:
        fam.execute("SELECT ID_Familia, Nombre_Familia FROM proyecto_bd.Info_Familia")
        return fam.fetchall()

def obtener_cursos():
    with connection.cursor() as cursor:
        cursor.execute(''' 
            SELECT c.ID_Curso, c.Grado, c.Letra FROM proyecto_bd.Curso c;
        ''')
        return cursor.fetchall()

def añadir_alumno(request): 
    print(obtener_generos())
    estudiante = []

    if request.method == 'POST':

        accion = request.POST.get('accion')

        print("recibimos", accion)

        rut_alumno = request.POST.get('rut_al')
        primer_nombre = request.POST.get('nombre_1_al')
        segundo_nombre = request.POST.get('nombre_2_al')
        primer_apellido = request.POST.get('apellido_1_al')
        segundo_apellido = request.POST.get('apellido_2_al')
        fecha_nac = request.POST.get('fecha_nac')
        matricula = request.POST.get('matricula_al')
        estado_academico = request.POST.get('estado_academico_al')
        anio_ingreso = request.POST.get('anio_ingreso')
        fecha_matricula = request.POST.get('fecha_mat')
        semestre_ingreso = request.POST.get('semestre_ing')
        genero = request.POST.get('genero_al')
        religion = request.POST.get('religion_al')
        nacionalidad = request.POST.get('nacionalidad_al')
        contrasena = request.POST.get('password_al')
        curso_id = request.POST.get('curso')

        with connection.cursor() as crear_per:
            crear_per.execute("""
            INSERT INTO proyecto_bd.Persona 
            (RUN_Persona, ContraseÃ±a, Fecha_de_nacimiento, ID_Genero, ID_Nacionalidad, ID_Religion) 
            VALUES (%s, %s, %s, %s, %s, %s)""",
            [rut_alumno, contrasena,fecha_nac, genero,nacionalidad, religion]) 

        with connection.cursor() as crear_nom:
            crear_nom.execute("""
            INSERT INTO proyecto_bd.Nombre_Completo 
            (RUN_Persona, Primer_nombre, Segundo_nombre, Apellido_paterno, Apellido_materno) 
            VALUES (%s, %s, %s, %s, %s)""",
            [rut_alumno,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido])

        with connection.cursor() as crear_al:
            crear_al.execute("""
            INSERT INTO proyecto_bd.Estudiante(
            RUN_Persona, 
            ID_Familia, 
            AÃ±o_de_Ingreso, 
            Numero_de_Matricula,
            Foto,
            Fecha_Matricula,
            Estado_Academico,
            Semestre_de_Ingreso
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) 
            RETURNING RUN_Persona, ID_Familia, AÃ±o_de_Ingreso, Numero_de_Matricula, Foto, Fecha_Matricula, Estado_Academico, Semestre_de_Ingreso
            """,
            [rut_alumno, id_familia, anio_ingreso, matricula, None, fecha_matricula, estado_academico, semestre_ingreso])

            estudiante_raw = crear_al.fetchone()

        with connection.cursor() as ver_al:
            ver_al.execute("SELECT * FROM proyecto_bd.obtener_nombre_completo(%s)",[rut_alumno])
            nombre_al = ver_al.fetchone()[0]

        with connection.cursor() as cursor:
            
            cursor.execute("INSERT INTO proyecto_bd.estudiantepertenececurso (RUN_Estudiante, ID_Curso)   VALUES (%s, %s)", [rut_alumno, curso_id])

        estudiante = [{
            'rut': estudiante_raw[0],
            'nombre': nombre_al,
            'id_F': estudiante_raw[1],
            'anio_i': estudiante_raw[2],
            'matricula': estudiante_raw[3],
            'fecha_m': estudiante_raw[5],
            'estado_a': estudiante_raw[6],
            'semestre_i': estudiante_raw[7],
        }]

    return render(request, 'Funcionario/Ingresar_Estudiantes.html',{
        'estudiante' : estudiante,
        'generos' : arreglar_palabras(obtener_generos()),
        'nacionalidades' : arreglar_palabras(obtener_nacionalidad()),
        'religiones' : arreglar_palabras(obtener_religion()),
        'familias' : arreglar_palabras(obtener_familias()),
        'cursos':obtener_cursos()
    })

def ver_links(request):
    return render(request, 'Funcionario/Pag_Funcionario.html')


