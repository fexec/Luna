from db import db
import bcrypt
from models import User
from authlib.jose import jwt
from datetime import datetime, timedelta

'''
METHODS TO BE IMPLEMENTED

create_user():

1. Creating a new user in the database
- encrypt the password using bcrypt
- create user object using the provided fields from the request and encrypted the password
-  

update_user():
2. updating a user in the database


3. deleting a user from the database

4. getting an individual user from the database
    
'''

'''
checks if username exists and valid password
'''

def validate_user_credentials(username, password):
    try:
        user_doc_ref = db.collection(u'users').document(username)
        user_doc = user_doc_ref.get()
    
        if user_doc:
            user = User.from_dict(user_doc.to_dict())
            print(user)
            d = user.to_dict()
            return user.password == password

        return False 
    
    except Exception as e:
        return None
   

def update_user_credentials(user):
    
    user_doc_ref = db.collection(u'users').document(
        user.username)
    user_doc_ref.update(user.to_dict())
    


def create_access_token(username):
    
    header =  {'alg': 'HS256'}
    payload = {'userid': username}
    key = 'secret'
    token  = jwt.encode(header, payload, key)
  
    return token.decode('utf8')

def create_refresh_token():

    header = {'alg': 'HS256'}
    
    current_date = datetime.now()
    future_date = current_date +  timedelta(days=15)
    payload = {'iat':str(current_date), 'exp':str(future_date)}
    key = 'hermpythonsucks'
    token = jwt.encode(header, payload, key)

    return token.decode('utf8')


