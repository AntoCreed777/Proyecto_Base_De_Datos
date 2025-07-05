

-- Consulta para asignatura y profesores de un curso


-- Obtener nombre completo de persona
CREATE OR REPLACE FUNCTION proyecto_bd.obtener_nombre_completo(RUN_Persona VARCHAR(12))
RETURNS VARCHAR(100) AS $$
DECLARE
    nombre_completo VARCHAR(100);
BEGIN
    SELECT 
        (nc.Primer_nombre || ' ' || nc.Segundo_nombre || ' ' || nc.Apellido_paterno || ' ' || nc.Apellido_materno)::VARCHAR(100) INTO nombre_completo
    FROM proyecto_bd.Nombre_Completo nc
    WHERE nc.RUN_Persona = obtener_nombre_completo.RUN_Persona;

    RETURN nombre_completo;
END;

$$ LANGUAGE plpgsql;



-- Consulta para obtener el numero telefonico de una persona
CREATE OR REPLACE FUNCTION proyecto_bd.obtener_numero_telefonico(RUN_Persona VARCHAR(12))
RETURNS VARCHAR(20) AS $$
DECLARE
    numero_telefonico VARCHAR(20);
BEGIN
    SELECT 
        (nt.Codigo_del_pais || ' ' || nt.Codigo_del_area || ' ' || nt.Numero_unico)::VARCHAR(20) INTO numero_telefonico
    FROM proyecto_bd.Numero_Telefonico nt
    WHERE nt.RUN_Persona = obtener_numero_telefonico.RUN_Persona;
    RETURN numero_telefonico;
END;

$$ LANGUAGE plpgsql;


-- Consulta para obtener asignaturas y profesores de un curso

