from  models import Restaurant, Customer, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurant.db')

Session = sessionmaker(bind=engine)
session = Session()
