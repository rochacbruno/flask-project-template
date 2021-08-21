from flask import Blueprint

from .views import index, product, secret

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule(
    "/product/<product_id>", view_func=product, endpoint="productview"
)
bp.add_url_rule("/secret", view_func=secret, endpoint="secret")


def init_app(app):
    app.register_blueprint(bp)
