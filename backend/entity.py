# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'mentorconnect.c4mlq10qcmwj.us-east-2.rds.amazonaws.com'
db_port = 5432
db_name = 'mentorconnect'
db_user = 'hack72'
db_password = 'mentor72' #TODO hide

#engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
engine = create_engine(f'postgresql:///{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
