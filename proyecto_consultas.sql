-- Consulta para asignatura y profesores de un curso

CREATE OR REPLACE FUNCTION proyecto_bd.obtener_asignaturas_y_profesores(curso_id INT)
RETURNS TABLE(asignatura VARCHAR, docente VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        a.nombre AS Asignatura, 
        (nc.nombre || ' ' || nc.Apellido_paterno || ' ' || nc.Apellido_materno)::VARCHAR AS Docente
        
    FROM proyecto_bd.Asignatura a
    JOIN proyecto_bd.docenteDICTAasignatura da ON a.ID_Asignatura = da.ID_Asignatura
    JOIN proyecto_bd.Docente d ON d.ID_Persona = da.Id_Docente
    JOIN proyecto_bd.Persona p ON p.RUN = d.ID_Persona
    JOIN proyecto_bd.Nombre_Completo nc ON p.RUN = nc.RUN_Persona
    WHERE a.ID_Curso = curso_id;
END;    

$$ LANGUAGE plpgsql;

SELECT * FROM proyecto_bd.obtener_asignaturas_y_profesores(1); -- Retorna la asignatura y docente del curso con ID 1