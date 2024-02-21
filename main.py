from lib.db import BASE, engine, session
from lib import Casual, Supervisor, Manager
from datetime import datetime
import ipdb


if __name__ == "__main__":
    print ("This is the Main")

    BASE.metadata.create_all(engine)

    Casual1 = Casual(
        name="Amos",
        gender="Male",
        birthdate=datetime(year=1994, month=2, day=3),
        service_number=35467
    )

    session.add(Casual1)
    #session.query(Casual).update()
    #session.commit()






    ipdb.set_trace()