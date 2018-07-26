# coding=utf-8

from sqlalchemy import Column, String, Integer, Boolean
from entity import Entity, Base
from marshmallow import Schema, fields


class User(Entity, Base):
    __tablename__ = 'users'

    name = Column(String)
    employee_id = Column(Integer)
    is_mentor = Column(Boolean)
    is_mentee = Column(Boolean)
    password = Column(String)
    email = Column(String)
    job_title = Column(String)
    department = Column(String)
    bio = Column(String)
    employee_network = Column(String)
    num_to_mentor = Column(Integer)

    def __init__(self, name, employee_id, is_mentor, is_mentee, password, email,job_title, department, bio, employee_network, num_to_mentor):
        Entity.__init__(self)
        self.name = name
        self.employee_id = employee_id
        self.is_mentor = is_mentor
        self.is_mentee = is_mentee
        self.password = password
        self.email = email
        self.job_title = job_title
        self.department = department
        self.bio = bio
        self.employee_network = employee_network
        self.num_to_network = num_to_network

class UserSchema(Schema):
    name = fields.Str()
    employee = fields.Integer()
    is_mentor = fields.Boolean()
    is_Mentee = fields.Boolean()
    password = fields.Str()
    email = fields.Str()
    job_title = fields.Str()
    department = fields.Str()
    bio = fields.Str()
    employee_network = fields.Str()
    num_to_network = fields.Integer()


class Relatioship(Entity, Base):
    __tablename__='relationships'

    mentor_name = Column(String)
    mentee_name = Column(String)
    mentor_id = Column(Integer)
    mentee_id = Column(Integer)

    def __init__(self,mentor_name, mentee_name, mentor_id, mentee_id):
        Entity.__init__(self)
        self.mentor_name = mentor_name
        self.mentee_name = mentee_name
        self.mentor_id = mentor_id
        self.mentee_id = mentee_id

class RelationshipSechema(Schema):
    mentor_name = fields.Str()
    mentee_name = fields.Str()
    mentor_id = fields.Integer()
    mentee_id = fields.Integer()


class MentorSurvey(Entity, Base):
    __tablename__ = 'mentorsurveys'

    user_id = Column(Integer)
    location = Column(String)
    cpa = Column(Integer)
    leadership_skills= Column(Integer)
    life_at_nike = Column(Integer)
    education_advice = Column(Integer)
    finance = Column(Integer)

    def __init__(self, user_id, location, cpa, leadership_skills, life_at_nike, education_advice, finance):
        Entity.__init__(self)
        self.user_id = user_id
        self.location = location
        self.cpa = cpa
        self.leadership_skills = leadership_skills
        self.education_advice = education_advice
        self.finance = finance 

class MentorSurvey(Schema):
    user_id = fields.Integer()
    location = fields.Str()
    cpa = fields.Integer()
    leadership_skills = fields.Integer()
    life_at_nike = fields.Integer()
    education_advice = fields.Integer()
    finance = fields.Integer()

class MenteeSurvey(Entity, Base):
    __tablename__ = 'menteesurveys'

    user_id = Column(Integer)
    location = Column(String)
    cpa = Column(Integer)
    leadership_skills= Column(Integer)
    life_at_nike = Column(Integer)
    education_advice = Column(Integer)
    finance = Column(Integer)
    
    def __init__(self, user_id, location, cpa, leadership_skills, life_at_nike, education_advice, finance):
        Entity.__init__(self)
        self.user_id = user_id
        self.location = location
        self.cpa = cpa
        self.leadership_skills = leadership_skills
        self.education_advice = education_advice
        self.finance = finance

class MenteeSurvey(Schema):
    user_id = fields.Integer()
    location = fields.Str()
    cpa = fields.Integer()
    leadership_skills = fields.Integer()
    life_at_nike = fields.Integer()
    education_advice = fields.Integer()
    finance = fields.Integer()
    


