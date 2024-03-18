#!/usr/bin/python3
"""Module of a script to insert a new state to the db"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost:3306/{sys.argv[3]}")

    Session = sessionmaker(bind=engine)
    session = Session()

    """Define a new state object"""
    new_state = State(name='Louisiana')

    """Add the new object to the session"""
    session.add(new_state)

    """Commit the transaction"""
    session.commit()
    print(f"{new_state.id}")

    session.close()
