#!/usr/bin/python3
"""
A python script that contains the class definition of a State
and an instance Base = declarative_base():
"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

"""Import SQLAlchemy"""

Base = declarative_base()
"""Define the database models"""


class State(Base):
    """The State class that inherits from base
    Args:
        id: Auto generate, unique, primary key, can't be null
        name: String, can't be null
    """

    __tablename__ = "states"
    id = Column(
        Integer, Sequence("state_id_seq"), unique=True,
        nullable=False, primary_key=True
    )
    name = Column(String(128), nullable=False)
