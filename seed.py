import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Manager,Supervisor,Casual
from faker import Faker

if __name__ == "__main__":
    fake = Faker()
    engine = create_engine('sqlite:///site.db')
    Base.metadata.bind = engine
    Session = sessionmaker (bind=engine)
    session = Session()
    
    def generate_occupation():
        occupations  = ["Software Engineer", "Teacher", "Doctor", "Writer", "Chef", "Artist", "Electrician", "Nurse", "Photographer"]
        return random.choice(occupations)

    #clear data before running the seed data
    
    session.query(Manager).delete()
    session.query(Supervisor).delete()
    session.query(Casual).delete()
    session.commit()  
    
    #managers seed data
    managers = [
    Manager(
        name=fake.name(),
        contact=fake.phone_number(),
        email=fake.email()
    )
    for i in range(50)]

    session.bulk_save_objects(managers)
    session.commit()
    
    
    #managers seed data
    supervisors = [
    Supervisor(
        name=fake.name(),
        contact=fake.phone_number(),
        trade=generate_occupation(),
        
    )
    for i in range(50)]

    session.bulk_save_objects(supervisors)
    session.commit()
    

    #seed data
    casuals = [
    Casual(
        name=fake.name(),
        gender=fake.word(),
        birthdate=fake.date(),
        service_number=random.randint(10**11, (10**12) - 1)
    )
    for i in range(50)]

    session.bulk_save_objects(casuals)
    session.commit()
    