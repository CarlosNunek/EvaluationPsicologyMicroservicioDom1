from flask import Blueprint, request, jsonify
from services.evaluation_service import procesar_evaluacion

evaluation_bp = Blueprint('evaluation', __name__)

@evaluation_bp.route('/api/ingresar_evaluacion', methods=['POST'])
def ingresar_evaluacion():
    data = request.get_json()
    try:
        evaluacion_id = procesar_evaluacion(data)
        return jsonify({"mensaje": "Evaluación psicológica ingresada correctamente", "id": evaluacion_id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
