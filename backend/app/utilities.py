from random import randint, seed, choice, randrange
from models import Users, Relatioship, MentorSurvey, MenteeSurvey
from entity import session, engine, Base

seed(7242018)

job_title_seq = ['entry', 'senior', 'manager']
depart_seq = ['technology', 'digital', 'hr', 'warehouse']
emp_network_seq = ['Women in Stem', 'Pride employeess', 'Black employees',
                    'Latino employees']

users_list = [
    {
        'name': 'Alice', 'employee_id': randint(50, 100),
        'is_mentor': True, 'is_mentee': False,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': choice(job_title_seq), 'department': choice(depart_seq),
        'bio': 'user info', 'employee_network': [],
        'num_to_mentor': 3, 'location': 'WHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6)
    },
    {
        'name': 'Bob', 'employee_id': randint(50, 100),
        'is_mentor': False, 'is_mentee': True,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': choice(job_title_seq), 'department': choice(depart_seq),
        'bio': 'user info', 'employee_network': [choice(emp_network_seq)],
        'num_to_mentor': 0, 'location': 'WHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6)
    },
    {
        'name': 'Carol', 'employee_id': randint(50, 100),
        'is_mentor': True, 'is_mentee': False,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': choice(job_title_seq), 'department': choice(depart_seq),
        'bio': 'user info',
        'employee_network': [choice(emp_network_seq), choice(emp_network_seq)],
        'num_to_mentor': 3, 'location': 'EHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6)
    },
    {
        'name': 'Diana', 'employee_id': randint(50, 100),
        'is_mentor': True, 'is_mentee': True,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': choice(job_title_seq), 'department': choice(depart_seq),
        'bio': 'user info', 'employee_network': [choice(emp_network_seq)],
        'num_to_mentor': 3, 'location': 'WHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6)
    },
    {
        'name': 'Eric', 'employee_id': randint(50, 100),
        'is_mentor': False, 'is_mentee': True,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': choice(job_title_seq), 'department': choice(depart_seq),
        'bio': 'user info',
        'employee_network': [choice(emp_network_seq), choice(emp_network_seq)],
        'num_to_mentor': 0, 'location': 'EHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6)
    }
]

# generate database schema
Base.metadata.create_all(engine)

def create_test_db():
    """Populate empty database with entries"""
    for entry in users_list:
        #Populate users table
        new_user = Users(
            entry['name'], entry['employee_id'], entry['is_mentor'],
            entry['is_mentee'], entry['password'], entry['email'],
            entry['job_title'], entry['department'], entry['bio'],
            entry['employee_network'], entry['num_to_mentor']
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

    results = session.query(Users).all()
    if len(results) == 5:
        print("Successfully added dummy values to data")
    else:
        print(f"Error only had {len(results)} entries in database")

    #TODO Populate Relationship Table

    session.commit()
    session.close()
