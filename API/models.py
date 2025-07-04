from django.db import models 

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
class Nacionalidad(models.Model):
    pais = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.pais
    
class Religion(models.Model):
    nombre_religion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_religion
    
class Persona(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    RUN = models.CharField(max_length=12, unique=True, primary_key=True)
    fecha_nacimiento = models.DateField(null=False)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    id_religion = models.ForeignKey(Religion, on_delete=models.CASCADE)

class Nombre_Completo(models.Model):
    RUN_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, primary_key=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.primer_nombre} {self.segundo_nombre or ''} {self.apellido_paterno} {self.apellido_materno or ''}"
    
class Numero_Telefonico(models.Model):
    RUN_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    codigo_del_pais = models.IntegerField()
    codigo_del_area = models.IntegerField()
    numero_unico = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.codigo_del_pais} {self.codigo_del_area} {self.numero_unico}"
    
class Lugar_de_Residencia(models.Model):
    RUN_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, primary_key=True)
    region = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    numero_casa = models.IntegerField()
    numero_departamento = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.calle}, {self.numero_casa}, {self.numero_departamento}, {self.ciudad}, {self.region}"
    
class Apoderado(models.Model):
    RUN_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, primary_key=True)
    profesion = models.CharField(max_length=100)
    lugar_de_trabajo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.RUN_persona} {self.profesion} {self.lugar_de_trabajo}"
    
class Direccion_de_Trabajo(models.Model):
    RUN_Apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE, primary_key=True)
    region = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    numero_casa = models.IntegerField()
    numero_departamento = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.calle}, {self.numero_casa}, {self.numero_departamento}, {self.ciudad}, {self.region}"
    
class Numero_Telefonico_Trabajo(models.Model):
    RUN_Apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE, primary_key=True)
    codigo_del_pais = models.IntegerField()
    codigo_del_area = models.IntegerField()
    numero_unico = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.codigo_del_pais} {self.codigo_del_area} {self.numero_unico}"
    
class Funcionario(models.Model):
    RUN_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, primary_key=True)
    titulo_academico = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.RUN_persona} {self.titulo_academico} {self.cargo} {self.rol}"
    
class Docente(models.Model):
    RUN_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.RUN_persona}"


class Info_Familia(models.Model):

    class Estado_Marital_Padres(models.TextChoices):
        CASADOS = 'casados', 'Casados'
        SEPARADOS = 'separados', 'Separados'
        ANULADO = 'anulado', 'Anulado'
        CONVIVIENTES = 'convivientes', 'Convivientes'
        VIUDO = 'viudo', 'Viudo' 
        VIUDA = 'viuda', 'Viuda' 
        SOLTEROS = 'solteros', 'Solteros'
        DIVORCIADO = 'divorciado', 'Divorciado'

    class Estado_Vida_Padres(models.TextChoices):
        AMBOS_VIVOS = 'ambos_vivos', 'Ambos Vivos'
        AMBOS_FALLECIDOS = 'ambos_fallecidos', 'Ambos Fallecidos'
        PADRE_FALLECIDO = 'padre_fallecido', 'Padre Fallecido'
        MADRE_FALLECIDA = 'madre_fallecida', 'Madre Fallecida'

    class Energia(models.TextChoices):
        RED_ELECTRICA = 'red_electrica', 'Red Eléctrica'

    class Tipo_Agua(models.TextChoices):
        ALCANTARILLADO = 'alcantarillado', 'Alcantarillado'
        POZO = 'pozo', 'Pozo'
        SIN_ACCESO = 'sin_acceso', 'Sin Acceso'
        CON_BOMBA = 'con_bomba', 'Con Bomba'
        LLAVE_EN_VIVIENDA = 'llave_en_vivienda', 'Llave en Vivienda'
        LLAVE_EN_SITIO = 'llave_en_sitio', 'Llave en Sitio'
    
    class Tipo_Construccion(models.TextChoices):
        CASA_SOLIDA = 'casa_solida', 'Casa Sólida'
        CASA_MADERA = 'casa_madera', 'Casa de Madera'
        DEPARTAMENTO = 'departamento', 'Departamento'
        ARRIENDO = 'arriendo', 'Arriendo'
        MEDIA_AGUA = 'media_agua', 'Media Agua'

    class Propiedad(models.TextChoices):
        PROPIA = 'propia', 'Propia'
        CEDIDA = 'cedida', 'Cedida'
        ARRENDADA = 'arrendada', 'Arrendada'
        ALLEGADOS = 'allegados', 'Allegados'

    nombre_familia = models.CharField(max_length=100)
    numero_integrantes = models.IntegerField()
    cuantos_trabajan = models.IntegerField()
    ocupacion_padres = models.CharField(max_length=100)

    estado_marital_padres = models.CharField(
        max_length=50,
        choices=Estado_Marital_Padres.choices,
        default=Estado_Marital_Padres.CASADOS
    )

    estado_vida_padres = models.CharField(
        max_length=50,
        choices=Estado_Vida_Padres.choices,
        default=Estado_Vida_Padres.AMBOS_VIVOS
    )

    ingresos_mensuales = models.BigIntegerField()

    cantidad_dormitorios = models.IntegerField()
    cantidad_banos = models.IntegerField()
    banos_compartidos = models.BooleanField(default=False)
    energia = models.CharField(
        max_length=50,
        choices=Energia.choices,
        default=Energia.RED_ELECTRICA
    )
    tipo_agua = models.CharField(
        max_length=50,
        choices=Tipo_Agua.choices,
        default=Tipo_Agua.ALCANTARILLADO
    )

    tipo_construccion = models.CharField(
        max_length=50,
        choices=Tipo_Construccion.choices,
        default=Tipo_Construccion.CASA_SOLIDA
    )

    propiedad = models.CharField(
        max_length=50,
        choices=Propiedad.choices,
        default=Propiedad.PROPIA
    )

    def __str__(self):
        return f"{self.nombre_familia} - {self.numero_integrantes} integrantes"
    

