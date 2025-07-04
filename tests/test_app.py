import json
import pytest
from app import app
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_mongo():
    with patch("app.mongo") as mock:
        mock_insert_result = MagicMock()
        mock_insert_result.inserted_id = "fake_id_123"
        mock.db.evaluaciones_psicologicas.insert_one.return_value = mock_insert_result
        yield mock

def test_ingresar_evaluacion_exito(client, mock_mongo):
    payload = {
        "id_recluso": "1725279812",
        "nivel_agresividad": 4,
        "trastornos": "Transtorno de personalidad, Transtorno de depresion",
        "estabilidad_emocional": "Alta",
        "riesgo_reincidencia": 8,
        "tiempo_encarcelado": 24,
        "puntaje_psicologico": 85,
        "edad": 30,
        "observaciones": "Requiere tratamiento"
    }

    response = client.post("/api/ingresar_evaluacion",
                           data=json.dumps(payload),
                           content_type="application/json")

    assert response.status_code == 200
    data = response.get_json()
    assert "id" in data
    assert data["id"] == "fake_id_123"
