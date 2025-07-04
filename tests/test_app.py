import json
import pytest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_insert_one():
    with patch("config.mongo.mongo.db.evaluaciones_psicologicas.insert_one") as mock_insert:
        mock_insert.return_value.inserted_id = "fake_id_123"
        yield mock_insert

def test_ingresar_evaluacion_exito(client, mock_insert_one):
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

    response = client.post("/api/ingresar_evaluacion", json=payload)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.get_json())

    assert response.status_code == 200
    data = response.get_json()
    assert "id" in data
    assert data["id"] == "fake_id_123"