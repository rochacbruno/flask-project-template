from flask import Flask
from dynaconf import FlaskDynaconf


def create_app(**config):
    app = Flask(__name__)
    FlaskDynaconf(app)  # config managed by Dynaconf
    app.config.load_extensions(
        "EXTENSIONS"
    )  # Load extensions from settings.toml
    app.config.update(config)  # Override with passed config
    return app
