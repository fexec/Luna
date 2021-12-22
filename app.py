import os
from flask import Flask, jsonify
from authlib.integrations.flask_client import OAuth
from authlib.jose import jwt

app = Flask(__name__)
app.config['TESTING'] = True

oauth = OAuth(app)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")