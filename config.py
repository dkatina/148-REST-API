import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:BAC146@localhost/tacos'
    CACHE_TYPE = "SimpleCache"
    DEBUG = True


class TestingConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    CACHE_TYPE = "SimpleCache"
    TESTING =True


class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///app.db' 
    CACHE_TYPE = "SimpleCache"