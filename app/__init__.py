from flask import Flask
from flask_sqlalchemy import SQLALCHEMY
from config import Config
import os


db = SQLALCHEMY()


def create_app(config_object=Config):
    app = Flask(__name__)

    app.config.from_object(config_object)

    db.init(app)

    return app
