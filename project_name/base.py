from dynaconf import FlaskDynaconf
from flask import Flask


def create_app(**config):
    app = Flask(__name__)
    FlaskDynaconf(app, **config)  # config managed by Dynaconf
    app.config.load_extensions(
        "EXTENSIONS"
    )  # Load extensions from settings.toml
    app.config.update(config)  # Override with passed config
    return app
