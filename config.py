
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:BAC146@localhost/tacos'
    CACHE_TYPE = "SimpleCache"
    DEBUG = True