import datetime
from django.db import connection
import psycopg2
from psycopg2 import sql

from proyecto_base_de_datos.settings import DATABASES
db = DATABASES['default']

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
def query_id_asignaturas(cursor, ID_Curso, nombre_asignatura=None):
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
def query_estudiante():
    pass
    
@query_to_db
def query_asistencia(cursor, ID_Asignatura):

    # print( cursor.execute(f'SELECT * FROM proyecto_bd.obtener_asistencia_curso({ID_Asignatura})').fetchone())
    cursor.execute(f'SELECT * FROM proyecto_bd.obtener_asistencia_curso({ID_Asignatura})')
    results = cursor.fetchall()    
    asistencia = crear_diccionarios(['Nombre Estudiante', 'Asistencia', 'Fecha', 'Hora'], results)
    return asistencia

    
