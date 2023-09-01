from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

# Define database commnection
engine = create_engine('sqlite:///restaurant.db', echo=True)

#base class for all the classes
Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)  
    name = Column(String)  
    price = Column(Integer)  

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

class Review(Base):
    __tablename__ ='reviews'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    star_rating = Column(Integer)

# create all tables in the database
Base.metadata.create_all(engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()