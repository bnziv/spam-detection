from flask import Flask
from flask_cors import CORS
from app.routes import api

def create_app():
    """
    Create a Flask application
    """
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(api, url_prefix='/api')

    return app