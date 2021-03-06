#!/usr/bin/python3
'''
Script pprints all City objects from the database
'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import _xoptions, argv
from model_state import State, Base
from model_city import City

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    host = 'localhost'
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user, passwd, host, db))
    session = sessionmaker(bind=engine)
    Session = session()

    table = Session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(City.id)

    for row in table:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))

    session.close()
