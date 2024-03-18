#!/usr/bin/python3
"""Module of a script to change the name of a state object with id"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost:3306/{sys.argv[3]}")

    Session = sessionmaker(bind=engine)
    session = Session()

    a_states = session.query(State).order_by(State.id).all()

    for state in a_states:
        if 'a' in state.name:
            session.delete(state)

    session.commit()
    session.close()
