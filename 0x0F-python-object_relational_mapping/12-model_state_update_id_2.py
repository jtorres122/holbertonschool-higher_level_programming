#!/usr/bin/python3
'''Script changes the name of a State object from the database'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
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

    update = Session.query(State).get(2)
    update.name = "New Mexico"
    Session.commit()

    Session.close()
