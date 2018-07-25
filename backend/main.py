# coding=utf-8

from app import app
from entity import session

if __name__ == '__main__':

    app.run()
    session.close()
