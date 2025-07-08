from django.shortcuts import render
from django.db import connection


# Create your views here.

def ver_horario_asignaturas_curso(request):
    resultados = []
    curso_id = None

    if request.method == 'POST':
        curso_id = request.POST.get('curso_id')

        if curso_id:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM proyecto_bd.obtener_horario_curso(%s);",[curso_id])
                resultados_raw = cursor.fetchall()

                resultados = [
                    {
                        'Nombre' : fila[3],
                        'Dia' : fila[0],
                        'Hora_inicio' : fila[1],
                        'Hora_fin' : fila[2]
                    }
                    for fila in resultados_raw
                ]
    return render(request, 'Docente/Horario_curso.html', {
        'horarios' : resultados,
        'curso_id' : curso_id
    })

def ver_asistencia_curso(request):
    resultados = []
    asignatura_id = None

    if request.method == 'POST':
        asignatura_id = request.POST.get('asignatura_id')

        if asignatura_id:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM proyecto_bd.obtener_asistencia_curso(%s);", [asignatura_id])
                resultados_raw = cursor.fetchall()

                resultados = [
                    {
                        'estudiante': fila[0],
                        'asistencia': fila[1],
                        'fecha': fila[2],
                        'hora': fila[3]
                    }
                    for fila in resultados_raw
                ]

    return render(request, 'Docente/Asistencia.html', {
        'asistencias': resultados,
        'asignatura_id': asignatura_id
    })




def ver_lista_curso(request):
    estudiantes = []
    curso_id = None
    if request.method == 'POST':
        curso_id = request.POST.get('curso_id')
        if curso_id:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM proyecto_bd.obtener_estudiantes_por_curso(%s);", [curso_id])
                resultados = cursor.fetchall()
                estudiantes = [fila[0] for fila in resultados]

    return render(request, 'Docente/Lista_Curso.html', {
        'estudiantes': estudiantes,
        'curso_id': curso_id
    })

def ver_links(request):
    return render(request, 'Docente/Pag_Docente.html')