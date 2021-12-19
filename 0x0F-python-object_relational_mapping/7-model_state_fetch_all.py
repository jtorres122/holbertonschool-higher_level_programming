#!/usr/bin/python3
'''
Script lists all State objects from a database
'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == '__main__':

    user=argv[1]
    passwd=argv[2]
    host='localhost'
    db=argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db))
    session = sessionmaker(bind=engine)
    Session = session()

    table = Session.query(State).order_by(State.id)

    for row in table:
        print('{}: {}'.format(row.id, row.name))

    Session.close()
