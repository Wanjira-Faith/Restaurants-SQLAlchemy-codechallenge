from  models import Restaurant, Customer, Review
from sqlalchemy import create_engine,func
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurant.db')

Session = sessionmaker(bind=engine)
session = Session()

# Test relationships and methods

# Retrieve a sample restaurant
restaurant = session.query(Restaurant).filter_by(name="Cuban Code").first()

# Print the restaurant's name and price
print('--------------------------------')
print(f"Restaurant Name: {restaurant.name}")
print(f"Restaurant Price: {restaurant.price}")
print('---------------------------------')

# Print all reviews for the restaurant
print("All Reviews:")
for review_str in restaurant.all_reviews():
    print(review_str)
print('--------------------------------')    

# Retrieve a sample customer
customer = session.query(Customer).filter_by(first_name="Linda").first()

# Print the customer's full name
print(f"Customer Full Name: {customer.full_name()}")
print('-------------------------------')

# Print the customer's favorite restaurant with the highest star rating
favourite_restaurant = customer.favourite_restaurant()
rating = session.query(func.max(Review.star_rating)).filter_by(restaurant=favourite_restaurant).scalar()

print('-------------------------------')
print(f"Favourite Restaurant: {favourite_restaurant.name} (Rating: {rating})")
print('--------------------------------')

# Add a review for a restaurant by the customer
new_rating = 4  
customer.add_review(restaurant, new_rating)

# Print all reviews left by the customer
print('----------------------------------')
print("Customer's Reviews:")
for review in customer.reviews:
    print(review.full_review())
print('-----------------------------------')

# Delete all reviews by the customer for a specific restaurant
customer.delete_reviews(restaurant)

# Print all reviews for the restaurant after deleting the customer's reviews
print('------------------------------------')
print("All Reviews (after deleting customer's reviews):")
for review_str in restaurant.all_reviews():
    print(review_str)

# Close the session
session.close() 