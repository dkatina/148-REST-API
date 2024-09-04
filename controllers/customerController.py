from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from cache import cache


def save(): #name the controller the same as the service it recruites

    try:
        customer_data = customer_schema.load(request.json)
    
    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    
    customer = customerService.save(customer_data)
    return customer_schema.jsonify(customer), 201 #send them the customer object with a 201 successful creation status


# @cache.cached(timeout=120)
def find_all():
    page = request.args.get("page")
    per_page = request.args.get("per_page") #paginate relys on integers and query parameters by default are strings (must convert)
    all_customers = customerService.find_all(page, per_page)

    return customers_schema.jsonify(all_customers), 200