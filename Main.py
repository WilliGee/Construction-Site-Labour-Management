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
        service_number=35467,
        casual_id = 25115494
    )

def search_casual():
    try:
        Casual = input("Enter casuals name: ")

    except Exception as e:
        print(f"Error adding casual: {e}")
        print("An error occurred. Please try again.")

def get_supervisor():
    try:
        supervisor_name = input("Enter supervisor name: ")

    except Exception as e:
        print(f"Error getting supervisor info: {e}")
        print("An error occurred. Please try again.")

def identify_the_manager():
    try:
        manager = input("Enter manager name: ")

    except Exception as e:
        print(f"Error updating magazine info: {e}")
        print("An error occurred. Please try again.")

def print_casuals():
    print("\nAll Casuals:")
    for casuals in casuals.all():
        print(casuals)


    def main():
    # Adding sample data
     manager = Manager("William")


     supervisor1 = Supervisor ("Paul")
     supervisor2 = Supervisor("Mark")

     casual1 = Casual ("Amos")
     casual2 = Casual ("John")
     casual3 = Casual ("Steeve")

    while True:
        print("\nOptions:")
        print("1. Search Casual")
        print("2. Get Supervisor")
        print("3. Identify the Manager")
        print("4. Print Casuals")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            search_casual()
        elif choice == "2":
            get_supervisor()
        elif choice == "3":
            identify_the_manager()
        elif choice == "4":
            print_casuals()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

    session.add(Casual1)
    #session.query(Casual).update()
    session.commit()

if __name__ == "__main__":
    print ("This is the Main")


    ipdb.set_trace()