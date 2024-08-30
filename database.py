from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): #Creating our base class that all models will inherit
    pass

db = SQLAlchemy(model_class=Base) #Instantiating our db using Base as the model class