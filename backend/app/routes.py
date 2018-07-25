# coding=utf-8
from flask import request
from models import User
from entity import session
from app import app
import json

@app.route('/')
def index():
    return "Hello World!"

@app.route('/user/<int:employee_id>')
def get_user(employee_id):
    """Return user with the same id"""

    results = session.query(User).filter(User.employee_id == employee_id).first()

    if results is None:
        return "No employee with that id found", 400

    return str(results.employee_id)

#@app.route('/new_user', methods=['POST'])
#def add_user():
    #"""Given user info, add to database"""

#    new_user = request.get_json().get("newuser")

#    return json.dumps(new_user)
