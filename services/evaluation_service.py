from repositories.evaluation_repository import almacenar_evaluacion_psicologica

def procesar_evaluacion(data):

     # Validaciones básicas de existencia
    campos_obligatorios = ['id_recluso', 'nivel_agresividad', 'trastornos']
    for campo in campos_obligatorios:
        if campo not in data or data[campo] is None:
            raise ValueError(f"El campo '{campo}' es obligatorio.")
        
    # Validaciones tal como tú las tienes
    if 'id_recluso' not in data or 'nivel_agresividad' not in data or 'trastornos' not in data:
        raise ValueError("Los campos 'id_recluso', 'nivel_agresividad' y 'trastornos' son obligatorios.")

    if not (1 <= data['nivel_agresividad'] <= 5):
        raise ValueError("El nivel de agresividad debe estar entre 1 y 5.")

    if not isinstance(data['trastornos'], list):
        raise ValueError("El campo 'trastornos' debe ser una lista de trastornos.")

    if 'estabilidad_emocional' in data and data['estabilidad_emocional'] not in ["Baja", "Media", "Alta"]:
        raise ValueError("El nivel de estabilidad emocional debe ser 'Baja', 'Media' o 'Alta'.")

    if 'observaciones' in data and not isinstance(data['observaciones'], str):
        raise ValueError("Las observaciones deben ser una cadena de texto.")

    if 'puntaje_psicologico' in data and not (0 <= data['puntaje_psicologico'] <= 100):
        raise ValueError("El puntaje psicológico debe estar entre 0 y 100.")

    if 'edad' in data and not isinstance(data['edad'], int):
        raise ValueError("La edad debe ser un número entero.")

    if 'riesgo_reincidencia' in data and not (0 <= data['riesgo_reincidencia'] <= 10):
        raise ValueError("El riesgo de reincidencia debe estar entre 0 y 10.")

    if 'tiempo_encarcelado' in data and not isinstance(data['tiempo_encarcelado'], int):
        raise ValueError("El tiempo encarcelado debe ser un número entero.")

    # Guardar en DB
    return almacenar_evaluacion_psicologica(data)
