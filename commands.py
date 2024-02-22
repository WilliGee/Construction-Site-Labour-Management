import click
from models import Base, Manager,Supervisor,Casual, engine
from sqlalchemy.orm import sessionmaker

# Create the database tables
Base.metadata.create_all(engine)

# Create a Session
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
def list_managers():
    managers = session.query(Manager).all()
    for manager in managers:
        click.echo(manager)

@cli.command()
def list_supervisors():
    supervisors = session.query(Supervisor).all()
    for supervisor in supervisors:
        click.echo(supervisor)

@cli.command()
def list_casuals():
    casuals = session.query(Casual).all()
    for casual in casuals:
        click.echo(casual)

@cli.command()
def add_manager():
    name = click.prompt('Enter manager name')
    new_manager = Manager(name=name)
    session.add(new_manager)
    session.commit()
    click.echo(f'Manager {name} added successfully.')

@cli.command()
def add_supervisor():
    name = click.prompt('Enter supervisor name')
    new_supervisor = Supervisor(name=name)
    session.add(new_supervisor)
    session.commit()
    click.echo(f'Supervisor {name} added successfully.')

@cli.command()
def add_casual():
    name = click.prompt('Enter casual name')
    new_casual = Casual(name=name)
    session.add(new_casual)
    session.commit()
    click.echo(f'Casual {name} added successfully.')

@cli.command()
@click.option('--manager_name', prompt='Enter manager name')
def delete_manager(manager_name):
    manager = session.query(Manager).filter_by(name=manager_name).first()
    if manager:
        session.delete(manager)
        session.commit()
        click.echo(f'Manager {manager_name} deleted successfully.')
    else:
        click.echo(f'Manager {manager_name} not found.')

@cli.command()
@click.option('--supervisor_name', prompt='Enter supervisor name')
def delete_supervisor(supervisor_name):
    supervisor = session.query(Supervisor).filter_by(name=supervisor_name).first()
    if supervisor:
        session.delete(supervisor)
        session.commit()
        click.echo(f'Supervisor {supervisor_name} deleted successfully.')
    else:
        click.echo(f'Supervisor {supervisor_name} not found.')

@cli.command()
@click.option('--casual_name', prompt='Enter casual name')
def delete_casual(casual_name):
    casual = session.query(Casual).filter_by(name=casual_name).first()
    if casual:
        session.delete(casual)
        session.commit()
        click.echo(f'Casual {casual_name} deleted successfully.')
    else:
        click.echo(f'Casual {casual_name} not found.')


def print_main_menu():
    click.echo("Main Menu:")
    click.echo("1. List Managers")
    click.echo("2. List Supervisors")
    click.echo("3. List Casuals")
    click.echo("4. Add Manager")
    click.echo("5. Add Supervisor")
    click.echo("6. Add Casual")
    click.echo("7. Delete Manager")
    click.echo("8. Delete Supervisor")
    click.echo("9. Delete Casual")
    click.echo("0. Exit")
    
    
@cli.command()
def main_menu():
    while True:
        print_main_menu()
        choice = click.prompt('Pick your Bane(0-9)', type=int)
        
        if choice == 0:
            click.echo('exiting site!')
            break
        elif choice == 1:
            list_managers()
        elif choice == 2:
            list_supervisors()
        elif choice == 3:
            list_casuals()
        elif choice == 4:
            add_manager()
        elif choice == 5:
            add_supervisor()
        elif choice == 6:
            add_casual()
        elif choice == 7:
            delete_manager()
        elif choice == 8:
            delete_supervisor()
        elif choice == 9:
            delete_casual()
        else:
            click.echo('Invalid choice. Please stay within bounds (0-9).')

if __name__ == '__main__':
    main_menu()
