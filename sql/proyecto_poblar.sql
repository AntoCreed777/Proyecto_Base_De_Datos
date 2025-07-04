-- Script para poblar la base de datos del proyecto

INSERT INTO proyecto_bd.Genero (Nombre_Genero) VALUES 
    ('Masculino'),
    ('Femenino'),
    ('No Binario'),
    ('Otro');

INSERT INTO proyecto_bd.Nacionalidad (Pais) VALUES 
    ('Chile'),
    ('Argentina'),
    ('Perú'),
    ('Brasil'),
    ('Uruguay');

INSERT INTO proyecto_bd.Religion (Nombre_Religion)  
VALUES
    ('Católica'),
    ('Evangélica'),
    ('Judía'),
    ('Musulmana'),
    ('Atea'),
    ('Agnóstica');

INSERT INTO proyecto_bd.Persona 
(RUN_Persona, Contraseña, Fecha_de_nacimiento, ID_Genero, ID_Nacionalidad, ID_Religion) 
VALUES 
    ('12345670-k', 'pass0secure', '2001-01-01', 1, 1, 1), -- APODERADO
    ('12345671-k', 'pass1secure', '2002-02-02', 2, 2, 2), -- APODERADO
    ('12345672-k', 'pass2secure', '2003-03-03', 3, 3, 3), -- APODERADO
    ('12345673-k', 'pass3secure', '2004-04-04', 4, 4, 4), -- APODERADO
    ('12345674-k', 'pass4secure', '1980-05-05', 1, 5, 5), -- DOCENTE
    ('12345675-k', 'pass5secure', '1981-06-06', 2, 1, 1), -- DOCENTE
    ('12345676-k', 'pass6secure', '1990-07-07', 3, 2, 2), -- FUNCIONARIO
    ('12345677-k', 'pass7secure', '1991-08-08', 4, 3, 3), -- FUNCIONARIO
    ('12345678-k', 'pass8secure', '2005-09-09', 1, 4, 4), -- ESTUDIANTE
    ('12345679-k', 'pass9secure', '2006-10-10', 2, 5, 5); -- ESTUDIANTE

INSERT INTO proyecto_bd.Nombre_Completo 
(RUN_Persona, Primer_nombre, Segundo_nombre, Apellido_paterno, Apellido_materno) 
VALUES 
    ('12345670-k', 'Valentina', 'Maria', 'González', 'Pérez'), --APODERADO
    ('12345671-k', 'Mateo', 'José', 'Muñoz', 'Rojas'),        --APODERADO
    ('12345672-k', 'Isidora', 'Fernanda', 'Díaz', 'Fernández'),   --APODERADO
    ('12345673-k', 'Benjamín', 'Alejandro', 'Soto', 'Morales'),    --APODERADO
    ('12345674-k', 'Florencia', 'Ignacia', 'Silva', 'Castillo'), --DOCENTE
    ('12345675-k', 'Tomás', 'Andrés', 'Ramírez', 'Gutiérrez'),  --DOCENTE
    ('12345676-k', 'Camila', 'Carmela', 'Torres', 'Reyes'),      --FUNCIONARIO
    ('12345677-k', 'Lucas', 'Sebastian', 'Martínez', 'Vargas'),    --FUNCIONARIO
    ('12345678-k', 'Josefa', 'Amanda', 'Contreras', 'López'),   --ESTUDIANTE
    ('12345679-k', 'Agustín', 'Raúl', 'Espinoza', 'Herrera'); --ESTUDIANTE

INSERT INTO proyecto_bd.Numero_Telefonico 
(RUN_Persona, Codigo_del_pais, Codigo_del_area, Numero_unico)
VALUES 
('12345670-k', 56, 2, 12345678),
('12345671-k', 56, 2, 23456789),
('12345672-k', 56, 2, 34567890),
('12345673-k', 56, 2, 45678901),
('12345674-k', 56, 2, 56789012),
('12345675-k', 56, 2, 67890123),
('12345676-k', 56, 2, 78901234),
('12345677-k', 56, 2, 89012345),
('12345678-k', 56, 2, 90123456),
('12345679-k', 56, 2, 11223344);

