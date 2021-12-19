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

    table = Session.query(State).filter(State.name.contains('a')).
    order_by(State.id)

    for row in table:
        print('{}: {}'.format(row.id, row.name))

    Session.close()
