from random import randint, seed, choice, randrange
from models import Users, Relatioship, MentorSurvey, MenteeSurvey
from entity import session, engine, Base

seed(7242018)

survey_fields = ['cpa', 'leadership_skills', 'life_at_nike', 'education_advice',
    'finance', 'location']
job_title_seq = ['entry', 'senior', 'manager']
depart_seq = ['technology', 'digital', 'hr', 'warehouse']
emp_network_seq = ['Women in Stem', 'Pride employeess', 'Black employees',
                    'Latino employees']

users_list = [
    {
        'fname': 'Alice', 'lname': 'Allen', 'employee_id': randint(50, 100),
        'is_mentor': True, 'is_mentee': False,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': choice(job_title_seq), 'department': choice(depart_seq),
        'bio': 'user info', 'employee_network': [],
        'num_to_mentor': 3, 'location': 'WHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6), 'url':''
    },
    {
        'fname': 'Bob', 'lname': 'Bolton', 'employee_id': randint(50, 100),
        'is_mentor': False, 'is_mentee': True,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': choice(job_title_seq), 'department': choice(depart_seq),
        'bio': 'user info', 'employee_network': [choice(emp_network_seq)],
        'num_to_mentor': 0, 'location': 'WHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6), 'url':''
    },
    {
        'fname': 'Carol', 'lname': 'Carson', 'employee_id': randint(50, 100),
        'is_mentor': True, 'is_mentee': False,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': choice(job_title_seq), 'department': choice(depart_seq),
        'bio': 'user info',
        'employee_network': [choice(emp_network_seq), choice(emp_network_seq)],
        'num_to_mentor': 3, 'location': 'EHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6), 'url':''
    },
    {
        'fname': 'Diana', 'lname': 'Diners', 'employee_id': randint(50, 100),
        'is_mentor': True, 'is_mentee': True,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': choice(job_title_seq), 'department': choice(depart_seq),
        'bio': 'user info', 'employee_network': [choice(emp_network_seq)],
        'num_to_mentor': 3, 'location': 'WHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6), 'url':''
    },
    {
        'fname': 'Eric', 'lname': 'Ericson', 'employee_id': randint(50, 100),
        'is_mentor': False, 'is_mentee': True,
        'password': 'nike', 'email': 'employee@nike.com',
        'job_title': choice(job_title_seq), 'department': choice(depart_seq),
        'bio': 'user info',
        'employee_network': [choice(emp_network_seq), choice(emp_network_seq)],
        'num_to_mentor': 0, 'location': 'EHQ', 'cpa': randrange(1, 6),
        'leadership_skills': randrange(1, 6), 'life_at_nike': randrange(1, 6),
        'education_advice': randrange(1, 6), 'finance': randrange(1, 6), 'url':''
    }
]

# generate database schema
Base.metadata.create_all(engine)

def create_test_db():
    """Populate empty database with entries"""
    for entry in users_list:
        #Populate users table
        new_user = Users(
            entry['fname'], entry['lname'], entry['employee_id'], entry['is_mentor'],
            entry['is_mentee'], entry['password'], entry['email'],
            entry['job_title'], entry['department'], entry['bio'],
            entry['employee_network'], entry['num_to_mentor'], entry['url']
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
    if len(results) == 8:
        print("Successfully added dummy values to data")
    else:
        print(f"Error only had {len(results)} entries in database")

    #TODO Populate Relationship Table

    session.commit()

def matches(new_user):
    #find mentor
    if new_user['is_mentee']:
        mentor_ranking = []
        all_mentors = session.query(Users).filter(Users.is_mentor == True).all()
        #print(all_mentors)

        for mentor in all_mentors:
            cur_mentor = session.query(MentorSurvey).filter(
                MentorSurvey.user_id == mentor.employee_id).first()

            score = 0
            if new_user['location'] == cur_mentor.location:
                score += 1
            if new_user['cpa'] == cur_mentor.cpa:
                score += 1
            if new_user['leadership_skills'] == cur_mentor.leadership_skills:
                score += 1
            if new_user['life_at_nike'] == cur_mentor.life_at_nike:
                score += 1
            if new_user['education_advice'] == cur_mentor.education_advice:
                score += 1
            if new_user['finance'] == cur_mentor.finance:
                score += 1

            mentor_ranking.append((mentor.employee_id, score))

            mentor_ranking.sort(key=lambda tup:tup[1])
        return mentor_ranking

    #find mentee
    if new_user['is_mentor']:
        mentee_ranking = []
        all_mentees = session.query(Users).filter(Users.is_mentee == True).all()

        for mentees in all_mentees:
            cur_mentee = session.query(MenteeSurvey).filter(
                MenteeSurvey.user_id == mentee.employee_id).first()

            score = 0
            if new_user['location'] == cur_mentee.location:
                score += 1
            if new_user['cpa'] == cur_mentee.cpa:
                score += 1
            if new_user['leadership_skills'] == cur_mentee.leadership_skills:
                score += 1
            if new_user['life_at_nike'] == cur_mentee.life_at_nike:
                score += 1
            if new_user['education_advice'] == cur_mentee.education_advice:
                score += 1
            if new_user['finance'] == cur_mentee.finance:
                score += 1

            mentee_ranking.append((mentee.employee_id, score))
            mentee__ranking.sort(key=lambda tup:tup[1])

        return mentee__ranking
