#!/usr/bin/python3
'''Script lists all State objects and City objects'''


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import Base, City
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
        print(row.id, end="")
        print(":", row.name)
        for city in row.cities:
            print("\t", end="")
            print(city.id, end="")
            print(":", city.name)
