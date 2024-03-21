#!/usr/bin/python3
"""Module of a script to print the state object with the name
passed as an argument from the db"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost:3306/{sys.argv[3]}")

    Session = sessionmaker(bind=engine)
    session = Session()

    name = sys.argv[4]

    """Search for the first object with the state name"""
    state = session.query(State).filter(State.name == name).first()

    if state:
        print(state.id)
    else:
        print('Not found')

    session.close()
