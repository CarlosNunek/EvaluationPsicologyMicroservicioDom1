from flask_pymongo import PyMongo

mongo = PyMongo()

def init_mongo(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/evaluaciones_psicologicas_db"
    mongo.init_app(app)