INSERT INTO proyecto_bd.Lugar_de_Residencia 
(RUN_Persona, Region, Ciudad, Comuna, Calle, Numero_casa, Numero_dpt)
VALUES 
('12345678-k', 'Región de O’Higgins', 'Rancagua', 'Machalí', 'Calle San Martín', 9202, 909),
('12345670-k', 'Región Metropolitana', 'Santiago', 'Providencia', 'Avenida Providencia', 1234, 101),
('12345671-k', 'Región de Valparaíso', 'Valparaíso', 'Viña del Mar', 'Avenida Libertad', 5678, 202),
('12345672-k', 'Región del Biobío', 'Concepción', 'Chiguayante', 'Calle Colón', 9101, 303),
('12345673-k', 'Región de La Araucanía', 'Temuco', 'Padre Las Casas', 'Calle Balmaceda', 1121, 404),
('12345674-k', 'Región de Los Lagos', 'Puerto Montt', 'Puerto Varas', 'Calle San Pedro', 3141, 505), 
('12345675-k', 'Región de Magallanes', 'Punta Arenas', 'Puerto Natales', 'Calle Costanera', 5161, 606),
('12345676-k', 'Región de Antofagasta', 'Antofagasta', 'Calama', 'Calle Prat', 7181, 707),
('12345677-k', 'Región de Coquimbo', 'La Serena', 'Coquimbo', 'Calle Balmaceda', 8191, 808),
('12345679-k', 'Región del Maule', 'Talca', 'Curicó', 'Calle Libertador Bernardo O’Higgins', 1023, 1010);

INSERT INTO proyecto_bd.Apoderado 
(RUN_Persona, Profesion, Lugar_de_Trabajo)
VALUES 
('12345670-k', 'Contadora', 'Empresa ABC'),
('12345671-k', 'Educador Diferencial', 'Instituto XYZ'),
('12345672-k', 'Médica', 'Hospital Local'),
('12345673-k', 'Secretario Académico', 'Universidad Nacional');


INSERT INTO proyecto_bd.Docente
(RUN_Persona)
VALUES
('12345674-k'), -- Docente Florencia
('12345675-k'); -- Docente Tomás

INSERT INTO proyecto_bd.Info_Familia(
    Nombre_Familia,
    Cuantos_Trabajan,
    Ocupacion_Padres,
    Numero_Integrantes,
    Cantidad_Dormitorios,
    Cantidad_Baños,
    Baños_Compartidos,
    Energia,                -- Red electrica, Otro suministro, Sin electricidad.
    Tipo_Agua,              -- Agua potable, Pozo, Otro suministro.
    Tipo_Construccion,      -- Casa solida, Casa Madera, Departamento, Arriendo, Mediagua.
    Propiedad,              -- Propia, cedida, arrendada, allegados.
    Estado_Marital_Padres,  -- Casado, Separados, Anulado, Convivientes, Viudo(a), Solteros, Divorciados.
    Estado_Vida_Padres,     -- Ambos Vivos, Ambos Muertos, Solo el Padre Vivo, Solo la Madre Viva.
    Ingresos_Mensuales
) VALUES 
('Familia González', 2, 'Ingeniero y Profesora', 4, 3, 2, TRUE,'Red eléctrica', 'Agua potable', 'Casa sólida', 'Propia', 'Casados', 'Ambos Vivos', 800000),
('Familia Muñoz', 1, 'Médico', 1, 2, 1, FALSE, 'Red eléctrica', 'Agua potable', 'Departamento', 'Arrendada', 'Convivientes', 'Solo el Padre Vivo', 600000);

