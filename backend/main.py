# coding=utf-8

from entity import Session, engine, Base
from models import User

# generate database schema
Base.metadata.create_all(engine)

# start seesion
session = Session()

# check for existing data
users = session.query(User).all()

if len(users) == 0:
    # Create dummy values
    temp_mentor = User("Super Athlete", 45, True, False)
    temp_mentee = User("New Kid", 90, False, True)
    session.add(temp_mentor)
    session.add(temp_mentee)

    session.commit()
    session.close()

    # reload db
    users = session.query(User).all()

#Print Results
for user in users:
    print(f'{user.name}')
