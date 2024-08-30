from flask import Flask
from database import db
from models.schemas import ma
from limiter import limiter
from cache import cache


#models
from models.customer import Customer

#blueprints
from routes.customerBP import customer_blueprint


def create_app(config_name):

    app = Flask(__name__) #instantiate the Flask app

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    blueprint_config(app)
    rate_limit_config(app)
    cache.init_app(app)

    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix="/customers")

def rate_limit_config(app):
    limiter.init_app(app)
    limiter.limit("100 per hour")(customer_blueprint)


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    with app.app_context():
        db.create_all()

    app.run()