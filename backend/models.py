# coding=utf-8

from sqlalchemy import Column, String, Integer, Boolean
from entity import Entity, Base

class User(Entity, Base):
    __tablename__ = 'users'

    name = Column(String)
    employee_id = Column(Integer)
    is_mentor = Column(Boolean)
    is_mentee = Column(Boolean)

    def __init__(self, name, employee_id, is_mentor, is_mentee):
        Entity.__init__(self)
        self.name = name
        self.employee_id = employee_id
        self.is_mentor = is_mentor
        self.is_mentee = is_mentee
