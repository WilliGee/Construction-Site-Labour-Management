from lib.db import BASE, engine, session
from lib import Labourer
from datetime import datetime
import ipdb


if __name__ == "__main__":
    print ("This is the Main")

    BASE.metadata.create_all(engine)

    Labourer1 = Labourer(
        name = "Amos"
        gender = "Male"
        birthdate = datetime(year=1994, month=2, day=3)
        service_number = 35467
    )

    session.add(Labourer1)
    session.query(Labourer).update()
    session.commit()






    ipdb.set_trace()