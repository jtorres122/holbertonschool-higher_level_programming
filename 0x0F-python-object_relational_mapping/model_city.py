#!/usr/bin/python3
""" Module defines class City who inherits from Base """

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''
    Class adds table cities and three fields
    with defined attributes
    '''

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
