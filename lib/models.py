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

     # Retrieve the restaurant with the highest price rating
    @classmethod
    def fanciest(cls):
         return session.query(cls).order_by(cls.price.desc()).first()
    
     # Retrieve all reviews for this restaurant and format them as strings
    def all_reviews(self):
        return [review.full_review() for review in self.reviews]


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define a one-to-many relationship with review class
    reviews = relationship('Review', back_populates='customer')

    # Define a many-to-many relationship with restaurant class through reviews table
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

    # Concatenate first name and last name to get the full name of the customer
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # Retrieve the customer's favorite restaurant based on the highest review rating
    def favourite_restaurant(self):
        return (
            session.query(Restaurant)
            .join(Review)
            .filter(Review.customer_id == self.id)
            .order_by(Review.star_rating.desc())
            .limit(1)
            .first()
        )

    # Add a new review for the customer 
    def add_review(self, restaurant, rating):
        new_review = Review(customer_id=self.id, restaurant_id=restaurant.id, star_rating=rating)
        session.add(new_review)
        session.commit()

    # Delete all reviews by the customer for a specific restaurant
    def delete_reviews(self, restaurant):
        reviews_to_delete = session.query(Review).filter(Review.restaurant == restaurant, Review.customer == self).all()
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()


class Review(Base):
    __tablename__ ='reviews'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    star_rating = Column(Integer)

    # Define the relationships with restaurant and customer class
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    # Format the review as a string
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."


# create all tables in the database
Base.metadata.create_all(engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()