class Estudiante(models.Model):

    class Estado_Academico(models.TextChoices):
        VIGENTE = 'vigente', 'Vigente'
        EGRESADO = 'egresado', 'Egresado'
        REITERADO = 'reiterado', 'Reiterado'
        ELIMINADO = 'eliminado', 'Eliminado'
        PREMATRICULADO = 'prematriculado', 'Prematriculado'
        CONGELADO = 'congelado', 'Congelado'

    RUN_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, primary_key=True)
    id_familia = models.ForeignKey(Info_Familia, on_delete=models.CASCADE)
    anio_ingreso = models.IntegerField()
    numero_de_matricula = models.CharField(max_length=50, unique=True)
    fecha_matricula = models.DateField()
    #foto = models.ImageField(upload_to='fotos_estudiantes/', blank=True, null=True) 
    estado_academico = models.CharField(
        max_length=50, 
        choices=Estado_Academico.choices,
        default=Estado_Academico.VIGENTE
    )

    semestre_ingreso = models.IntegerField()

    def __str__(self):
        return f"{self.RUN_persona} {self.id_familia} {self.anio_ingreso} {self.numero_de_matricula}"
    
class Bloque_Horario(models.Model):

    class Dias_Semana(models.TextChoices):
        LUNES = 'lunes', 'Lunes'
        MARTES = 'martes', 'Martes'
        MIERCOLES = 'miercoles', 'Miércoles'
        JUEVES = 'jueves', 'Jueves'
        VIERNES = 'viernes', 'Viernes'
        SABADO = 'sabado', 'Sábado'
        DOMINGO = 'domingo', 'Domingo'

    dia = models.CharField(
        max_length=50,
        choices=Dias_Semana.choices,
        default=Dias_Semana.LUNES
    )

    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        unique_together = (('dia', 'hora_inicio', 'hora_fin'),)

    def __str__(self):
        return f"{self.dia} {self.hora_inicio} - {self.hora_fin}"
    
class Sala(models.Model):
    nombre_sala = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_sala
    
class Curso(models.Model):
    
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    anio = models.IntegerField()
    semestre = models.IntegerField()
    grado = models.IntegerField()
    letra = models.CharField(max_length=1, default='A')

    def __str__(self):
        return f"{self.grado} ({self.letra}) - {self.anio} Semestre {self.semestre}, Docente: {self.id_docente}, Sala: {self.id_sala}"
    
class Asignatura(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre_asignatura = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_asignatura}, curso: {self.id_curso}"
    
