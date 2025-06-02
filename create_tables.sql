CREATE OR REPLACE SCHEMA proyecto_bd;

CREATE TABLE IF NOT EXISTS proyecto_bd.Persona (
    RUN VARCHAR(12) PRIMARY KEY,
    Contraseña VARCHAR(255) NOT NULL,
    Fecha_de_nacimiento DATE NOT NULL,
    ID_Religión INT,
    ID_Genero INT,
    ID_Nacionalidad INT,
    FOREIGN KEY (ID_Religión) REFERENCES Religión(ID_Religión),
    FOREIGN KEY (ID_Genero) REFERENCES Genero(ID_Genero),
    FOREIGN KEY (ID_Nacionalidad) REFERENCES Nacionalidad(ID_Nacionalidad)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Numero_Telefonico (
    RUN_Persona VARCHAR(12),
    Codigo_del_pais INT NOT NULL,
    Codigo_del_area INT NOT NULL,
    Numero_unico BIGINT NOT NULL,
    PRIMARY KEY (RUN_Persona, Codigo_del_pais, Codigo_del_area, Numero_unico),
    FOREIGN KEY (RUN_Persona) REFERENCES Persona(RUN)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Lugar_de_Residencia (
    RUN_Persona VARCHAR(12) PRIMARY KEY,
    Region VARCHAR(100),
    Ciudad VARCHAR(100),
    Comuna VARCHAR(100),
    Calle VARCHAR(100),
    Numero_casa INT,
    Numero_dpt INT,
    FOREIGN KEY (RUN_Persona) REFERENCES Persona(RUN)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Nombre_Completo (
    RUN_Persona VARCHAR(12) PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido_paterno VARCHAR(50),
    Apellido_materno VARCHAR(50),
    FOREIGN KEY (RUN_Persona) REFERENCES Persona(RUN)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Genero (
    ID_Genero SERIAL PRIMARY KEY,
    Nombre_Genero VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Nacionalidad (
    ID_Nacionalidad SERIAL PRIMARY KEY,
    Pais VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Religión (
    ID_Religión SERIAL PRIMARY KEY,
    Nombre_Religión VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Apoderado (
    ID_Persona VARCHAR(12) PRIMARY KEY,
    Profesión VARCHAR(100),
    Lugar_de_Trabajo VARCHAR(255),
    FOREIGN KEY (ID_Persona) REFERENCES Persona(RUN)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Direccion_de_Trabajo (
    ID_Apoderado VARCHAR(12) PRIMARY KEY,
    Region VARCHAR(100),
    Ciudad VARCHAR(100),
    Comuna VARCHAR(100),
    Calle VARCHAR(100),
    Numero_Casa INT,
    Numero_Dpt INT,
    FOREIGN KEY (ID_Apoderado) REFERENCES Apoderado(ID_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Numero_Telefonico_Trabajo (
    ID_Apoderado VARCHAR(12),
    Codigo_del_Pais INT,
    Codigo_del_Area INT,
    Numero_Unico BIGINT,
    PRIMARY KEY (ID_Apoderado, Codigo_del_Pais, Codigo_del_Area, Numero_Unico),
    FOREIGN KEY (ID_Apoderado) REFERENCES Apoderado(ID_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Funcionario (
    ID_Persona VARCHAR(12) PRIMARY KEY,
    Titulo_Academico VARCHAR(100),
    Cargo VARCHAR(50),
    Rol VARCHAR(50),
    FOREIGN KEY (ID_Persona) REFERENCES Persona(RUN)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Docente (
    ID_Persona VARCHAR(12) PRIMARY KEY,
    FOREIGN KEY (ID_Persona) REFERENCES Persona(RUN)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Evaluacion (
    ID_Evaluacion SERIAL PRIMARY KEY,
    ID_Docente VARCHAR(12),
    ID_Asignatura INT,
    Fecha_Evaluacion DATE NOT NULL,
    Ponderacion FLOAT NOT NULL,
    FOREIGN KEY (ID_Docente) REFERENCES Docente(ID_Persona),
    FOREIGN KEY (ID_Asignatura) REFERENCES Asignatura(ID_Asignatura)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Asignatura (
    ID_Asignatura SERIAL PRIMARY KEY,
    Nombre VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Bloque_Horario (
    Dia VARCHAR(10),
    Hora_Inicio TIME,
    Hora_Fin TIME,
    PRIMARY KEY (Dia, Hora_Inicio, Hora_Fin)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Asistencia (
    ID_Asistencia SERIAL PRIMARY KEY,
    ID_Estudiante VARCHAR(12),
    ID_Asignatura INT,
    Estado VARCHAR(20),
    Fecha DATE,
    Dia VARCHAR(10),
    Hora_Inicio TIME,
    Hora_Fin TIME,
    FOREIGN KEY (ID_Estudiante) REFERENCES Estudiante(ID_Persona),
    FOREIGN KEY (ID_Asignatura) REFERENCES Asignatura(ID_Asignatura),
    FOREIGN KEY (Dia, Hora_Inicio, Hora_Fin) REFERENCES Bloque_Horario(Dia, Hora_Inicio, Hora_Fin)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Justificación (
    ID_Justificación SERIAL PRIMARY KEY,
    ID_Asistencia INT NOT NULL,
    Descripción_Justificación TEXT,
    FOREIGN KEY (ID_Asistencia) REFERENCES Asistencia(ID_Asistencia)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Curso (
    ID_Curso SERIAL PRIMARY KEY,
    ID_Docente VARCHAR(12),
    ID_Sala INT,
    Año INT NOT NULL,
    Semestre INT NOT NULL,
    Grado INT,
    Letra CHAR(1),
    FOREIGN KEY (ID_Docente) REFERENCES Docente(ID_Persona),
    FOREIGN KEY (ID_Sala) REFERENCES Sala(ID_Sala)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.ActividadExtracurricular (
    ID_Actividad SERIAL PRIMARY KEY,
    ID_Sala INT,
    Nombre_Actividad VARCHAR(100),
    FOREIGN KEY (ID_Sala) REFERENCES Sala(ID_Sala)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Sala (
    ID_Sala SERIAL PRIMARY KEY,
    Nombre_Sala VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Estudiante (
    ID_Persona VARCHAR(12) PRIMARY KEY,
    ID_Familia INT,
    Año_de_Ingreso INT NOT NULL,
    Número_de_Matrícula VARCHAR(50),
    Foto BYTEA,
    Fecha_Matricula DATE,
    Estado_Académico VARCHAR(50),
    Semestre_de_Ingreso INT,
    FOREIGN KEY (ID_Persona) REFERENCES Persona(RUN),
    FOREIGN KEY (ID_Familia) REFERENCES Info_Familia(ID_Familia)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Info_Familia (
    ID_Familia SERIAL PRIMARY KEY,
    Nombre_Familia VARCHAR(100),
    Cuantos_Trabajan INT,
    Cantidad_Dormitorios INT,
    Cantidad_Baños INT,
    Baños_Compartidos BOOLEAN,
    Número_Integrantes INT,
    Tipo_Agua VARCHAR(50),
    Ocupación_Padre VARCHAR(100),
    Ocupación_Madre VARCHAR(100),
    Energía VARCHAR(50),
    Estado_Marital_Padres VARCHAR(50),
    Estado_Vida_Padre VARCHAR(50),
    Estado_Vida_Madre VARCHAR(50),
    Tipo_Construcción VARCHAR(50),
    Propiedad VARCHAR(50),
    Ingresos_Mensuales BIGINT
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Reporte_Accidente (
    ID_Reporte SERIAL PRIMARY KEY,
    ID_Estudiante VARCHAR(12),
    Descripción TEXT,
    Fecha DATE NOT NULL,
    FOREIGN KEY (ID_Estudiante) REFERENCES Estudiante(ID_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.Anotación (
    ID_Anotación SERIAL PRIMARY KEY,
    ID_Estudiante VARCHAR(12),
    Descripción TEXT,
    Tipo_Anotación VARCHAR(50),
    FOREIGN KEY (ID_Estudiante) REFERENCES Estudiante(ID_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.estudianteTOMAactividad (
    ID_Estudiante VARCHAR(12),
    ID_Actividad INT,
    PRIMARY KEY (ID_Estudiante, ID_Actividad),
    FOREIGN KEY (ID_Estudiante) REFERENCES Estudiante(ID_Persona),
    FOREIGN KEY (ID_Actividad) REFERENCES ActividadExtracurricular(ID_Actividad)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.estudianteRINDEevaluación (
    ID_Estudiante VARCHAR(12),
    ID_Evaluación INT,
    Nota NUMERIC(5, 2),
    PRIMARY KEY (ID_Estudiante, ID_Evaluación),
    FOREIGN KEY (ID_Estudiante) REFERENCES Estudiante(ID_Persona),
    FOREIGN KEY (ID_Evaluación) REFERENCES Evaluacion(ID_Evaluacion)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.estudiantePERTENECEcurso (
    ID_Estudiante VARCHAR(12),
    ID_Curso INT,
    PRIMARY KEY (ID_Estudiante, ID_Curso),
    FOREIGN KEY (ID_Estudiante) REFERENCES Estudiante(ID_Persona),
    FOREIGN KEY (ID_Curso) REFERENCES Curso(ID_Curso)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.apoderadoRESPONSABLEDEestudiante (
    ID_Estudiante VARCHAR(12),
    ID_Apoderado VARCHAR(12),
    Relación VARCHAR(50),
    PRIMARY KEY (ID_Estudiante, ID_Apoderado),
    FOREIGN KEY (ID_Estudiante) REFERENCES Estudiante(ID_Persona),
    FOREIGN KEY (ID_Apoderado) REFERENCES Apoderado(ID_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.docenteDICTAasignatura (
    ID_Curso INT,
    ID_Docente VARCHAR(12),
    PRIMARY KEY (ID_Curso, ID_Docente),
    FOREIGN KEY (ID_Curso) REFERENCES Curso(ID_Curso),
    FOREIGN KEY (ID_Docente) REFERENCES Docente(ID_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.docenteACARGOactividad (
    ID_Actividad INT,
    ID_Docente VARCHAR(12),
    PRIMARY KEY (ID_Actividad, ID_Docente),
    FOREIGN KEY (ID_Actividad) REFERENCES ActividadExtracurricular(ID_Actividad),
    FOREIGN KEY (ID_Docente) REFERENCES Docente(ID_Persona)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.actividadESTAENELbloquehorario (
    Día VARCHAR(10),
    Hora_Inicio TIME,
    Hora_Fin TIME,
    ID_Actividad INT,
    PRIMARY KEY (Día, Hora_Inicio, Hora_Fin, ID_Actividad),
    FOREIGN KEY (Día, Hora_Inicio, Hora_Fin) REFERENCES Bloque_Horario(Día, Hora_Inicio, Hora_Fin),
    FOREIGN KEY (ID_Actividad) REFERENCES ActividadExtracurricular(ID_Actividad)
);

CREATE TABLE IF NOT EXISTS proyecto_bd.asignaturaESTAENbloquehorario (
    Día VARCHAR(10),
    Hora_Inicio TIME,
    Hora_Fin TIME,
    ID_Asignatura INT,
    PRIMARY KEY (Día, Hora_Inicio, Hora_Fin, ID_Asignatura),
    FOREIGN KEY (Día, Hora_Inicio, Hora_Fin) REFERENCES Bloque_Horario(Día, Hora_Inicio, Hora_Fin),
    FOREIGN KEY (ID_Asignatura) REFERENCES Asignatura(ID_Asignatura)
);
