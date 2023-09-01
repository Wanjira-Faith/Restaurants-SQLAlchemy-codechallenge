from  models import Restaurant, Customer, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurant.db')

Session = sessionmaker(bind=engine)
session = Session()

# Sample data
restaurant1 = Restaurant(name='Delicious Eatery', price=15000)
restaurant2 = Restaurant(name='Dusit Princess', price=20000)
restaurant3 = Restaurant(name='Cuban Code', price=17000)

customer1 = Customer(firts_name='Linda', last_name='Wambui')
customer2 = Customer(first_name='Abdi', last_name='Malik')
customer3 = Customer(first_name='Viela', last_name='Clara')

review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=6)
review2 = Review(restaurant=restaurant1, customer=customer2, star_rating=5)
review3 = Review(restaurant=restaurant2, customer=customer1, star_rating=7)
review4 = Review(restaurant=restaurant3, customer=customer3, star_rating=8)





