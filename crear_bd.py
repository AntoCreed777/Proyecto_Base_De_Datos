import psycopg2, getpass
import sys

from proyecto_base_de_datos.settings import DATABASES
db = DATABASES['default']

def crear_bd():
    conn = psycopg2.connect(
        database="postgres", 
        user='postgres', 
        password=db['PASSWORD'], 
        host=db['HOST'],
        port= db['PORT'],
    )

    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    sql = '''CREATE database proyecto_base_de_datos''';

    #Creating a database
    cursor.execute(sql)
    print("Base de datos creada exitosamente.......")

    print('Creando tablas')

    #Closing the connection
    conn.close()
    cursor.close()

def crear_tablas(dir_archivo_create='./sql/create_tables.sql', dir_archivo_funciones='./sql/proyecto_consultas.sql'):
            
    ## obtener codigo de creacion de tablas sql
    archivo_codigo_sql = open(dir_archivo_create, 'r')
    lineas_codigo_sql = archivo_codigo_sql.readlines()

    codigo_sql = ''
    for linea in lineas_codigo_sql:
        codigo_sql += linea 

    # obtener codigo de creacion de funciones sql
    archivo_funciones_sql = open(dir_archivo_funciones, 'r')
    lineas_funciones_sql = archivo_funciones_sql.readlines()

    funciones_sql = ''
    for linea in lineas_funciones_sql:
        funciones_sql += linea 

    # conectarse a nueva bd

    print('Conectando a nueva bd')
    conn = psycopg2.connect(
        database=db['NAME'], 
        user='postgres', 
        password=db['PASSWORD'], 
        host=db['HOST'], 
        port= db['PORT'] 
    )

    conn.autocommit = True

    cursor = conn.cursor()
    print('Creando tablas')
    cursor.execute(codigo_sql)

    print('Creando funciones')
    cursor.execute(funciones_sql)

    conn.close()
    cursor.close()

    print('Termino de creacion de tablas')
    #Closing the connection

def poblar_bd(dir_archivo='./sql/proyecto_poblar.sql'):
    ## obtener codigo sql
    archivo_codigo_sql = open(dir_archivo, 'r')
    lineas_codigo_sql = archivo_codigo_sql.readlines()

    codigo_sql = ''
    for linea in lineas_codigo_sql:
        codigo_sql += linea 

    conn = psycopg2.connect(
        database=db['NAME'], 
        user='postgres', 
        password=db['PASSWORD'], 
        host=db['HOST'], 
        port= db['PORT']
    )

    conn.autocommit = True

    cursor = conn.cursor()
    print('Poblando tablas')
    cursor.execute(codigo_sql)

    conn.close()
    cursor.close()





option = ''
password = ''

if len(sys.argv) == 1:

    option = 'default'
    password = db['PASSWORD']
    

elif len(sys.argv) == 3:
    option = sys.argv[1]

if option == 'crear' or option == 2:
    crear_bd()
    crear_tablas()
elif option == 'poblar' or option == 3:
    poblar_bd()
elif option == 'default' or option == 1:
    crear_bd()
    crear_tablas()
    poblar_bd()

else:
    print(f'''USO: {sys.argv[0]} <modo> <contraseña_postgreSQL> 
        Modos disponibles: 
        - crear 
        - poblar
        - default (crear y poblar)
    ''')
