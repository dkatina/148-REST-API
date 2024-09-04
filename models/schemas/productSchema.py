from . import ma
from marshmallow import fields

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False) #Don't need them to pass us an id, because pk is auto-incrementing
    product_name = fields.String(required=True)
    price = fields.Float(required=True)

    class Meta:
        field = ("id", "product_name", "price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True) #for handling a list of products