CREATE OR REPLACE FUNCTION proyecto_bd.obtener_asignaturas_y_docentes_curso(curso_id INT)
RETURNS TABLE(asignatura VARCHAR, docente VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        a.Nombre_Asignatura AS Asignatura, 
        proyecto_bd.obtener_nombre_completo(da.RUN_Docente) AS Docente

    FROM proyecto_bd.Asignatura a
    JOIN proyecto_bd.docenteDICTAasignatura da ON a.ID_Asignatura = da.ID_Asignatura
    WHERE a.ID_Curso = curso_id;
END;    

$$ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------

-- Consulta para obtener alumnos de un curso
CREATE OR REPLACE FUNCTION proyecto_bd.obtener_estudiantes_por_curso(curso_id INT)
RETURNS TABLE (Estudiante VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT proyecto_bd.obtener_nombre_completo(epc.RUN_Estudiante) AS Estudiante
        
    FROM proyecto_bd.Curso c
    JOIN proyecto_bd.estudiantePERTENECEcurso epc ON c.ID_Curso = epc.ID_Curso
    JOIN proyecto_bd.Nombre_Completo nc ON nc.RUN_Persona = epc.RUN_Estudiante
    WHERE c.ID_Curso = curso_id;
END;    

$$ LANGUAGE plpgsql;


-- Consulta para obtener el horario de las asignaturas de un curso
CREATE OR REPLACE FUNCTION proyecto_bd.obtener_horario_curso(curso_id INT)
RETURNS TABLE ( Nombre_Asignatura VARCHAR(100), Dia VARCHAR, Hora_Inicio TIME, Hora_Fin TIME) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        a.Nombre_asignatura,       
        b.Dia,
        b.Hora_Inicio,
        b.Hora_Fin
    FROM proyecto_bd.Curso c
    JOIN proyecto_bd.Asignatura a ON a.ID_Curso = c.ID_Curso
    JOIN proyecto_bd.asignaturaESTAENbloquehorario ab ON ab.ID_Asignatura = a.ID_Asignatura
    JOIN proyecto_bd.Bloque_Horario b ON ab.Dia = b.Dia and ab.Hora_Inicio = b.Hora_Inicio and ab.Hora_Fin = b.Hora_Fin
    WHERE c.ID_Curso = curso_id
    ORDER BY b.Dia, b.Hora_Inicio;
END;

$$ LANGUAGE plpgsql;


-- VER NOTAS DE ASIGNATURA DE CURSO

CREATE OR REPLACE FUNCTION proyecto_bd.obtener_notas_asignatura(ID_Asignatura INT) 
RETURNS TABLE (Estudiante VARCHAR, Nota NUMERIC) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        proyecto_bd.obtener_nombre_completo(re.RUN_Estudiante) AS Estudiante,
        re.Nota AS Nota
    FROM proyecto_bd.estudianteRINDEevaluacion re
    JOIN proyecto_bd.Evaluacion e ON re.ID_Evaluacion = e.ID_Evaluacion
    WHERE e.ID_Asignatura = obtener_notas_curso.ID_Asignatura;
END;

$$ LANGUAGE plpgsql;


-- Consulta datos apoderados de estudiante

CREATE OR REPLACE FUNCTION proyecto_bd.obtener_apoderados_estudiante(RUN_Estudiante VARCHAR(12))
RETURNS TABLE (Apoderado VARCHAR, Telefono VARCHAR, Relacion VARCHAR, Lugar_de_Trabajo VARCHAR, Profesion VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        proyecto_bd.obtener_nombre_completo(ar.RUN_Apoderado) AS Apoderado,
        proyecto_bd.obtener_numero_telefonico(ar.RUN_Apoderado) AS Telefono,
        ar.Relacion AS Relacion,
        a.Lugar_de_Trabajo AS Lugar_de_Trabajo,
        a.Profesion AS Profesion
    FROM proyecto_bd.apoderadoRESPONSABLEDEestudiante ar
    JOIN proyecto_bd.Apoderado a ON ar.RUN_Apoderado = a.RUN_Persona
    WHERE ar.RUN_Estudiante = obtener_apoderados_estudiante.RUN_Estudiante;
END;

$$ LANGUAGE plpgsql;


-- Obtener asistencia de curso a asignatura
CREATE OR REPLACE FUNCTION proyecto_bd.obtener_asistencia_curso(ID_Asignatura INT)
RETURNS TABLE (Estudiante VARCHAR(100), Asistencia VARCHAR(20), Fecha DATE, Hora TIME) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        proyecto_bd.obtener_nombre_completo(a.RUN_Estudiante) AS Estudiante,
        a.Estado AS Asistencia,
        a.Fecha AS Fecha,
        a.Hora_Inicio AS Hora
    FROM proyecto_bd.Asistencia a
    WHERE a.ID_Asignatura = obtener_asistencia_curso.ID_Asignatura;
END;

$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION proyecto_bd.obtener_info_familia(RUN_Estudiante VARCHAR(12))
RETURNS TABLE (
    ID_Familia INT,
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
) AS $$
DECLARE 
    familia_estudiante INT;
BEGIN 
    SELECT e.ID_Familia INTO familia_estudiante
	FROM proyecto_bd.Estudiante e
	WHERE e.RUN_Persona = RUN_Estudiante;

    RETURN QUERY
    SELECT *
    FROM proyecto_bd.Info_Familia i
    WHERE i.ID_Familia = familia_estudiante;
END;

$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION proyecto_bd.obtener_docente_dicta_asignatura(RUN_Docente VARCHAR(12))
RETURNS TABLE (ID_Asignatura INT, Asignatura VARCHAR(100), Curso VARCHAR(4)) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        a.ID_Asignatura AS ID_Asignatura,
        a.Nombre_asignatura AS Asignatura,
        (c.Grado || ' ' || c.Letra)::VARCHAR(4) AS Curso,

    FROM proyecto_bd.docenteDICTAasignatura dda
    JOIN proyecto_bd.asignatura a ON a.ID_Asignatura = dda.ID_Asignatura
    JOIN proyecto_bd.Curso c ON c.ID_Curso = a.ID_Curso
    WHERE dda.RUN_Docente = obtener_docente_dicta_asignatura.RUN_Docente;
END;

$$ LANGUAGE plpgsql



-- PENDIENTE:

-- X - Consulta y emision del compendio de notas del Alumno.
-- X - Consulta del horario de un curso.
-- X - Consulta de las Asignaturas y Profesores de un curso.
-- X - Consulta de los Alumnos pertenecientes a un curso.
-- X - Emision de la lista de Alumnos de un curso.
-- X - Consulta de informacion de un Alumno.
-- X - Emision del Informe de asistencia a las distintas Asignaturas.

-- X Consulta sobre informacion de la familia del Alumno.
-- X Consulta de los datos de un Profesor
-- - Ingreso de Notas restringido por docentes.
