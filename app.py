import os
from flask import Flask, jsonify, request, response
import werkzeug.exceptions as ex
from authlib.integrations.flask_client import OAuth
from authlib.jose import jwt
from db import db
import functools
import utils
import datetime
import config


app = Flask(__name__)

@app.route("/")
def hello_world():
    resp = make_response
    
    '''
    Things to be implemented here
    1. adding refresh token to http-only cookie
    2. need to add is_active and field to the user model
    3. add method that sets the refresh token to blank for a user if they log out 
    4. store ROLE field inside of jwt
    '''
    
'''
this function checks if the jwt making the request hasn't been tampered with by malicious users or 
if the jwt making the request isn't expired.

- if the jwt is expired we want to use the refresh token and create a new access token to make a request for the user
-
'''
def login_required(method):
    @functools.wraps(method):
        def wrapper(self):
            header = request.headers.get('Authorization')
            token = header.split()[1]
            
            try: 
                decoded = jwt.decode(
                    token, 
                    app.config['KEY'], 
                    algorithms='H256'
                    )
                
            except jwt.JWTError:   
                abort(400, message='Token is not valid')
                
            
            user = decoded['userid']
            
                
@app.route("/api/login", methods=["POST"])
async def user_login():

    try:

        valid_credentials = utils.validate_user_credentials(
            request.json['username'], request.json['password'])

        if not valid_credentials:
            abort(400, message='')
        access_token = utils.create_access_token(request.json['username'])
        refresh_token = utils.create_refresh_token()
        
        return jsonify({'access_token': access_token})
    
    except Exception as e:
        abort(500, message = 'Something went wrong while processing your request.')


def invalid_credentials():
    return jsonify({'message': 'username or password is incorrect or does not exist'}), 400

#when this is ran the access token is added to db of invalidated jwts 
@app.route("/logout", methods=["POST"])
def invalidate_access_token():
    
    # Bearer <token>
    request.headers['Authorization'].split(" ")[1]
    
    
    

@app.route("/test", methods=["GET"])
def test_request():
    print(request.json['username'])

    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")