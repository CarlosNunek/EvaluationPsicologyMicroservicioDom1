from flask import Flask, request, jsonify
from config.mongo import init_mongo
from flask_cors import CORS
from controllers.evaluation_controller import evaluation_bp

app = Flask(__name__)
CORS(app)

# Inicializar Mongo
init_mongo(app)

# Registrar rutas
app.register_blueprint(evaluation_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)