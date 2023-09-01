from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,ForeignKey
from sqlalcemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship


engine = create_engine('sqlite///:restaurants.db', echo=True)

Base = declarative_base()
