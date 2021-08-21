from flask import abort, render_template
from flask_simplelogin import login_required

from project_name.models import Product


def index():
    products = Product.query.all()
    return render_template("index.html", products=products)


def product(product_id):
    product = Product.query.filter_by(id=product_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("product.html", product=product)


@login_required
def secret():
    return "This can be seen only if user is logged in"


@login_required(username="admin")
def only_admin():
    return "only admin user can see this text"
