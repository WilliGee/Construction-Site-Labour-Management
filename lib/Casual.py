from .db import BASE
from sqlalchemy import Column, Integer, DateTime, String

class Casual (BASE):

    __tablename__ = "casuals"


    id = Column (Integer(), primary_key=True)
    name = Column(String())
    gender = Column(String())
    birthdate = Column(Integer())
    service_number = Column (Integer())
    casual_id = Column (Integer())

    def work(self):
        print ("Trade")