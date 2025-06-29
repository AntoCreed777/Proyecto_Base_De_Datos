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
    nombre_familia = models.CharField(max_length=100)
    numero_integrantes = models.IntegerField()
    cuantos_trabajan = models.IntegerField()
    ocupacion_padres = models.CharField(max_length=100)

    estado_marital_padres = models.TextChoices(
        'EstadoMaritalPadres',
        [
            ('soltero', 'Soltero'),
            ('casado', 'Casado'),
            ('divorciado', 'Divorciado'),
            ('viudo', 'Viudo'),
        ]
    )
    estado_vida_padres = models.CharField(max_length=50)
    ingresos_mensuales = models.BigIntegerField()

    cantidad_dormitorios = models.IntegerField()
    cantidad_banos = models.IntegerField()
    banos_compartidos = models.BooleanField(default=False)
    energia = models.CharField(max_length=50)
    tipo_agua = models.CharField(max_length=50)
    tipo_construccion = models.CharField(max_length=50)
    propiedad = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.RUN_persona} {self.profesion} {self.lugar_de_trabajo}"