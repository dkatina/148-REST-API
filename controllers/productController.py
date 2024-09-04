from flask import request, jsonify 
from models.schemas.productSchema import product_schema, products_schema
from marshmallow import ValidationError
from services import productService

def save():
    try: 
        product_data = product_schema.load(request.json) #unpack/deserializing (load) and validate (product_schema) incoming request data
    except ValidationError as e:
        return jsonify(e.messages), 400 #sending error message and error status code
    
    new_product = productService.save(product_data) #calling my service

    return product_schema.jsonify(new_product), 201 


def find_all():
    all_products = productService.find_all()
    return products_schema.jsonify(all_products), 200

def search_product():
    search_term = request.args.get("search")
    search_products = productService.search_product(search_term)
    return products_schema.jsonify(search_products), 200
