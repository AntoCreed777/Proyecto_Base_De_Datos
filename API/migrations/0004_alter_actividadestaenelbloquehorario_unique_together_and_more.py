# Generated by Django 4.2.23 on 2025-07-05 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_rename_run_persona_persona_run'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='actividadestaenelbloquehorario',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='actividadestaenelbloquehorario',
            name='id_actividad',
        ),
        migrations.RemoveField(
            model_name='actividadestaenelbloquehorario',
            name='id_bloque_horario',
        ),
        migrations.RemoveField(
            model_name='anotacion',
            name='RUN_Estudiante',
        ),
        migrations.RemoveField(
            model_name='apoderado',
            name='RUN_persona',
        ),
        migrations.AlterUniqueTogether(
            name='apoderadoresponsabledeestudiante',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='apoderadoresponsabledeestudiante',
            name='RUN_Apoderado',
        ),
        migrations.RemoveField(
            model_name='apoderadoresponsabledeestudiante',
            name='RUN_Estudiante',
        ),
        migrations.RemoveField(
            model_name='asignatura',
            name='id_curso',
        ),
        migrations.AlterUniqueTogether(
            name='asignaturaestaenbloquehorario',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='asignaturaestaenbloquehorario',
            name='id_asignatura',
        ),
        migrations.RemoveField(
            model_name='asignaturaestaenbloquehorario',
            name='id_bloque_horario',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='RUN_estudiante',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='id_asignatura',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='id_bloque_horario',
        ),
        migrations.AlterUniqueTogether(
            name='bloque_horario',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='curso',
            name='id_docente',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='id_sala',
        ),
        migrations.RemoveField(
            model_name='direccion_de_trabajo',
            name='RUN_Apoderado',
        ),
        migrations.RemoveField(
            model_name='docente',
            name='RUN_persona',
        ),
        migrations.AlterUniqueTogether(
            name='docenteacargoactividad',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='docenteacargoactividad',
            name='RUN_Docente',
        ),
        migrations.RemoveField(
            model_name='docenteacargoactividad',
            name='id_actividad',
        ),
        migrations.AlterUniqueTogether(
            name='docentedictaasignatura',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='docentedictaasignatura',
            name='RUN_Docente',
        ),
        migrations.RemoveField(
            model_name='docentedictaasignatura',
            name='id_asignatura',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='RUN_persona',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='id_familia',
        ),
        migrations.AlterUniqueTogether(
            name='estudiantepertenececurso',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='estudiantepertenececurso',
            name='RUN_Estudiante',
        ),
        migrations.RemoveField(
            model_name='estudiantepertenececurso',
            name='id_curso',
        ),
        migrations.AlterUniqueTogether(
            name='estudianterindeevaluacion',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='estudianterindeevaluacion',
            name='RUN_Estudiante',
        ),
        migrations.RemoveField(
            model_name='estudianterindeevaluacion',
            name='id_evaluacion',
        ),
        migrations.AlterUniqueTogether(
            name='estudiantetomaactividad',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='estudiantetomaactividad',
            name='RUN_Estudiante',
        ),
        migrations.RemoveField(
            model_name='estudiantetomaactividad',
            name='id_actividad',
        ),
        migrations.RemoveField(
            model_name='evaluacion',
            name='id_asignatura',
        ),
        migrations.RemoveField(
            model_name='evaluacion',
            name='run_docente',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='RUN_persona',
        ),
        migrations.RemoveField(
            model_name='justificacion',
            name='id_asistencia',
        ),
        migrations.RemoveField(
            model_name='justificacion',
            name='id_sala',
        ),
        migrations.RemoveField(
            model_name='lugar_de_residencia',
            name='RUN_persona',
        ),
        migrations.RemoveField(
            model_name='nombre_completo',
            name='RUN_persona',
        ),
        migrations.RemoveField(
            model_name='numero_telefonico',
            name='RUN_persona',
        ),
        migrations.RemoveField(
            model_name='numero_telefonico_trabajo',
            name='RUN_Apoderado',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id_genero',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id_nacionalidad',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id_religion',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='reporte_accidente',
            name='RUN_Estudiante',
        ),
        migrations.DeleteModel(
            name='Actividad_Extracurricular',
        ),
        migrations.DeleteModel(
            name='actividadESTAENELbloquehorario',
        ),
        migrations.DeleteModel(
            name='Anotacion',
        ),
        migrations.DeleteModel(
            name='Apoderado',
        ),
        migrations.DeleteModel(
            name='apoderadoRESPONSABLEDEestudiante',
        ),
        migrations.DeleteModel(
            name='Asignatura',
        ),
        migrations.DeleteModel(
            name='asignaturaESTAENbloquehorario',
        ),
        migrations.DeleteModel(
            name='Asistencia',
        ),
        migrations.DeleteModel(
            name='Bloque_Horario',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Direccion_de_Trabajo',
        ),
        migrations.DeleteModel(
            name='Docente',
        ),
        migrations.DeleteModel(
            name='docenteACARGOactividad',
        ),
        migrations.DeleteModel(
            name='docenteDICTAasignatura',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='estudiantePERTENECEcurso',
        ),
        migrations.DeleteModel(
            name='estudianteRINDEevaluacion',
        ),
        migrations.DeleteModel(
            name='estudianteTOMAactividad',
        ),
        migrations.DeleteModel(
            name='Evaluacion',
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Info_Familia',
        ),
        migrations.DeleteModel(
            name='Justificacion',
        ),
        migrations.DeleteModel(
            name='Lugar_de_Residencia',
        ),
        migrations.DeleteModel(
            name='Nacionalidad',
        ),
        migrations.DeleteModel(
            name='Nombre_Completo',
        ),
        migrations.DeleteModel(
            name='Numero_Telefonico',
        ),
        migrations.DeleteModel(
            name='Numero_Telefonico_Trabajo',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.DeleteModel(
            name='Religion',
        ),
        migrations.DeleteModel(
            name='Reporte_Accidente',
        ),
        migrations.DeleteModel(
            name='Sala',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
