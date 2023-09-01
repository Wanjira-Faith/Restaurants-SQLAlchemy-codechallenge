from sqlalchemy import create_engine
from sqlalcemy.ext.declarative import declarative_base

engine = create_engine('sqlite///:restaurants.db')

Base = declarative_base()
