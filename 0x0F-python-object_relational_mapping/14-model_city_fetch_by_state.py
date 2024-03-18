#!/usr/bin/python3
"""Module to print all the city objects in a db"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City


if __name__ == '__main__':
    engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost:3306/{sys.argv[3]}")

    Session = sessionmaker(engine)
    session = Session()

    Results = session.query(City, State).\
        join(City.state).order_by(City.id).all()

    for city, state in Results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
