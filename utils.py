from db import db
from models import User
from lib.pybcrypt import bcrypt

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
    



'''
METHODS TO BE IMPLEMENTED

1. Creating a new user in the database


2. Getting a user from the database

3. updating a user in the database

4. deleting a user from the database

'''