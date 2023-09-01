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

    # Define a one-to-many relationship with review class
    reviews = relationship('Review', back_populates='restaurant')

    # Define a many-to-many relationship with customer class through reviews table
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

    @classmethod
    def fanciest(cls):
         return session.query(cls).order_by(cls.price.desc()).first()
    
    def all_reviews(self):
        [review.full_review() for review in self.reviews]

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define a one-to-many relationship with review class
    reviews = relationship('Review', back_populates='customer')

    # Define a many-to-many relationship with restaurant class through reviews table
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

class Review(Base):
    __tablename__ ='reviews'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    star_rating = Column(Integer)

    # Define the relationships with restaurant and customer class
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')


# create all tables in the database
Base.metadata.create_all(engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()