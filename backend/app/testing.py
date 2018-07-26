from random import randrange
import json
import requests

payload = {
        'fname': 'Mr', 'lname': 'New-Hire', 'employee_id': 150,
        'is_mentor': False, 'is_mentee': True,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': 'rotation engineer', 'department': 'technology',
        'bio': 'hello I"m new', 'employee_network': [],
        'num_to_mentor': 0, 'location': 'WHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6),
        'url': 'Mr Hire Profile'
    }

requests.post('http://127.0.0.1:5000/new_user', data=json.dumps(payload))


#---sign up---#
"""
Email
Password
First Name
Last Name
Job Title
Department
Employee Networks

Role 'Mentor' 'Mentee'

#Returne info
Name
Job Title
Bio
Email
profileID = employee_id
"""
