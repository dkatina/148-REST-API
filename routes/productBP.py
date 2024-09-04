from flask import Blueprint

from controllers.productController import save, find_all, search_product

product_blueprint = Blueprint("product_bp", __name__)

#where we put our url_endpoints
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/search', methods=['GET'])(search_product)