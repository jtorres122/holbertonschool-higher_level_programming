#!/usr/bin/python3
"""
Script creates the State “California” with 
the City “San Francisco” from the database 
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = Session()

    Session.add(City(name="San Francisco", state=State(name="California")))

    Session.commit()
    Session.close()
