from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine ("sqlite:///site.db")
BASE = declarative_base()

