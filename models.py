from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///site.db')

Base = declarative_base()


class Manager (Base):

    __tablename__ = "managers"


    id = Column (Integer(), primary_key=True)
    name = Column(String())
    contact = Column(String())
    email = Column (String(60), unique=True)
    supervisors = relationship('Supervisor',backref='manager')
    
    def __repr__(self):
        return f'Manager(id={self.id})' + \
            f'name= {self.name}'+ \
            f'gender= {self.contact})' + \
            f'bio={self.email}'


class Supervisor (Base):

    __tablename__ = "supervisors"


    id = Column (Integer(), primary_key=True)
    name = Column(String())
    contact = Column(String())
    trade = Column (String())
    manager_id= Column(Integer(),ForeignKey('managers.id'))
    casuals= relationship('Casual', backref='supervisor')
    
    def __repr__(self):
        return f'Supervisor(id={self.id})' + \
            f'name= {self.name}'+ \
            f'gender= {self.contact})' + \
            f'bio={self.trade}'  + \
            f'manager_id={self.manager_id}'
            
class Casual (Base):

    __tablename__ = "casuals"


    id = Column (Integer(), primary_key=True)
    name = Column(String())
    gender = Column(String())
    birthdate = Column(Integer())
    service_number = Column (Integer())
    supervisor_id= Column(Integer(),ForeignKey('supervisors.id') )


    def __repr__(self):
        return f'Casual(id={self.id})' + \
            f'name= {self.name}'+ \
            f'gender= {self.gender})' + \
            f'bio={self.birthdate}' + \
            f'supervisor_id={self.supervisor_id}' 