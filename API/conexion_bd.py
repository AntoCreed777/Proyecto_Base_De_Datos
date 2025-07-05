import datetime
from enum import Enum
from django.db import connection
import psycopg2
from psycopg2 import sql

from proyecto_base_de_datos.settings import DATABASES
db = DATABASES['default']

# class Funciones_SQL(Enum):
#     NOTAS_POR_ASIGNATURA = {'nombre': obtener_notas_asignatura, 'argumentos': []},



def query_to_db(view_func):
    
    def wrapper(*args, **kwargs):
        try:
            connection = psycopg2.connect(
                dbname=db['NAME'],
                user=db['USER'],
                password=db['PASSWORD'],
                host=db['HOST'],
                port=db['PORT']
            )

            cursor = connection.cursor()
            # Execute the view function with the database connection
            results = view_func(cursor, *args, **kwargs)
            connection.close()
            cursor.close()
            return results
        
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
            return None
        
    return wrapper

def crear_diccionarios(columnas, resultados): 

    diccionarios = []
    
    for res in resultados:
        diccionario = {}
        for i, columna in enumerate(columnas):

            value = res[i]

            if isinstance(value, datetime.date):
                print(f'Value: {value} \n Type: {type(value)}')
                value = value.strftime('%Y-%m-%d')

            elif isinstance(value, datetime.time):
                print(f'Value: {value} \n Type: {type(value)}')
                value = value.strftime('%H:%M')
            
            diccionario[columna] = value

        diccionarios.append(diccionario)

    return diccionarios

# Funcion que consulta los ID de las asignaturas de un curso
# Si no se especifica el nombre de la asignatura, devuelve todos los ID de las asignaturas del curso
@query_to_db
def obtener_id_asignaturas(cursor, ID_Curso, nombre_asignatura=None):
    query = None
    attributes = ['ID_Asignatura']
    if nombre_asignatura:
        query = f'''
        SELECT ID_Asignatura
        FROM proyecto_bd.Asignatura
        WHERE ID_Curso = {ID_Curso} AND Nombre_asignatura = '{nombre_asignatura}';
        '''
    else: 
        query = f'''
        SELECT ID_Asignatura, Nombre_asignatura
        FROM proyecto_bd.Asignatura
        WHERE ID_Curso = {ID_Curso};
        '''

        attributes.append('Nombre_asignatura')

    cursor.execute(query)
    results = cursor.fetchall()
    return crear_diccionarios(attributes, results)

@query_to_db
def obtener_estudiante(cursor, Nombre_estudiante):
    pass
    
@query_to_db
def obtener_asistencia(cursor, ID_Asignatura):

    # print( cursor.execute(f'SELECT * FROM proyecto_bd.obtener_asistencia_curso({ID_Asignatura})').fetchone())
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_asistencia_curso({ID_Asignatura})')
    results = cursor.fetchall()    
    asistencia = crear_diccionarios(['Nombre Estudiante', 'Asistencia', 'Fecha', 'Hora'], results)
    return asistencia

@query_to_db
def obtener_numero_telefonico(cursor, RUN_Persona):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_numero_telefonico({RUN_Persona})')
    results = cursor.fetchall()    
    num_tel = crear_diccionarios(['Número de Teléfono'], results)
    return num_tel

@query_to_db
def obtener_asignaturas_y_docentes_curso(cursor, ID_Curso):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_asignaturas_y_docentes_curso({ID_Curso})')
    results = cursor.fetchall()    
    diccionario = crear_diccionarios(['Asignatura', 'Docente'], results)
    return diccionario


@query_to_db
def obtener_estudiantes_por_curso(cursor, ID_Curso):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_estudiantes_por_curso({ID_Curso})')
    results = cursor.fetchall()    
    diccionario = crear_diccionarios(['Estudiante'], results)
    return diccionario

@query_to_db
def obtener_horario_curso(cursor, ID_Curso):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_horario_curso({ID_Curso})')
    results = cursor.fetchall()    
    diccionario = crear_diccionarios(['Asignatura','Día','Hora Inicio','Hora Término'] ,results)
    return diccionario

@query_to_db
def obtener_horario_curso(cursor, ID_Curso):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_horario_curso({ID_Curso})')
    results = cursor.fetchall()    
    diccionario = crear_diccionarios(['Asignatura','Día','Hora Inicio','Hora Término'] ,results)
    return diccionario

@query_to_db
def obtener_notas_asignatura(cursor, ID_Asignatura):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_notas_asignatura({ID_Asignatura})')
    results = cursor.fetchall()    
    diccionario = crear_diccionarios(['Estudiante', 'Nota'] ,results)
    return diccionario


@query_to_db
def obtener_apoderados_estudiante(cursor, RUN_Estudiante):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_apoderados_estudiante({RUN_Estudiante})')
    results = cursor.fetchall()    
    diccionario = crear_diccionarios([
        'Apoderado(a)', 
        'Teléfono', 
        'Relación', 'Lugar de Trabajo', 
        'Profesión'
    ] ,results)
    return diccionario  


@query_to_db
def obtener_asistencia_curso(cursor, ID_Curso):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_asistencia_curso({ID_Curso})')
    results = cursor.fetchall()    
    diccionario = crear_diccionarios(['Estudiante', 'Asistencia', 'Fecha', 'Hora'], results)
    return diccionario


@query_to_db
def obtener_asistencia_curso(cursor, ID_Curso):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_asistencia_curso({ID_Curso})')
    results = cursor.fetchall()    
    diccionario = crear_diccionarios(['Estudiante', 'Asistencia', 'Fecha', 'Hora'], results)
    return diccionario

@query_to_db
def obtener_info_familia(cursor, ID_Estudiante):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_info_familia({ID_Estudiante})')
    results = cursor.fetchall()    
    diccionario = crear_diccionarios([

        'ID Familia',
        'Nombre Familia',
        'Cuantos Trabajan',
        'Ocupación Padres',
        'Número Integrantes',
        'Cantidad Dormitorios',
        'Cantidad Baños',
        'Baños Compartidos',
        'Energía',
        'Tipo de Agua',
        'Tipo de Construcción',
        'Propiedad',
        'Estado Marital Padres',
        'Estado de Vida Padres',
        'Ingresos Mensuales'
    ], results)
    return diccionario

@query_to_db
def obtener_docente_dicta_asignatura(cursor, RUN_Docente):
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_docente_dicta_asignatura({RUN_Docente})')
    results = cursor.fetchall()    
    diccionario = crear_diccionarios(['ID Asignatura', ' Asignatura', 'Curso'], results)
    return diccionario