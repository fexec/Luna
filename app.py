import os
from flask import Flask, jsonify, request
from authlib.integrations.flask_client import OAuth
from authlib.jose import jwt
import utils
import datetime


app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)
    
@app.route("/login", methods=["POST"])
def user_login():

    try:

        valid_credentials = utils.validate_user_credentials(
            request.json['username'], request.json['password'])

        if not valid_credentials:
            return invalid_credentials()
                
        access_token = utils.create_access_token(request.json['username'])
        refresh_token = utils.create_refresh_token()

        return jsonify({"access_token": access_token, "refresh_token": refresh_token})
    
    except Exception as e:
        invalid_credentials()


def invalid_credentials():
    return jsonify({"message": "username or password is incorrect or does not exist"}), 400


@app.route("/test", methods=["GET"])
def test_request():
    print(request.json['username'])

    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")