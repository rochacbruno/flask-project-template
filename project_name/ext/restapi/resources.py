from flask import abort, jsonify
from flask_restful import Resource
from flask_simplelogin import login_required

from project_name.models import Product


class ProductResource(Resource):
    def get(self):
        products = Product.query.all() or abort(204)
        return jsonify(
            {"products": [product.to_dict() for product in products]}
        )

    @login_required(basic=True, username="admin")
    def post(self):
        """
        Creates a new product.

        Only admin user authenticated using basic auth can post
        Basic takes base64 encripted username:password.

        # curl -XPOST localhost:5000/api/v1/product/ \
        #  -H "Authorization: Basic Y2h1Y2s6bm9ycmlz" \
        #  -H "Content-Type: application/json"
        """
        return NotImplementedError(
            "Someone please complete this example and send a PR :)"
        )


class ProductItemResource(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(404)
        return jsonify(product.to_dict())
