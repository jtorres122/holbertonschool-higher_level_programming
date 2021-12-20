#!/usr/bin/python3
'''
Script prints the State object with the name
passed as argument from the database
'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    host = 'localhost'
    db = argv[3]
    state_arg = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user, passwd, host, db))
    session = sessionmaker(bind=engine)
    Session = session()

    table = Session.query(State).filter_by(name=state_arg).first()

    if table is not None:
        print("{}".format(table.id))
    else:
        print("Not found")

    Session.close()
