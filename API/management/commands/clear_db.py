from django.core.management.base import BaseCommand
from django.db import transaction
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
    help = 'Elimina todos los datos de la base de datos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Confirmar la eliminación sin preguntar',
        )

    def handle(self, *args, **options):
        if not options['confirm']:
            confirm = input(
                "⚠️  ADVERTENCIA: Esto eliminará TODOS los datos de la base de datos.\n"
                "¿Estás seguro que quieres continuar? (escribe 'si' para confirmar): "
            )
            if confirm.lower() != 'si':
                self.stdout.write(
                    self.style.WARNING('❌ Operación cancelada')
                )
                return

        self.stdout.write('🗑️  Iniciando eliminación de todos los datos...')
        
        try:
            with transaction.atomic():
                # Eliminar en orden inverso para respetar las foreign keys
                # Primero las tablas de relaciones
                self.stdout.write('Eliminando relaciones...')
                
                count = asignaturaESTAENbloquehorario.objects.count()
                asignaturaESTAENbloquehorario.objects.all().delete()
                self.stdout.write(f'  - asignaturaESTAENbloquehorario: {count} registros eliminados')
                
                count = actividadESTAENELbloquehorario.objects.count()
                actividadESTAENELbloquehorario.objects.all().delete()
                self.stdout.write(f'  - actividadESTAENELbloquehorario: {count} registros eliminados')
                
                count = docenteACARGOactividad.objects.count()
                docenteACARGOactividad.objects.all().delete()
                self.stdout.write(f'  - docenteACARGOactividad: {count} registros eliminados')
                
                count = docenteDICTAasignatura.objects.count()
                docenteDICTAasignatura.objects.all().delete()
                self.stdout.write(f'  - docenteDICTAasignatura: {count} registros eliminados')
                
                count = apoderadoRESPONSABLEDEestudiante.objects.count()
                apoderadoRESPONSABLEDEestudiante.objects.all().delete()
                self.stdout.write(f'  - apoderadoRESPONSABLEDEestudiante: {count} registros eliminados')
                
                count = estudiantePERTENECEcurso.objects.count()
                estudiantePERTENECEcurso.objects.all().delete()
                self.stdout.write(f'  - estudiantePERTENECEcurso: {count} registros eliminados')
                
                count = estudianteRINDEevaluacion.objects.count()
                estudianteRINDEevaluacion.objects.all().delete()
                self.stdout.write(f'  - estudianteRINDEevaluacion: {count} registros eliminados')
                
                count = estudianteTOMAactividad.objects.count()
                estudianteTOMAactividad.objects.all().delete()
                self.stdout.write(f'  - estudianteTOMAactividad: {count} registros eliminados')
                
                # Luego las tablas que dependen de otras
                self.stdout.write('Eliminando registros dependientes...')
                
                count = Anotacion.objects.count()
                Anotacion.objects.all().delete()
                self.stdout.write(f'  - Anotacion: {count} registros eliminados')
                
                count = Reporte_Accidente.objects.count()
                Reporte_Accidente.objects.all().delete()
                self.stdout.write(f'  - Reporte_Accidente: {count} registros eliminados')
                
                count = Actividad_Extracurricular.objects.count()
                Actividad_Extracurricular.objects.all().delete()
                self.stdout.write(f'  - Actividad_Extracurricular: {count} registros eliminados')
                
                count = Justificacion.objects.count()
                Justificacion.objects.all().delete()
                self.stdout.write(f'  - Justificacion: {count} registros eliminados')
                
                count = Asistencia.objects.count()
                Asistencia.objects.all().delete()
                self.stdout.write(f'  - Asistencia: {count} registros eliminados')
                
                count = Bloque_Horario.objects.count()
                Bloque_Horario.objects.all().delete()
                self.stdout.write(f'  - Bloque_Horario: {count} registros eliminados')
                
                count = Evaluacion.objects.count()
                Evaluacion.objects.all().delete()
                self.stdout.write(f'  - Evaluacion: {count} registros eliminados')
                
                count = Asignatura.objects.count()
                Asignatura.objects.all().delete()
                self.stdout.write(f'  - Asignatura: {count} registros eliminados')
                
                count = Curso.objects.count()
                Curso.objects.all().delete()
                self.stdout.write(f'  - Curso: {count} registros eliminados')
                
                count = Sala.objects.count()
                Sala.objects.all().delete()
                self.stdout.write(f'  - Sala: {count} registros eliminados')
                
                count = Estudiante.objects.count()
                Estudiante.objects.all().delete()
                self.stdout.write(f'  - Estudiante: {count} registros eliminados')
                
                count = Info_Familia.objects.count()
                Info_Familia.objects.all().delete()
                self.stdout.write(f'  - Info_Familia: {count} registros eliminados')
                
                count = Docente.objects.count()
                Docente.objects.all().delete()
                self.stdout.write(f'  - Docente: {count} registros eliminados')
                
                count = Apoderado.objects.count()
                Apoderado.objects.all().delete()
                self.stdout.write(f'  - Apoderado: {count} registros eliminados')
                
                # Luego las tablas de información personal
                self.stdout.write('Eliminando información personal...')
                
                count = Lugar_de_Residencia.objects.count()
                Lugar_de_Residencia.objects.all().delete()
                self.stdout.write(f'  - Lugar_de_Residencia: {count} registros eliminados')
                
                count = Numero_Telefonico.objects.count()
                Numero_Telefonico.objects.all().delete()
                self.stdout.write(f'  - Numero_Telefonico: {count} registros eliminados')
                
                count = Nombre_Completo.objects.count()
                Nombre_Completo.objects.all().delete()
                self.stdout.write(f'  - Nombre_Completo: {count} registros eliminados')
                
                count = Persona.objects.count()
                Persona.objects.all().delete()
                self.stdout.write(f'  - Persona: {count} registros eliminados')
                
                # Finalmente las tablas de catálogos
                self.stdout.write('Eliminando catálogos...')
                
                count = Religion.objects.count()
                Religion.objects.all().delete()
                self.stdout.write(f'  - Religion: {count} registros eliminados')
                
                count = Nacionalidad.objects.count()
                Nacionalidad.objects.all().delete()
                self.stdout.write(f'  - Nacionalidad: {count} registros eliminados')
                
                count = Genero.objects.count()
                Genero.objects.all().delete()
                self.stdout.write(f'  - Genero: {count} registros eliminados')
                
                self.stdout.write(
                    self.style.SUCCESS('✅ Todos los datos han sido eliminados exitosamente')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error durante la eliminación: {str(e)}')
            )
            raise
