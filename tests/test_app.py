import json
import pytest
from app import app
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_ingresar_evaluacion_exito(client):
    payload = {
        "id_recluso": "1234567890",
        "nivel_agresividad": "alto",
        "trastornos": "ninguno",
        "estabilidad_emocional": "estable",
        "riesgo_reincidencia": "bajo",
        "tiempo_entre_rejas": 24,
        "puntaje_psicologico": 85,
        "edad": 30
    }
    response = client.post("/api/ingresar_evaluacion",
                           data=json.dumps(payload),
                           content_type="application/json")
    assert response.status_code == 200
    assert "id" in response.get_json()

def test_ingresar_evaluacion_faltante(client):
    payload = {
        "nivel_agresividad": "medio",  # Falta 'id_recluso'
        "trastornos": "ansiedad"
    }
    response = client.post("/api/ingresar_evaluacion",
                           data=json.dumps(payload),
                           content_type="application/json")
    assert response.status_code == 400 or response.status_code == 200
    data = response.get_json()
    assert "error" in data
