from database import db #services interact directly with the db
from models.customer import Customer #need this to create customer objects
from sqlalchemy import select #so we can query our db


def save(customer_data):

    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=customer_data['password'])
    db.session.add(new_customer)
    db.session.commit() #adding our new customer to our db

    db.session.refresh(new_customer)
    return new_customer


def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()

    return all_customers