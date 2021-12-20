#!/usr/bin/python3
'''
Script prints the first State object from the database hbtn_0e_6_usa
'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import _xoptions, argv
from model_state import State, Base

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    host = 'localhost'
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user, passwd, host, db))
    session = sessionmaker(bind=engine)
    Session = session()

    tobedeleted = Session.query(State).filter(
        State.name.contains('a')).all()

    for row in tobedeleted:
        Session.delete(row)

    Session.commit()
    Session.close()
