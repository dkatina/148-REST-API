from database import db
from models.product import Product
from sqlalchemy import select


def save(product_data): #save controller will pass the service validated data

    new_product = Product(product_name=product_data['product_name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit()

    db.session.refresh(new_product)
    return new_product #returning new product back to the controller


def find_all(): #Not recieveing and data from controller, because this is a GET request
    query = select(Product)
    all_products = db.session.execute(query).scalars().all()
    return all_products #Returning my database findings to the controller

def search_product(search_term):
    query = select(Product).where(Product.product_name.like(f'%{search_term}%'))
    search_products = db.session.execute(query).scalars().all()
    return search_products
