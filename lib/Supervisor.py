from .db import BASE
from sqlalchemy import Column, Integer, DateTime, String

class Supervisor (BASE):

    __tablename__ = "supervisors"


    id = Column (Integer(), primary_key=True)
    name = Column(String())
    contact = Column(String())
    trade = Column (String())

