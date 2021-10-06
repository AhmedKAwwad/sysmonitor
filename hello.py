from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    print ("Server is ON\n Welcome Awwad")
    # shutdown_server()
    return "<p>Hello, World!</p>"

