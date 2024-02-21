from .db import BASE
from sqlalchemy import Column, Integer, DateTime, String

class Manager (BASE):

    __tablename__ = "managers"


    id = Column (Integer(), primary_key=True)
    name = Column(String())
    contact = Column(String())