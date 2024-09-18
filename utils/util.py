import jwt
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, jsonify
import os

SECRET_KEY = os.environ.get('SECRET_KEY')

def encode_token(user_id): #original
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1), #setting an expiration date
        'iat': datetime.now(timezone.utc), #Issued at
        'sub': user_id #Sub stands for 'subject' aka who is this token for
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def token_required(f): #f = the function that our wrapper wraps around
    @wraps(f)
    def wrapper(*args, **kwargs): #when wrapping around a function we need to make sure it's paramaters make it through the wrapper
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256') #decodeing the toke with the same mechanism we used to encode the token
                print("Payload", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401 #unauthenticated
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid Token'}), 401
            return f(*args, **kwargs) #Calling our wrapped function
        else:
            return jsonify({'message': 'Authentication token missing'}), 401
    return wrapper
 
def user_validation(f): #Validates and returns the user_id associated with the token
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401 #unauthenticated
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid Token'}), 401
            return f(token_id=payload['sub'], *args, **kwargs)
        else:
            return jsonify({'message': 'Authentication token missing'}), 401
        
    return wrapper


#============== For Role-Based Access =================

def encode_role_token(user_id, role_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1), #setting an expiration date
        'iat': datetime.now(timezone.utc), #Issued at
        'sub': user_id, #Sub stands for 'subject' aka who is this token for
        'admin': role_id
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def admin_required(f): #f = the function that our wrapper wraps around
    @wraps(f)
    def wrapper(*args, **kwargs): #when wrapping around a function we need to make sure it's paramaters make it through the wrapper
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256') #decodeing the toke with the same mechanism we used to encode the token
                print("Payload", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401 #unauthenticated
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid Token'}), 401
            if payload['admin'] == 1:
                return f(*args, **kwargs) #Calling our wrapped function
            else:
                return jsonify({"message": "Need Admin permissions"}), 401
        else:
            return jsonify({'message': 'Authentication token missing'}), 401
    return wrapper