from db import db
from lib.pybcrypt import bcrypt
from models import User
from authlib.jose import jwt
from datetime import datetime, timedelta
from google.cloud import firestore

'''
METHODS TO BE IMPLEMENTED

create_user():

1. Creating a new user in the database
   - encrypt the password using bcrypt
   - create user object using the provided fields from the request and encrypted the password

2. Getting a user from the database

3. updating a user in the database

4. deleting a user from the database
'''

'''
checks if username exists and valid password
'''
def create_user(self,first_name,last_name, username, email, password):
  
    salt_password = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt_password)

    # create dictionary holding data 
    user_data = {
        "first_name" : first_name,
        "last_name" : last_name,
        "username" : username,
        "email" : email,
        "password" : hashed_password
    }
    
    # creating document 
    db.collection("users").add(user_data)
    
def validate_user_credentials(username, password):
    try:
        user_doc_ref = db.collection(u'users').document(username)
        user_doc = user_doc_ref.get()
    
        if user_doc.exists:
            user = User.from_dict(user_doc.to_dict())
            d = user.to_dict()
            return user.password == password

        return False 
    
    except Exception as e:
        return None
   

def update_user_credentials(user):
    user_doc_ref = db.collection(u'users').document(
        user.username)
    user_doc_ref.update(user.to_dict())
    
    
def create_access_token(username, key, role =[]):
    
    current_date = datetime.now()
    future_date = current_date +  timedelta(hours=1)
    header =  {'alg': 'HS256'}
    payload = {'userid': username, 
               'iat': str(datetime.now()),
               'exp': str(future_date),
               'role': 'USER'}
    token  = jwt.encode(header, payload, key)
  
    return token.decode('utf8')

def create_refresh_token(username, key):

    header = {'alg': 'HS256'}
    
    current_date = datetime.now()
    future_date = current_date +  timedelta(hours=48)
    payload = {'iat':str(current_date), 
               'exp':str(future_date),
               }
    
    token = jwt.encode(header, payload, key)
    return token.decode('utf8')


def check_refresh_token(token):
    return 'please login again'

'''
this method will add an invalid token into the collection of
banned jwt

uses a utf-8 string of the jwt-token as a document id
expired jwt documents contain:

byte array token
date that
'''
def deactivate_token(token):
    try:
        token_data = {
            'token': bytes(token, 'utf-8'),
            'date_added': firestore.SERVER_TIMESTAMP
        }
        db.collection(u'expired_tokens').document(token).set(token_data)  
    
    except:
        print('something went wrong while trying to add the jwt to the expired tokens')

