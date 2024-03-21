#!/usr/bin/python3
"""Module to list all the states in a db"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Create an engine to connect to MySQL server"""
    engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost:3306/{sys.argv[3]}")

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query all State objects and sort them"""
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    """Close the session"""
    session.close()
