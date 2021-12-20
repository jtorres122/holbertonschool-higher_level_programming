#!/usr/bin/python3
'''Script lists all City objects'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == '__main__':

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()

    table = Session.query(State).order_by(State.id)

    for row in table:
        for city in row.cities:
            print(city.id, end="")
            print(":", city.name, end="")
            print(" ->", row.name)