class Evaluacion(models.Model):
    run_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha_evaluacion = models.DateField()
    ponderacion = models.FloatField()

class Asistencia(models.Model):
    class EstadoAsistencia(models.TextChoices):
        PRESENTE = 'presente', 'Presente'
        AUSENTE = 'ausente', 'Ausente'
        JUSTIFICADO = 'justificado', 'Justificado'

    id_bloque_horario = models.ForeignKey(Bloque_Horario, on_delete=models.CASCADE)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    RUN_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(
        max_length=50,
        choices=EstadoAsistencia.choices,
        default=EstadoAsistencia.PRESENTE
    )

    def __str__(self):
        return f"{self.RUN_estudiante} {self.id_bloque_horario} {self.fecha} {self.estado}"
    
class Justificacion(models.Model):
    id_asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    descripcion_justificacion = models.TextField()

    def __str__(self):
        return f"{self.id_asistencia} {self.id_sala} {self.descripcion_justificacion}"
    
class Actividad_Extracurricular(models.Model):
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    nombre_actividad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_actividad} en {self.id_sala}"

class Reporte_Accidente(models.Model):
    RUN_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    descripcion_accidente = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Reporte de accidente de {self.RUN_Estudiante} en {self.fecha}"
    
class Anotacion(models.Model):
    class TipoAnotacion(models.TextChoices):
        POSITIVA = 'positiva', 'Positiva'
        NEGATIVA = 'negativa', 'Negativa'

    RUN_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    descripcion_anotacion = models.TextField()
    tipo_anotacion = models.CharField(
        max_length=50,
        choices=TipoAnotacion.choices,
    )

    def __str__(self):
        return f"Anotación de {self.RUN_Estudiante} - {self.tipo_anotacion}"
    
    
class estudianteTOMAactividad(models.Model):
   
    RUN_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_actividad = models.ForeignKey(Actividad_Extracurricular, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('RUN_Estudiante', 'id_actividad'),)

    def __str__(self):
        return f"{self.RUN_Estudiante} toma {self.id_actividad}"

  
class estudianteRINDEevaluacion(models.Model):

    RUN_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    nota = models.FloatField()

    class Meta:
        unique_together = (('RUN_Estudiante', 'id_evaluacion'),)


    def __str__(self):
        return f"{self.RUN_Estudiante} rinde {self.id_evaluacion} con nota {self.nota}"

  
class estudiantePERTENECEcurso(models.Model):
    
    RUN_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('RUN_Estudiante', 'id_curso'),)

    def __str__(self):
        return f"{self.RUN_Estudiante} pertenece al curso {self.id_curso}"
    
class apoderadoRESPONSABLEDEestudiante(models.Model):

    RUN_Apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE)
    RUN_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    relacion = models.CharField(max_length=50)

    class Meta:
        unique_together = (('RUN_Estudiante', 'RUN_Apoderado'),)

    def __str__(self):
        return f"{self.RUN_Apoderado} es responsable de {self.RUN_Estudiante}"
    

class docenteDICTAasignatura(models.Model):
    RUN_Docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    class Meta: 
        unique_together = (('RUN_Docente', 'id_asignatura'),)

    def __str__(self):
        return f"{self.RUN_Docente} dicta {self.id_asignatura}"

class docenteACARGOactividad(models.Model):
    RUN_Docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    id_actividad = models.ForeignKey(Actividad_Extracurricular, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('RUN_Docente', 'id_actividad'),)

    def __str__(self):
        return f"{self.RUN_Docente} está a cargo de {self.id_actividad}"
    
class actividadESTAENELbloquehorario(models.Model):
    id_actividad = models.ForeignKey(Actividad_Extracurricular, on_delete=models.CASCADE)
    id_bloque_horario = models.ForeignKey(Bloque_Horario, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_actividad', 'id_bloque_horario'),)

    def __str__(self):
        return f"{self.id_actividad} está en el bloque horario {self.id_bloque_horario}"
      
class asignaturaESTAENbloquehorario(models.Model):
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    id_bloque_horario = models.ForeignKey(Bloque_Horario, on_delete=models.CASCADE)
 
    class Meta:
        unique_together = (('id_asignatura', 'id_bloque_horario'),)

    def __str__(self):
        return f"{self.id_asignatura} está en el bloque horario {self.id_bloque_horario}"