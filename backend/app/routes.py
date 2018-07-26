# coding=utf-8

from app import app
from flask import request, jsonify
from models import Users, UserSchema, MenteeSurvey, MentorSurvey
from entity import session
from app.utilities import create_test_db, matches

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

    temp = session.query(Users).filter(Users.employee_id == employee_id).first()

    if temp is None:
        return "No employee with that id found", 400

    results = {
        'Email': temp.email,
        'Password': temp.password,
        'First Name': temp.fname,
        'Last Name': temp.lname,
        'Job Title': temp.job_title,
        'Department': temp.department,
        'Employee Networks': temp.employee_network,
        'url': temp.profile_pic
    }
    if temp.is_mentee and not temp.is_mentor:
        results['Role'] = 'Mentee'
    elif not temp.is_mentee and temp.is_mentor:
        results['Role'] = 'Mentor'
    else:
        results['Role'] = 'Both'

    return jsonify(results)

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

@app.route('/new_user', methods=['POST'])
def add_user():
    """Given user info, add to database"""
    entry = json.loads(request.data)

    new_user = Users(
            entry['fname'], entry['lname'], entry['employee_id'],
            entry['is_mentor'], entry['is_mentee'], entry['password'],
            entry['email'], entry['job_title'], entry['department'],
            entry['bio'], entry['employee_network'], entry['num_to_mentor'],
            entry['url']
    )
    session.add(new_user)

    #populate mentor survey table
    if entry['is_mentor'] == True:
        mentor_survey = MentorSurvey(
            entry['employee_id'], entry['location'], entry['cpa'],
            entry['leadership_skills'], entry['life_at_nike'],
            entry['education_advice'], entry['finance']
        )

        session.add(mentor_survey)

    #populate mentee survey table
    if entry['is_mentee'] == True:
        mentee_survey = MenteeSurvey(
            entry['employee_id'], entry['location'], entry['cpa'],
            entry['leadership_skills'], entry['life_at_nike'],
            entry['education_advice'], entry['finance']
        )

        session.add(mentee_survey)

    ranked = matches(entry)

    session.commit()

    profile_list = []
    for prof in ranked:
        temp = session.query(Users).filter(Users.employee_id == prof[0]).first()
        schema = UserSchema(many=False)
        results = {
            'Email': temp.email,
            'Password': temp.password,
            'First Name': temp.fname,
            'Last Name': temp.lname,
            'Job Title': temp.job_title,
            'Department': temp.department,
            'Employee Networks': temp.employee_network,
            'url': temp.profile_pic
        }
        if temp.is_mentee and not temp.is_mentor:
            results['Role'] = 'Mentee'
        elif not temp.is_mentee and temp.is_mentor:
            results['Role'] = 'Mentor'
        else:
            results['Role'] = 'Both'
        profile_list.append(schema.dump(temp))

    print(profile_list)

    return jsonify(profile_list)
