import pytest
from unittest.mock import patch, MagicMock
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ingresar_evaluacion_exito(client):
    payload = {
        "id_recluso": "1725279812",
        "nivel_agresividad": 4,
        "trastornos": ["Transtorno de personalidad, Transtorno de depresion"],
        "estabilidad_emocional": "Alta",
        "riesgo_reincidencia": 8,
        "tiempo_encarcelado": 24,
        "puntaje_psicologico": 85,
        "edad": 30,
        "observaciones": "Requiere tratamiento"
    }

    # Parcheamos el insert_one donde realmente se usa: en evaluation_repository
    with patch("repositories.evaluation_repository.mongo") as mock_mongo:
        mock_mongo.db.evaluaciones_psicologicas.insert_one.return_value.inserted_id = "fake_id_123"

        response = client.post("/api/ingresar_evaluacion", json=payload)

        assert response.status_code == 201
        data = response.get_json()
        assert data["id"] == "fake_id_123"

