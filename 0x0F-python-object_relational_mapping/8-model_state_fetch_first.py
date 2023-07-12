#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Create the engine
    """
    url = (f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    engine = create_engine(url)

    """
    Create a session to interact with the database engine
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Write the sql query to be executed
    """

    User = session.query(State).order_by(State.id).first()
    if User:
        print(f"{User.id}: {User.name}")
    else:
        print("Nothing")
