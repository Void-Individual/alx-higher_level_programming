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

    changed_state = session.query(State).filter(State.id == 2).first()

    if changed_state:
        changed_state.name = "New Mexico"
        session.commit()

    session.close()