INSERT INTO proyecto_bd.Estudiante(
    RUN_Persona, 
    ID_Familia, 
    Año_de_Ingreso, 
    Numero_de_Matricula,
    Foto,
    Fecha_Matricula,
    Estado_Academico, -- Vigente, Egresado, Reiterado, Eliminado, Prematriculado, Congelado.
    Semestre_de_Ingreso -- 1°Semestre y 2°Semestre.
    
) VALUES 
('12345678-k', 1, 2020, '2020-001', NULL, '2020-01-15', 'Vigente', 1),
('12345679-k', 2, 2021, '2021-002', NULL, '2021-02-20', 'Vigente', 2);

INSERT INTO proyecto_bd.Sala (Nombre_Sala) VALUES 
('Sala 101'),
('Sala 102'),
('Sala 103'),
('Sala 104'),
('Sala 105');

INSERT INTO proyecto_bd.Curso(
    RUN_Docente, 
    ID_Sala, 
    Año, 
    Semestre, 
    Grado, 
    Letra
) VALUES 
('12345674-k', 1, 2020, 1, 1, 'A'), -- Curso
('12345675-k', 2, 2020, 2, 2, 'B'), -- Curso
('12345674-k', 3, 2021, 1, 3, 'C'); -- Curso

INSERT INTO proyecto_bd.Asignatura (ID_Curso, Nombre_asignatura) VALUES 
('1', 'Matemáticas'),
('2', 'Lenguaje y Comunicación'),
('3', 'Ciencias Naturales'),
('1', 'Historia y Geografía'),
('2', 'Educación Física');

INSERT INTO proyecto_bd.Evaluacion(
    RUN_Docente, 
    ID_Asignatura, 
    Fecha_Evaluacion, 
    Ponderacion
) VALUES 
('12345674-k', 1, '2020-03-01', 0.3), -- Docente Florencia
('12345675-k', 2, '2020-03-02', 0.4), -- Docente Tomás
('12345674-k', 3, '2020-03-03', 0.2), -- Docente Florencia
('12345675-k', 4, '2020-03-04', 0.5); -- Docente Tomás


INSERT INTO proyecto_bd.Bloque_Horario (
    Dia,
    Hora_Inicio, 
    Hora_Fin 
) VALUES 
('Lunes', '08:00:00', '10:00:00'),
('Lunes', '10:30:00', '12:30:00'),
('Martes', '08:00:00', '10:00:00'),
('Martes', '10:30:00', '12:30:00'),
('Miércoles', '08:00:00', '10:00:00'),
('Miércoles', '10:30:00', '12:30:00'),
('Jueves', '08:00:00', '10:00:00'),
('Jueves', '10:30:00', '12:30:00'),
('Viernes', '08:00:00', '10:00:00'),
('Viernes', '10:30:00', '12:30:00');

INSERT INTO proyecto_bd.Asistencia(
    RUN_Estudiante, 
    ID_Asignatura, 
    Estado, 
    Fecha, 
    Dia, 
    Hora_Inicio, 
    Hora_Fin
) VALUES 
('12345678-k', 1, 'Presente', '2020-03-01', 'Lunes', '08:00:00', '10:00:00'),
('12345679-k', 2, 'Ausente', '2020-03-02', 'Martes', '10:30:00', '12:30:00'),
('12345678-k', 3, 'Presente', '2020-03-03', 'Miércoles', '08:00:00', '10:00:00'),
('12345679-k', 4, 'Presente', '2020-03-04', 'Jueves', '10:30:00', '12:30:00');

INSERT INTO proyecto_bd.Justificacion(
    ID_Asistencia, 
    Descripcion_Justificacion
) VALUES 
(1, 'Falta por enfermedad'),
(2, 'Falta por viaje familiar'),
(3, 'Falta por compromiso personal'),
(4, 'Falta por motivo académico');

