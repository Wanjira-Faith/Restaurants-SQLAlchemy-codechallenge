from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,ForeignKey
from sqlalcemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

# Define database commnection
engine = create_engine('sqlite///:restaurants.db', echo=True)

#base class for all the classes
Base = declarative_base()
