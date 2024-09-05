from flask import Blueprint
from controllers.customerController import save, find_all, login


customer_blueprint = Blueprint('customer_bp', __name__)

#url_prefix for this blueprint is /customers

customer_blueprint.route('/', methods=['POST'])(save) #triggers the save function on POST request to /customers
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/login', methods=["POST"])(login)
