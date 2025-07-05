CREATE SCHEMA proyecto_bd;


CREATE TABLE IF NOT EXISTS proyecto_bd.Genero (
    ID_Genero SERIAL PRIMARY KEY,
    Nombre_Genero VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Nacionalidad (
    ID_Nacionalidad SERIAL PRIMARY KEY,
    Pais VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Religion (
    ID_Religion SERIAL PRIMARY KEY,
    Nombre_Religion VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Persona (
    RUN_Persona VARCHAR(12) PRIMARY KEY,
    Contraseña VARCHAR(255) NOT NULL,
    Fecha_de_nacimiento DATE NOT NULL,
    ID_Genero INT,
    ID_Nacionalidad INT,
    ID_Religion INT,
    FOREIGN KEY (ID_Religion) REFERENCES proyecto_bd.Religion(ID_Religion),
    FOREIGN KEY (ID_Genero) REFERENCES proyecto_bd.Genero(ID_Genero),
    FOREIGN KEY (ID_Nacionalidad) REFERENCES proyecto_bd.Nacionalidad(ID_Nacionalidad)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Nombre_Completo (
    RUN_Persona VARCHAR(12) PRIMARY KEY,
    Primer_nombre VARCHAR(50),
    Segundo_nombre VARCHAR(50),
    Apellido_paterno VARCHAR(50),
    Apellido_materno VARCHAR(50),
    FOREIGN KEY (RUN_Persona) REFERENCES proyecto_bd.Persona(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Numero_Telefonico (
    RUN_Persona VARCHAR(12) PRIMARY KEY,
    Codigo_del_pais INT NOT NULL,
    Codigo_del_area INT NOT NULL,
    Numero_unico BIGINT NOT NULL UNIQUE,
    FOREIGN KEY (RUN_Persona) REFERENCES proyecto_bd.Persona(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Lugar_de_Residencia (
    RUN_Persona VARCHAR(12) PRIMARY KEY,
    Region VARCHAR(100),
    Ciudad VARCHAR(100),
    Comuna VARCHAR(100),
    Calle VARCHAR(100),
    Numero_casa INT,
    Numero_dpt INT,
    FOREIGN KEY (RUN_Persona) REFERENCES proyecto_bd.Persona(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Apoderado (
    RUN_Persona VARCHAR(12) PRIMARY KEY,
    Profesion VARCHAR(100),
    Lugar_de_Trabajo VARCHAR(255),
    FOREIGN KEY (RUN_Persona) REFERENCES proyecto_bd.Persona(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Direccion_de_Trabajo (
    RUN_Apoderado VARCHAR(12) PRIMARY KEY,
    Region VARCHAR(100),
    Ciudad VARCHAR(100),
    Comuna VARCHAR(100),
    Calle VARCHAR(100),
    Numero_Casa INT,
    Numero_Dpt INT,
    FOREIGN KEY (RUN_Apoderado) REFERENCES proyecto_bd.Apoderado(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Numero_Telefonico_Trabajo (
    RUN_Apoderado VARCHAR(12),
    Codigo_del_Pais INT,
    Codigo_del_Area INT,
    Numero_Unico BIGINT NOT NULL UNIQUE,
    PRIMARY KEY (RUN_Apoderado),
    FOREIGN KEY (RUN_Apoderado) REFERENCES proyecto_bd.Apoderado(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Funcionario (
    RUN_Persona VARCHAR(12) PRIMARY KEY,
    Titulo_Academico VARCHAR(100),
    Cargo VARCHAR(50),
    Rol VARCHAR(50),
    FOREIGN KEY (RUN_Persona) REFERENCES proyecto_bd.Persona(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Docente (
    RUN_Persona VARCHAR(12) PRIMARY KEY,
    FOREIGN KEY (RUN_Persona) REFERENCES proyecto_bd.Persona(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Info_Familia (
    ID_Familia SERIAL PRIMARY KEY,
    Nombre_Familia VARCHAR(100),
    Cuantos_Trabajan INT,
    Ocupacion_Padres VARCHAR(100),
    Numero_Integrantes INT,
    Cantidad_Dormitorios INT,
    Cantidad_Baños INT,
    Baños_Compartidos BOOLEAN,
    Energia VARCHAR(50),
    Tipo_Agua VARCHAR(50),
    Tipo_Construccion VARCHAR(50),
    Propiedad VARCHAR(50),
    Estado_Marital_Padres VARCHAR(50),
    Estado_Vida_Padres VARCHAR(50),
    Ingresos_Mensuales BIGINT
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Estudiante (
    RUN_Persona VARCHAR(12) PRIMARY KEY,
    ID_Familia INT,
    Año_de_Ingreso INT NOT NULL,
    Numero_de_Matricula VARCHAR(50),
    Foto BYTEA,
    Fecha_Matricula DATE,
    Estado_Academico VARCHAR(50),
    Semestre_de_Ingreso INT,
    FOREIGN KEY (RUN_Persona) REFERENCES proyecto_bd.Persona(RUN_Persona),
    FOREIGN KEY (ID_Familia) REFERENCES proyecto_bd.Info_Familia(ID_Familia)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Bloque_Horario (
    Dia VARCHAR(10),
    Hora_Inicio TIME,
    Hora_Fin TIME,
    PRIMARY KEY (Dia, Hora_Inicio, Hora_Fin)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Sala (
    ID_Sala SERIAL PRIMARY KEY,
    Nombre_Sala VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Curso (
    ID_Curso SERIAL PRIMARY KEY,
    RUN_Docente VARCHAR(12),
    ID_Sala INT,
    Año INT NOT NULL,
    Semestre INT NOT NULL,
    Grado INT,
    Letra CHAR(1),
    FOREIGN KEY (RUN_Docente) REFERENCES proyecto_bd.Docente(RUN_Persona),
    FOREIGN KEY (ID_Sala) REFERENCES proyecto_bd.Sala(ID_Sala)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Asignatura (
    ID_Asignatura SERIAL PRIMARY KEY,
    ID_Curso INT,
    Nombre_asignatura VARCHAR(100),
    FOREIGN KEY (Id_Curso) REFERENCES proyecto_bd.Curso(ID_Curso)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Evaluacion (
    ID_Evaluacion SERIAL PRIMARY KEY,
    RUN_Docente VARCHAR(12),
    ID_Asignatura INT,
    Fecha_Evaluacion DATE NOT NULL,
    Ponderacion FLOAT NOT NULL,
    FOREIGN KEY (RUN_Docente) REFERENCES proyecto_bd.Docente(RUN_Persona),
    FOREIGN KEY (ID_Asignatura) REFERENCES proyecto_bd.Asignatura(ID_Asignatura)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Asistencia (
    ID_Asistencia SERIAL PRIMARY KEY,
    ID_Asignatura INT,
    RUN_Estudiante VARCHAR(12),
    Estado VARCHAR(20),
    Fecha DATE,
    Dia VARCHAR(10),
    Hora_Inicio TIME,
    Hora_Fin TIME,
    FOREIGN KEY (RUN_Estudiante) REFERENCES proyecto_bd.Estudiante(RUN_Persona),
    FOREIGN KEY (ID_Asignatura) REFERENCES proyecto_bd.Asignatura(ID_Asignatura),
    FOREIGN KEY (Dia, Hora_Inicio, Hora_Fin) REFERENCES proyecto_bd.Bloque_Horario(Dia, Hora_Inicio, Hora_Fin)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Justificacion (
    ID_Justificacion SERIAL PRIMARY KEY,
    ID_Asistencia INT NOT NULL,
    Descripcion_Justificacion TEXT,
    FOREIGN KEY (ID_Asistencia) REFERENCES proyecto_bd.Asistencia(ID_Asistencia)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Actividad_Extracurricular (
    ID_Actividad SERIAL PRIMARY KEY,
    ID_Sala INT,
    Nombre_Actividad VARCHAR(100),
    FOREIGN KEY (ID_Sala) REFERENCES proyecto_bd.Sala(ID_Sala)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Reporte_Accidente (
    ID_Reporte SERIAL PRIMARY KEY,
    RUN_Estudiante VARCHAR(12),
    Descripcion_Accidente TEXT,
    Fecha DATE NOT NULL,
    FOREIGN KEY (RUN_Estudiante) REFERENCES proyecto_bd.Estudiante(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Anotacion (
    ID_Anotacion SERIAL PRIMARY KEY,
    RUN_Estudiante VARCHAR(12),
    Descripcion_Anotacion TEXT,
    Tipo_Anotacion VARCHAR(50),
    FOREIGN KEY (RUN_Estudiante) REFERENCES proyecto_bd.Estudiante(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.estudianteTOMAactividad (
    RUN_Estudiante VARCHAR(12),
    ID_Actividad INT,
    PRIMARY KEY (RUN_Estudiante, ID_Actividad),
    FOREIGN KEY (RUN_Estudiante) REFERENCES proyecto_bd.Estudiante(RUN_Persona),
    FOREIGN KEY (ID_Actividad) REFERENCES proyecto_bd.Actividad_Extracurricular(ID_Actividad)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.estudianteRINDEevaluacion (
    RUN_Estudiante VARCHAR(12),
    ID_Evaluacion INT,
    Nota NUMERIC(5, 2),
    PRIMARY KEY (RUN_Estudiante, ID_Evaluacion),
    FOREIGN KEY (RUN_Estudiante) REFERENCES proyecto_bd.Estudiante(RUN_Persona),
    FOREIGN KEY (ID_Evaluacion) REFERENCES proyecto_bd.Evaluacion(ID_Evaluacion)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.estudiantePERTENECEcurso (
    RUN_Estudiante VARCHAR(12),
    ID_Curso INT,
    PRIMARY KEY (RUN_Estudiante, ID_Curso),
    FOREIGN KEY (RUN_Estudiante) REFERENCES proyecto_bd.Estudiante(RUN_Persona),
    FOREIGN KEY (ID_Curso) REFERENCES proyecto_bd.Curso(ID_Curso)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.apoderadoRESPONSABLEDEestudiante (
    RUN_Estudiante VARCHAR(12),
    RUN_Apoderado VARCHAR(12),
    Relacion VARCHAR(50),
    PRIMARY KEY (RUN_Estudiante, RUN_Apoderado),
    FOREIGN KEY (RUN_Estudiante) REFERENCES proyecto_bd.Estudiante(RUN_Persona),
    FOREIGN KEY (RUN_Apoderado) REFERENCES proyecto_bd.Apoderado(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.docenteDICTAasignatura (
    ID_Asignatura INT,
    RUN_Docente VARCHAR(12),
    PRIMARY KEY (ID_Asignatura, RUN_Docente),
    FOREIGN KEY (ID_Asignatura) REFERENCES proyecto_bd.Asignatura(ID_Asignatura),
    FOREIGN KEY (RUN_Docente) REFERENCES proyecto_bd.Docente(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.docenteACARGOactividad (
    ID_Actividad INT,
    RUN_Docente VARCHAR(12),
    PRIMARY KEY (ID_Actividad, RUN_Docente),
    FOREIGN KEY (ID_Actividad) REFERENCES proyecto_bd.Actividad_Extracurricular(ID_Actividad),
    FOREIGN KEY (RUN_Docente) REFERENCES proyecto_bd.Docente(RUN_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.actividadESTAENELbloquehorario (
    ID_Actividad INT,
    Dia VARCHAR(10),
    Hora_Inicio TIME,
    Hora_Fin TIME,
    PRIMARY KEY (Dia, Hora_Inicio, Hora_Fin, ID_Actividad),
    FOREIGN KEY (Dia, Hora_Inicio, Hora_Fin) REFERENCES proyecto_bd.Bloque_Horario(Dia, Hora_Inicio, Hora_Fin),
    FOREIGN KEY (ID_Actividad) REFERENCES proyecto_bd.Actividad_Extracurricular(ID_Actividad)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.asignaturaESTAENbloquehorario (
    Dia VARCHAR(10),
    Hora_Inicio TIME,
    Hora_Fin TIME,
    ID_Asignatura INT,
    PRIMARY KEY (Dia, Hora_Inicio, Hora_Fin, ID_Asignatura),
    FOREIGN KEY (Dia, Hora_Inicio, Hora_Fin) REFERENCES proyecto_bd.Bloque_Horario(Dia, Hora_Inicio, Hora_Fin),
    FOREIGN KEY (ID_Asignatura) REFERENCES proyecto_bd.Asignatura(ID_Asignatura)
);


-- CREAR FUNCIONES PARA REALIZAR CONSULTAS
-- Obtener nombre completo de persona