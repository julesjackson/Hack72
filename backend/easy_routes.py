# coding=utf-8

from flask import Flask, jsonify, request

from backend.entity import Session, engine, Base
from backend.models import Users, UsersSchema

app = Flask(__name__)

@app.route('/mentors')
def get_mentors():
    all_mentors = Event.query.filter(Event.isMentor == True)

    return query_results(all_mentors)

@app.route('/mentee')
def get_mentees():
    all_mentees = Event.query.filter(Event.isMentee == True)

    return query_results(all_mentees)

@app.route('user/<int:employee_id>')
def get_user_with_employeeid(employee_id):
    user_profile = Event.query.filter(Event.employee_id == employee_id)

    return query_results(user_profile)


















