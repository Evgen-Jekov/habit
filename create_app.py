from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import Config
from app.connect.extension.extension import connect_extension

def create() -> Flask:
    app = Flask(__name__)
    cors = CORS(app, resources={r"/": {"origins": "http://127.0.0.1:5000"}})
    api = Api(app)

    app.config.from_object(Config)
    connect_extension(app=app)

    return app