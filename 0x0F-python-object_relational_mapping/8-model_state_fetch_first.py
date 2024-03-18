#!/usr/bin/python3
"""Module for a script to print the first state object in db"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost:3306/{sys.argv[3]}")

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    print(f"{states[0].id}: {states[0].name}")

    session.close()
