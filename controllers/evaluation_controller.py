from flask import Blueprint, request, jsonify
from services.evaluation_service import procesar_evaluacion
from config.mongo import mongo

evaluation_bp = Blueprint('evaluation', __name__)

@evaluation_bp.route('/api/ingresar_evaluacion', methods=['POST'])
def ingresar_evaluacion():
    data = request.get_json()
    try:
        evaluacion_id = procesar_evaluacion(data)
        return jsonify({"mensaje": "Evaluación psicológica ingresada correctamente", "id": evaluacion_id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@evaluation_bp.route('/api/evaluacion/<cedula>', methods=['GET'])
def obtener_evaluacion_por_cedula(cedula):
    try:
        evaluacion = mongo.db.evaluaciones_psicologicas.find_one({"id_recluso": cedula})
        if evaluacion:
            evaluacion["_id"] = str(evaluacion["_id"])  # convertir ObjectId a string
            return jsonify(evaluacion), 200
        else:
            return jsonify({"error": "Evaluación no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500