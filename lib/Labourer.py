from .db import BASE
from sqlalchemy import Column, Integer, DateTime, String

class Labourer (BASE):

    __tablename__ = "labourers"


    id = Column (Integer(), primary_key=True)
    name = Column(String())
    gender = Column(String())
    Birthdate = Column(Integer())
    service_number = Column (Integer())

    def work(self, materials):
        print ("Building", materials)