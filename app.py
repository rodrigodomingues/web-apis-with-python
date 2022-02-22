from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/greet")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    response = {"status":"error"}
    if(fname and lname):
        response = {"data":f"Hello, Is your name {fname} {lname}?"}
    if(fname and not lname):
        response = {"data":f"Hello, {fname}"}
    if(lname and not fname):
        response = {"data":f"Hello, Mr. {lname}"}

    return response

@app.get("/")
def base():
    response = {"data":"Hey!"}
    return response