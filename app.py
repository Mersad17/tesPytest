from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/other")
def hello_other():
    page = request.args.get('page', default = 1, type = int)
    return f"<p>Hello, Other!</p><p>Page : {page}<p>"





