from django.core.management.base import BaseCommand
from datetime import date, time
from API.models import (
    Genero, Nacionalidad, Religion, Persona, Nombre_Completo, 
    Numero_Telefonico, Lugar_de_Residencia, Apoderado, Docente,
    Info_Familia, Estudiante, Sala, Curso, Asignatura, Evaluacion,
    Bloque_Horario, Asistencia, Justificacion, Actividad_Extracurricular,
    Reporte_Accidente, Anotacion, estudianteTOMAactividad, estudianteRINDEevaluacion,
    estudiantePERTENECEcurso, apoderadoRESPONSABLEDEestudiante, docenteDICTAasignatura,
    docenteACARGOactividad, actividadESTAENELbloquehorario, asignaturaESTAENbloquehorario
)

class Command(BaseCommand):
    help = 'Poblar base de datos con datos de ejemplo'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Eliminar todos los datos existentes antes de poblar',
        )
        parser.add_argument(
            '--clear-only',
            action='store_true',
            help='Solo eliminar datos sin poblar nuevos',
        )

    def clear_database(self):
        """Elimina todos los datos de la base de datos en el orden correcto"""
        self.stdout.write('🗑️  Eliminando datos existentes...')
        
        # Eliminar en orden inverso para respetar las foreign keys
        # Primero las tablas de relaciones
        self.stdout.write('Eliminando relaciones...')
        asignaturaESTAENbloquehorario.objects.all().delete()
        actividadESTAENELbloquehorario.objects.all().delete()
        docenteACARGOactividad.objects.all().delete()
        docenteDICTAasignatura.objects.all().delete()
        apoderadoRESPONSABLEDEestudiante.objects.all().delete()
        estudiantePERTENECEcurso.objects.all().delete()
        estudianteRINDEevaluacion.objects.all().delete()
        estudianteTOMAactividad.objects.all().delete()
        
        # Luego las tablas que dependen de otras
        self.stdout.write('Eliminando registros dependientes...')
        Anotacion.objects.all().delete()
        Reporte_Accidente.objects.all().delete()
        Actividad_Extracurricular.objects.all().delete()
        Justificacion.objects.all().delete()
        Asistencia.objects.all().delete()
        Bloque_Horario.objects.all().delete()
        Evaluacion.objects.all().delete()
        Asignatura.objects.all().delete()
        Curso.objects.all().delete()
        Sala.objects.all().delete()
        Estudiante.objects.all().delete()
        Info_Familia.objects.all().delete()
        Docente.objects.all().delete()
        Apoderado.objects.all().delete()
        
        # Luego las tablas de información personal
        self.stdout.write('Eliminando información personal...')
        Lugar_de_Residencia.objects.all().delete()
        Numero_Telefonico.objects.all().delete()
        Nombre_Completo.objects.all().delete()
        Persona.objects.all().delete()
        
        # Finalmente las tablas de catálogos
        self.stdout.write('Eliminando catálogos...')
        Religion.objects.all().delete()
        Nacionalidad.objects.all().delete()
        Genero.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS('✅ Todos los datos han sido eliminados exitosamente')
        )

    def handle(self, *args, **options):
        self.stdout.write('Empezando a poblar la base de datos...')
        
        # Verificar opciones de limpieza
        if options['clear'] or options['clear_only']:
            self.clear_database()
            
        if options['clear_only']:
            self.stdout.write(
                self.style.SUCCESS('✅ Proceso completado: Solo se eliminaron los datos')
            )
            return
        
        # Create Genero records
        self.stdout.write('Creando registros de Genero...')
        generos = [
            'Masculino',
            'Femenino', 
            'No Binario',
            'Otro'
        ]
        
        genero_objects = []
        for nombre in generos:
            genero, created = Genero.objects.get_or_create(nombre=nombre)
            genero_objects.append(genero)
            if created:
                self.stdout.write(f'Created Genero: {nombre}')

        # Create Nacionalidad records
        self.stdout.write('Creando registros de Nacionalidad...')
        nacionalidades = [
            'Chile',
            'Argentina',
            'Perú',
            'Brasil',
            'Uruguay'
        ]
        
        nacionalidad_objects = []
        for pais in nacionalidades:
            nacionalidad, created = Nacionalidad.objects.get_or_create(pais=pais)
            nacionalidad_objects.append(nacionalidad)
            if created:
                self.stdout.write(f'Creada la nacionalidad: {pais}')

        # Create Religion records
        self.stdout.write('Creando registros de Religion...')
        religiones = [
            'Católica',
            'Evangélica',
            'Judía',
            'Musulmana',
            'Atea',
            'Agnóstica'
        ]
        
        religion_objects = []
        for nombre_religion in religiones:
            religion, created = Religion.objects.get_or_create(nombre_religion=nombre_religion)
            religion_objects.append(religion)
            if created:
                self.stdout.write(f'Created Religion: {nombre_religion}')

        # Create Persona records
        self.stdout.write('Creando registros de Persona...')
        personas_data = [
            ('12345670-k', date(2001, 1, 1), genero_objects[0], nacionalidad_objects[0], religion_objects[0]),  # APODERADO
            ('12345671-k', date(2002, 2, 2), genero_objects[1], nacionalidad_objects[1], religion_objects[1]),  # APODERADO
            ('12345672-k', date(2003, 3, 3), genero_objects[2], nacionalidad_objects[2], religion_objects[2]),  # APODERADO
            ('12345673-k', date(2004, 4, 4), genero_objects[3], nacionalidad_objects[3], religion_objects[3]),  # APODERADO
            ('12345674-k', date(1980, 5, 5), genero_objects[0], nacionalidad_objects[4], religion_objects[4]),  # DOCENTE
            ('12345675-k', date(1981, 6, 6), genero_objects[1], nacionalidad_objects[0], religion_objects[0]),  # DOCENTE
            ('12345676-k', date(1990, 7, 7), genero_objects[2], nacionalidad_objects[1], religion_objects[1]),  # FUNCIONARIO
            ('12345677-k', date(1991, 8, 8), genero_objects[3], nacionalidad_objects[2], religion_objects[2]),  # FUNCIONARIO
            ('12345678-k', date(2005, 9, 9), genero_objects[0], nacionalidad_objects[3], religion_objects[3]),  # ESTUDIANTE
            ('12345679-k', date(2006, 10, 10), genero_objects[1], nacionalidad_objects[4], religion_objects[4]), # ESTUDIANTE
        ]
        
        persona_objects = []
        for run, fecha_nacimiento, genero, nacionalidad, religion in personas_data:
            persona, created = Persona.objects.get_or_create(
                RUN=run,
                defaults={
                    'fecha_nacimiento': fecha_nacimiento,
                    'id_genero': genero,
                    'id_nacionalidad': nacionalidad,
                    'id_religion': religion
                }
            )
            persona_objects.append(persona)
            if created:
                self.stdout.write(f'Creada la Persona: {run}')

        # Create Nombre_Completo records
        self.stdout.write('Creando registros de Nombre_Completo...')
        nombres_data = [
            (persona_objects[0], 'Valentina', 'Maria', 'González', 'Pérez'),      # APODERADO
            (persona_objects[1], 'Mateo', 'José', 'Muñoz', 'Rojas'),             # APODERADO
            (persona_objects[2], 'Isidora', 'Fernanda', 'Díaz', 'Fernández'),    # APODERADO
            (persona_objects[3], 'Benjamín', 'Alejandro', 'Soto', 'Morales'),    # APODERADO
            (persona_objects[4], 'Florencia', 'Ignacia', 'Silva', 'Castillo'),   # DOCENTE
            (persona_objects[5], 'Tomás', 'Andrés', 'Ramírez', 'Gutiérrez'),     # DOCENTE
            (persona_objects[6], 'Camila', 'Carmela', 'Torres', 'Reyes'),        # FUNCIONARIO
            (persona_objects[7], 'Lucas', 'Sebastian', 'Martínez', 'Vargas'),    # FUNCIONARIO
            (persona_objects[8], 'Josefa', 'Amanda', 'Contreras', 'López'),      # ESTUDIANTE
            (persona_objects[9], 'Agustín', 'Raúl', 'Espinoza', 'Herrera'),     # ESTUDIANTE
        ]
        
        for persona, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno in nombres_data:
            nombre_completo, created = Nombre_Completo.objects.get_or_create(
                RUN_persona=persona,
                defaults={
                    'primer_nombre': primer_nombre,
                    'segundo_nombre': segundo_nombre,
                    'apellido_paterno': apellido_paterno,
                    'apellido_materno': apellido_materno
                }
            )
            if created:
                self.stdout.write(f'Nombre_Completo creado para: {persona.RUN}')

        # Create Numero_Telefonico records
        self.stdout.write('Creando registros de Numero_Telefonico...')
        telefonos_data = [
            (persona_objects[0], 56, 2, 12345678),
            (persona_objects[1], 56, 2, 23456789),
            (persona_objects[2], 56, 2, 34567890),
            (persona_objects[3], 56, 2, 45678901),
            (persona_objects[4], 56, 2, 56789012),
            (persona_objects[5], 56, 2, 67890123),
            (persona_objects[6], 56, 2, 78901234),
            (persona_objects[7], 56, 2, 89012345),
            (persona_objects[8], 56, 2, 90123456),
            (persona_objects[9], 56, 2, 11223344),
        ]
        
        for persona, codigo_pais, codigo_area, numero_unico in telefonos_data:
            telefono, created = Numero_Telefonico.objects.get_or_create(
                RUN_persona=persona,
                defaults={
                    'codigo_del_pais': codigo_pais,
                    'codigo_del_area': codigo_area,
                    'numero_unico': numero_unico
                }
            )
            if created:
                self.stdout.write(f'Numero_Telefonico creado para: {persona.RUN}')

        # Create Lugar_de_Residencia records
        self.stdout.write('Creando registros de Lugar_de_Residencia...')
        residencias_data = [
            (persona_objects[8], 'Región de O\'Higgins', 'Rancagua', 'Machalí', 'Calle San Martín', 9202, 909),
            (persona_objects[0], 'Región Metropolitana', 'Santiago', 'Providencia', 'Avenida Providencia', 1234, 101),
            (persona_objects[1], 'Región de Valparaíso', 'Valparaíso', 'Viña del Mar', 'Avenida Libertad', 5678, 202),
            (persona_objects[2], 'Región del Biobío', 'Concepción', 'Chiguayante', 'Calle Colón', 9101, 303),
            (persona_objects[3], 'Región de La Araucanía', 'Temuco', 'Padre Las Casas', 'Calle Balmaceda', 1121, 404),
            (persona_objects[4], 'Región de Los Lagos', 'Puerto Montt', 'Puerto Varas', 'Calle San Pedro', 3141, 505),
            (persona_objects[5], 'Región de Magallanes', 'Punta Arenas', 'Puerto Natales', 'Calle Costanera', 5161, 606),
            (persona_objects[6], 'Región de Antofagasta', 'Antofagasta', 'Calama', 'Calle Prat', 7181, 707),
            (persona_objects[7], 'Región de Coquimbo', 'La Serena', 'Coquimbo', 'Calle Balmaceda', 8191, 808),
            (persona_objects[9], 'Región del Maule', 'Talca', 'Curicó', 'Calle Libertador Bernardo O\'Higgins', 1023, 1010),
        ]
        
        for persona, region, ciudad, comuna, calle, numero_casa, numero_dpt in residencias_data:
            residencia, created = Lugar_de_Residencia.objects.get_or_create(
                RUN_persona=persona,
                defaults={
                    'region': region,
                    'ciudad': ciudad,
                    'comuna': comuna,
                    'calle': calle,
                    'numero_casa': numero_casa,
                    'numero_departamento': numero_dpt
                }
            )
            if created:
                self.stdout.write(f'Lugar_de_Residencia creado para: {persona.RUN}')

        # Create Apoderado records
        self.stdout.write('Creando registros de Apoderado...')
        apoderados_data = [
            (persona_objects[0], 'Contadora', 'Empresa ABC'),
            (persona_objects[1], 'Educador Diferencial', 'Instituto XYZ'),
            (persona_objects[2], 'Médica', 'Hospital Local'),
            (persona_objects[3], 'Secretario Académico', 'Universidad Nacional'),
        ]
        
        apoderado_objects = []
        for persona, profesion, lugar_trabajo in apoderados_data:
            apoderado, created = Apoderado.objects.get_or_create(
                RUN_persona=persona,
                defaults={
                    'profesion': profesion,
                    'lugar_de_trabajo': lugar_trabajo
                }
            )
            apoderado_objects.append(apoderado)
            if created:
                self.stdout.write(f'Apoderado creado: {persona.RUN}')

        # Create Docente records
        self.stdout.write('Creando registros de Docente...')
        docentes_data = [
            persona_objects[4],  # Florencia
            persona_objects[5],  # Tomás
        ]
        
        docente_objects = []
        for persona in docentes_data:
            docente, created = Docente.objects.get_or_create(RUN_persona=persona)
            docente_objects.append(docente)
            if created:
                self.stdout.write(f'Docente creado: {persona.RUN}')

        # Create Info_Familia records
        self.stdout.write('Creando registros de Info_Familia...')
        familias_data = [
            ('Familia González', 2, 'Ingeniero y Profesora', 4, 3, 2, True, 'red_electrica', 'llave_en_vivienda', 'casa_solida', 'propia', 'casados', 'ambos_vivos', 800000),
            ('Familia Muñoz', 1, 'Médico', 1, 2, 1, False, 'red_electrica', 'llave_en_vivienda', 'departamento', 'arrendada', 'convivientes', 'padre_fallecido', 600000),
        ]
        
        familia_objects = []
        for (nombre_familia, cuantos_trabajan, ocupacion_padres, numero_integrantes, 
             cantidad_dormitorios, cantidad_banos, banos_compartidos, energia, tipo_agua, 
             tipo_construccion, propiedad, estado_marital, estado_vida, ingresos_mensuales) in familias_data:
            
            familia, created = Info_Familia.objects.get_or_create(
                nombre_familia=nombre_familia,
                defaults={
                    'cuantos_trabajan': cuantos_trabajan,
                    'ocupacion_padres': ocupacion_padres,
                    'numero_integrantes': numero_integrantes,
                    'cantidad_dormitorios': cantidad_dormitorios,
                    'cantidad_banos': cantidad_banos,
                    'banos_compartidos': banos_compartidos,
                    'energia': energia,
                    'tipo_agua': tipo_agua,
                    'tipo_construccion': tipo_construccion,
                    'propiedad': propiedad,
                    'estado_marital_padres': estado_marital,
                    'estado_vida_padres': estado_vida,
                    'ingresos_mensuales': ingresos_mensuales
                }
            )
            familia_objects.append(familia)
            if created:
                self.stdout.write(f'Info_Familia creada: {nombre_familia}')

        # Create Estudiante records
        self.stdout.write('Creando registros de Estudiante...')
        estudiantes_data = [
            (persona_objects[8], familia_objects[0], 2020, '2020-001', date(2020, 1, 15), 'vigente', 1),
            (persona_objects[9], familia_objects[1], 2021, '2021-002', date(2021, 2, 20), 'vigente', 2),
        ]
        
        estudiante_objects = []
        for persona, familia, anio_ingreso, numero_matricula, fecha_matricula, estado_academico, semestre_ingreso in estudiantes_data:
            estudiante, created = Estudiante.objects.get_or_create(
                RUN_persona=persona,
                defaults={
                    'id_familia': familia,
                    'anio_ingreso': anio_ingreso,
                    'numero_de_matricula': numero_matricula,
                    'fecha_matricula': fecha_matricula,
                    'estado_academico': estado_academico,
                    'semestre_ingreso': semestre_ingreso
                }
            )
            estudiante_objects.append(estudiante)
            if created:
                self.stdout.write(f'Estudiante creado: {persona.RUN}')

        # Create Sala records
        self.stdout.write('Creando registros de Sala...')
        salas_data = [
            'Sala 101',
            'Sala 102',
            'Sala 103',
            'Sala 104',
            'Sala 105'
        ]
        
        sala_objects = []
        for nombre_sala in salas_data:
            sala, created = Sala.objects.get_or_create(nombre_sala=nombre_sala)
            sala_objects.append(sala)
            if created:
                self.stdout.write(f'Sala creada: {nombre_sala}')

        # Create Curso records
        self.stdout.write('Creando registros de Curso...')
        cursos_data = [
            (docente_objects[0], sala_objects[0], 2020, 1, 1, 'A'),
            (docente_objects[1], sala_objects[1], 2020, 2, 2, 'B'),
            (docente_objects[0], sala_objects[2], 2021, 1, 3, 'C'),
        ]
        
        curso_objects = []
        for docente, sala, anio, semestre, grado, letra in cursos_data:
            curso, created = Curso.objects.get_or_create(
                id_docente=docente,
                id_sala=sala,
                anio=anio,
                semestre=semestre,
                defaults={
                    'grado': grado,
                    'letra': letra
                }
            )
            curso_objects.append(curso)
            if created:
                self.stdout.write(f'Curso creado: {grado}{letra} - {anio}/{semestre}')

        # Create Asignatura records
        self.stdout.write('Creando registros de Asignatura...')
        asignaturas_data = [
            (curso_objects[0], 'Matemáticas'),
            (curso_objects[1], 'Lenguaje y Comunicación'),
            (curso_objects[2], 'Ciencias Naturales'),
            (curso_objects[0], 'Historia y Geografía'),
            (curso_objects[1], 'Educación Física'),
        ]
        
        asignatura_objects = []
        for curso, nombre_asignatura in asignaturas_data:
            asignatura, created = Asignatura.objects.get_or_create(
                id_curso=curso,
                nombre_asignatura=nombre_asignatura
            )
            asignatura_objects.append(asignatura)
            if created:
                self.stdout.write(f'Asignatura creada: {nombre_asignatura}')

        # Create Evaluacion records
        self.stdout.write('Creando registros de Evaluacion...')
        evaluaciones_data = [
            (docente_objects[0], asignatura_objects[0], date(2020, 3, 1), 0.3),
            (docente_objects[1], asignatura_objects[1], date(2020, 3, 2), 0.4),
            (docente_objects[0], asignatura_objects[2], date(2020, 3, 3), 0.2),
            (docente_objects[1], asignatura_objects[3], date(2020, 3, 4), 0.5),
        ]
        
        evaluacion_objects = []
        for docente, asignatura, fecha_evaluacion, ponderacion in evaluaciones_data:
            evaluacion, created = Evaluacion.objects.get_or_create(
                run_docente=docente,
                id_asignatura=asignatura,
                fecha_evaluacion=fecha_evaluacion,
                defaults={'ponderacion': ponderacion}
            )
            evaluacion_objects.append(evaluacion)
            if created:
                self.stdout.write(f'Evaluacion creada: {asignatura.nombre_asignatura} - {fecha_evaluacion}')

        # Create Bloque_Horario records
        self.stdout.write('Creando registros de Bloque_Horario...')
        bloques_data = [
            ('lunes', time(8, 0), time(10, 0)),
            ('lunes', time(10, 30), time(12, 30)),
            ('martes', time(8, 0), time(10, 0)),
            ('martes', time(10, 30), time(12, 30)),
            ('miercoles', time(8, 0), time(10, 0)),
            ('miercoles', time(10, 30), time(12, 30)),
            ('jueves', time(8, 0), time(10, 0)),
            ('jueves', time(10, 30), time(12, 30)),
            ('viernes', time(8, 0), time(10, 0)),
            ('viernes', time(10, 30), time(12, 30)),
        ]
        
        bloque_objects = []
        for dia, hora_inicio, hora_fin in bloques_data:
            bloque, created = Bloque_Horario.objects.get_or_create(
                dia=dia,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin
            )
            bloque_objects.append(bloque)
            if created:
                self.stdout.write(f'Bloque_Horario creado: {dia} {hora_inicio}-{hora_fin}')

        # Create Asistencia records
        self.stdout.write('Creando registros de Asistencia...')
        asistencias_data = [
            (estudiante_objects[0], asignatura_objects[0], 'presente', date(2020, 3, 1), bloque_objects[0]),
            (estudiante_objects[1], asignatura_objects[1], 'ausente', date(2020, 3, 2), bloque_objects[3]),
            (estudiante_objects[0], asignatura_objects[2], 'presente', date(2020, 3, 3), bloque_objects[4]),
            (estudiante_objects[1], asignatura_objects[3], 'presente', date(2020, 3, 4), bloque_objects[7]),
        ]
        
        asistencia_objects = []
        for estudiante, asignatura, estado, fecha, bloque in asistencias_data:
            asistencia, created = Asistencia.objects.get_or_create(
                RUN_estudiante=estudiante,
                id_asignatura=asignatura,
                fecha=fecha,
                defaults={
                    'estado': estado,
                    'id_bloque_horario': bloque
                }
            )
            asistencia_objects.append(asistencia)
            if created:
                self.stdout.write(f'Asistencia creada: {estudiante.RUN_persona.RUN} - {fecha}')

        # Create Justificacion records
        self.stdout.write('Creando registros de Justificacion...')
        justificaciones_data = [
            (asistencia_objects[0], sala_objects[0], 'Falta por enfermedad'),
            (asistencia_objects[1], sala_objects[1], 'Falta por viaje familiar'),
            (asistencia_objects[2], sala_objects[2], 'Falta por compromiso personal'),
            (asistencia_objects[3], sala_objects[3], 'Falta por motivo académico'),
        ]
        
        for asistencia, sala, descripcion in justificaciones_data:
            justificacion, created = Justificacion.objects.get_or_create(
                id_asistencia=asistencia,
                defaults={
                    'id_sala': sala,
                    'descripcion_justificacion': descripcion
                }
            )
            if created:
                self.stdout.write(f'Justificacion creada: {descripcion}')

        # Create Actividad_Extracurricular records
        self.stdout.write('Creando registros de Actividad_Extracurricular...')
        actividades_data = [
            (sala_objects[0], 'Fútbol'),
            (sala_objects[1], 'Banda Escolar'),
            (sala_objects[2], 'Teatro'),
            (sala_objects[3], 'Coro'),
            (sala_objects[4], 'Robótica'),
        ]
        
        actividad_objects = []
        for sala, nombre_actividad in actividades_data:
            actividad, created = Actividad_Extracurricular.objects.get_or_create(
                id_sala=sala,
                nombre_actividad=nombre_actividad
            )
            actividad_objects.append(actividad)
            if created:
                self.stdout.write(f'Actividad_Extracurricular creada: {nombre_actividad}')

        # Create Reporte_Accidente records
        self.stdout.write('Creando registros de Reporte_Accidente...')
        accidentes_data = [
            (estudiante_objects[0], 'Caída en el patio durante el recreo', date(2020, 3, 1)),
            (estudiante_objects[1], 'Lesión en la clase de educación física', date(2021, 3, 2)),
        ]
        
        for estudiante, descripcion, fecha in accidentes_data:
            accidente, created = Reporte_Accidente.objects.get_or_create(
                RUN_Estudiante=estudiante,
                fecha=fecha,
                defaults={'descripcion_accidente': descripcion}
            )
            if created:
                self.stdout.write(f'Created Reporte_Accidente: {estudiante.RUN_persona.RUN}')

        # Create Anotacion records
        self.stdout.write('Creando registros de Anotacion...')
        anotaciones_data = [
            (estudiante_objects[0], 'Excelente participación en clase', 'positiva'),
            (estudiante_objects[1], 'Falta de respeto a un compañero', 'negativa'),
        ]
        
        for estudiante, descripcion, tipo in anotaciones_data:
            anotacion, created = Anotacion.objects.get_or_create(
                RUN_Estudiante=estudiante,
                descripcion_anotacion=descripcion,
                defaults={'tipo_anotacion': tipo}
            )
            if created:
                self.stdout.write(f'Anotacion creada: {tipo} - {estudiante.RUN_persona.RUN}')

        # Create relationship records
        self.stdout.write('Creando registros de relaciones...')

        # estudianteTOMAactividad
        toma_actividad_data = [
            (estudiante_objects[0], actividad_objects[0]),  # Estudiante toma Fútbol
            (estudiante_objects[1], actividad_objects[1]),  # Estudiante toma Banda Escolar
        ]
        
        for estudiante, actividad in toma_actividad_data:
            toma, created = estudianteTOMAactividad.objects.get_or_create(
                RUN_Estudiante=estudiante,
                id_actividad=actividad
            )
            if created:
                self.stdout.write(f'estudianteTOMAactividad creada: {estudiante.RUN_persona.RUN} - {actividad.nombre_actividad}')

        # estudianteRINDEevaluacion
        rinde_evaluacion_data = [
            (estudiante_objects[0], evaluacion_objects[0], 6.5),
            (estudiante_objects[1], evaluacion_objects[1], 5.0),
        ]
        
        for estudiante, evaluacion, nota in rinde_evaluacion_data:
            rinde, created = estudianteRINDEevaluacion.objects.get_or_create(
                RUN_Estudiante=estudiante,
                id_evaluacion=evaluacion,
                defaults={'nota': nota}
            )
            if created:
                self.stdout.write(f'estudianteRINDEevaluacion creada: {estudiante.RUN_persona.RUN} - Nota: {nota}')

        # estudiantePERTENECEcurso
        pertenece_curso_data = [
            (estudiante_objects[0], curso_objects[0]),
            (estudiante_objects[1], curso_objects[1]),
        ]
        
        for estudiante, curso in pertenece_curso_data:
            pertenece, created = estudiantePERTENECEcurso.objects.get_or_create(
                RUN_Estudiante=estudiante,
                id_curso=curso
            )
            if created:
                self.stdout.write(f'estudiantePERTENECEcurso creada: {estudiante.RUN_persona.RUN} - Curso {curso.grado}{curso.letra}')

        # apoderadoRESPONSABLEDEestudiante
        responsable_data = [
            (estudiante_objects[0], apoderado_objects[0], 'Padre'),
            (estudiante_objects[1], apoderado_objects[1], 'Madre'),
        ]
        
        for estudiante, apoderado, relacion in responsable_data:
            responsable, created = apoderadoRESPONSABLEDEestudiante.objects.get_or_create(
                RUN_Estudiante=estudiante,
                RUN_Apoderado=apoderado,
                defaults={'relacion': relacion}
            )
            if created:
                self.stdout.write(f'apoderadoRESPONSABLEDEestudiante creada: {apoderado.RUN_persona.RUN} - {estudiante.RUN_persona.RUN}')

        # docenteDICTAasignatura
        dicta_asignatura_data = [
            (asignatura_objects[0], docente_objects[0]),  # Matemáticas
            (asignatura_objects[1], docente_objects[1]),  # Lenguaje y Comunicación
            (asignatura_objects[2], docente_objects[0]),  # Ciencias Naturales
            (asignatura_objects[3], docente_objects[1]),  # Historia y Geografía
        ]
        
        for asignatura, docente in dicta_asignatura_data:
            dicta, created = docenteDICTAasignatura.objects.get_or_create(
                id_asignatura=asignatura,
                RUN_Docente=docente
            )
            if created:
                self.stdout.write(f'docenteDICTAasignatura creada: {docente.RUN_persona.RUN} - {asignatura.nombre_asignatura}')

        # docenteACARGOactividad
        a_cargo_data = [
            (actividad_objects[0], docente_objects[0]),  # Fútbol
            (actividad_objects[1], docente_objects[1]),  # Banda Escolar
        ]
        
        for actividad, docente in a_cargo_data:
            a_cargo, created = docenteACARGOactividad.objects.get_or_create(
                id_actividad=actividad,
                RUN_Docente=docente
            )
            if created:
                self.stdout.write(f'docenteACARGOactividad creada: {docente.RUN_persona.RUN} - {actividad.nombre_actividad}')

        # actividadESTAENELbloquehorario
        actividad_bloque_data = [
            (actividad_objects[0], bloque_objects[0]),  # Fútbol - Lunes 8:00-10:00
            (actividad_objects[1], bloque_objects[3]),  # Banda Escolar - Martes 10:30-12:30
        ]
        
        for actividad, bloque in actividad_bloque_data:
            actividad_bloque, created = actividadESTAENELbloquehorario.objects.get_or_create(
                id_actividad=actividad,
                id_bloque_horario=bloque
            )
            if created:
                self.stdout.write(f'actividadESTAENELbloquehorario creada: {actividad.nombre_actividad} - {bloque.dia}')

        # asignaturaESTAENbloquehorario
        asignatura_bloque_data = [
            (asignatura_objects[2], bloque_objects[4]),  # Ciencias Naturales - Miércoles 8:00-10:00
            (asignatura_objects[3], bloque_objects[7]),  # Historia y Geografía - Jueves 10:30-12:30
            (asignatura_objects[4], bloque_objects[8]),  # Educación Física - Viernes 8:00-10:00
        ]
        
        for asignatura, bloque in asignatura_bloque_data:
            asignatura_bloque, created = asignaturaESTAENbloquehorario.objects.get_or_create(
                id_asignatura=asignatura,
                id_bloque_horario=bloque
            )
            if created:
                self.stdout.write(f'asignaturaESTAENbloquehorario creada: {asignatura.nombre_asignatura} - {bloque.dia}')

        self.stdout.write(
            self.style.SUCCESS('La base de datos ha sido poblada exitosamente.')
        )
