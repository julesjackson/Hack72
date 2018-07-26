# coding=utf-8

from app import app
from flask import request, jsonify
from models import Users, UserSchema
from entity import session
from app.utilities import create_test_db

import json

#Check if database exist and is populated, else populate
testing = session.query(Users).all()
if len(testing) == 0:
    create_test_db()

@app.route('/')
def index():
    return "Hello World!"

@app.route('/user/<int:employee_id>')
def get_user(employee_id):
    """Return user with the same id"""

    results = session.query(Users).filter(Users.employee_id == employee_id).first()

    if results is None:
        return "No employee with that id found", 400

    return str(results.employee_id)

@app.route('/mentors')
def get_all_mentors():
    """Return all users who are mentors"""

    mentor_objects = session.query(Users).filter(Users.is_mentor == True).all()
    schema = UserSchema(many=True)
    mentors = schema.dump(mentor_objects)

    return jsonify(mentors.data)

@app.route('/mentees')
def get_all_mentees():
    """Return all users who are mentees"""

    mentee_objects = session.query(Users).filter(Users.is_mentee == True).all()
    schema = UserSchema(many=True)
    mentees = schema.dump(mentee_objects)

    return jsonify(mentees.data)

#@app.route('/new_user', methods=['POST'])
#def add_user():
#    """Given user info, add to database"""

#    new_user = request.get_json().get("newuser")

#    return json.dumps(new_user)
