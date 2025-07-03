from config.mongo import mongo

def almacenar_evaluacion_psicologica(data):
    evaluacion = mongo.db.evaluaciones_psicologicas.insert_one(data)
    return str(evaluacion.inserted_id)