INSERT INTO proyecto_bd.Actividad_Extracurricular( 
        ID_Sala, 
        Nombre_Actividad
    ) VALUES 
    (1, 'Fútbol'),
    (2, 'Banda Escolar'),
    (3, 'Teatro'),
    (4, 'Coro'),
    (5, 'Robótica');

INSERT INTO proyecto_bd.Reporte_Accidente(
    RUN_Estudiante, 
    Descripcion_Accidente,
    Fecha
) VALUES 
('12345678-k', 'Caída en el patio durante el recreo', '2020-03-01'),
('12345679-k', 'Lesión en la clase de educación física', '2021-03-02');

INSERT INTO proyecto_bd.Anotacion(
    RUN_Estudiante, 
    Descripcion_Anotacion, 
    Tipo_Anotacion -- Positiva, Negativa.
) VALUES 
('12345678-k', 'Excelente participación en clase', 'Positiva'),
('12345679-k', 'Falta de respeto a un compañero', 'Negativa');

INSERT INTO proyecto_bd.estudianteTOMAactividad(
    RUN_Estudiante, 
    ID_Actividad
) VALUES 
('12345678-k', 1), -- Estudiante toma actividad Fútbol
('12345679-k', 2); -- Estudiante toma actividad Banda Escolar

INSERT INTO proyecto_bd.estudianteRINDEevaluacion(
    RUN_Estudiante, 
    ID_Evaluacion, 
    Nota
) VALUES 
('12345678-k', 1, 6.5), -- Estudiante rinde evaluación
('12345679-k', 2, 5.0); -- Estudiante rinde evaluación

INSERT INTO proyecto_bd.estudiantePERTENECEcurso(
    RUN_Estudiante, 
    ID_Curso
) VALUES 
('12345678-k', 1), -- Estudiante pertenece al curso 1
('12345679-k', 2); -- Estudiante pertenece al curso 2

INSERT INTO proyecto_bd.apoderadoRESPONSABLEDEestudiante(
    RUN_Estudiante, 
    RUN_Apoderado, 
    Relacion -- Padre, Madre, Hermano, Tío, etc.    
) VALUES 
('12345678-k', '12345670-k', 'Padre'), -- Apoderado responsable del estudiante
('12345679-k', '12345671-k', 'Madre'); -- Apoderado responsable del estudiante

INSERT INTO proyecto_bd.docenteDICTAasignatura(
    ID_Asignatura,
    RUN_Docente
) VALUES 
    (1, '12345674-k'), -- Docente asigna asignatura Matemáticas
    (2, '12345675-k'), -- Docente asigna asignatura Lenguaje y Comunicación
    (3, '12345674-k'), -- Docente asigna asignatura Ciencias Naturales
    (4, '12345675-k'); -- Docente asigna asignatura Historia y Geografía

INSERT INTO proyecto_bd.docenteACARGOactividad(
    ID_Actividad, 
    RUN_Docente
) VALUES 
(1, '12345674-k'), -- Docente a cargo de la actividad Fútbol
(2, '12345675-k'); -- Docente a cargo de la actividad Banda Escolar

INSERT INTO proyecto_bd.actividadESTAENELbloquehorario(
    ID_Actividad, 
    Dia,
    Hora_Inicio,
    Hora_Fin
) VALUES 
(1, 'Lunes', '08:00:00', '10:00:00'), -- Actividad Fútbol en bloque horario
(2, 'Martes', '10:30:00', '12:30:00'); -- Actividad Banda Escolar en bloque horario

INSERT INTO proyecto_bd.asignaturaESTAENbloquehorario(
    ID_Asignatura, 
    Dia,
    Hora_Inicio,
    Hora_Fin
) VALUES 
(3, 'Miércoles', '08:00:00', '10:00:00'), -- Asignatura Ciencias Naturales en bloque horario
(4, 'Jueves', '10:30:00', '12:30:00'), -- Asignatura Historia y Geografía en bloque horario
(5, 'Viernes', '08:00:00', '10:00:00'); -- Asignatura Educación Física en bloque horario
