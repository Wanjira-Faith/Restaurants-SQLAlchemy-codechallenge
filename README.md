# Restaurants-SQLAlchemy-codechallenge

# Introduction
This is a Python application that models a restaurant review system using SQLAlchemy, a popular Object-Relational Mapping (ORM) library for Python. The application includes three main models: Restaurant, Customer, and Review, and it allows users to interact with these models in various ways.

# Project Structure
* `models.py`: The main application file that contains the SQLAlchemy model definitions for Restaurant, Customer, and Review, as well as the database configuration.
* `seeds.py`: A script for seeding the database with sample data for testing.
* `test.py`: A script for testing and demonstrating the functionality of the application.

# Database Schema
The application defines three main tables in the database:

Restaurants Table:
* id (Integer, Primary Key)
* name (String)
* price (Integer)

Customers Table:
* id (Integer, Primary Key)
* first_name (String)
* last_name (String)

Reviews Table:
* id (Integer, Primary Key)
* restaurant_id (Integer, Foreign Key referencing restaurants.id)
* customer_id (Integer, Foreign Key referencing customers.id)
* star_rating (Integer)


# Migrations
Before using the application, you will need to create a migration for all tables.

- A `Review` belongs to a `Restaurant`, and a `Review` also belongs to a  `Customer`.  In your migration, create any columns your `reviews` table will need to establish these relationships.

* The `reviews` table should also have:  - A `star_rating` column that stores an integer.
 
After creating the `reviews` table using a migration, use the `seeds.py` file to create instances of all your classes so you can test your code.

# Usage
To test and use the application, run:
`python test.py`

#   Deliverables

# Object Relationship Methods
Use SQLAlchemy query methods where appropriate.

# Review
-- `Review customer()`

 - should return the `Customer` instance for this review

-- `Review restaurant()`

 - should return the `Restaurant` instance for this review

# Restaurant
-- `Restaurant reviews()`

 - returns a collection of all the reviews for the `Restaurant`

-- `Restaurant customers()`

 - returns a collection of all the customers who reviewed the `Restaurant`

 # Customer
 -- `Customer reviews()`
 - should return a collection of all the reviews that the `Customer` has left

-- `Customer restaurants()`
 - should return a collection of all the restaurants that the `Customer` has reviewed.

 # Aggregate and Relationship Methods

 # Customer
 -- `Customer full_name()`
 - returns the full name of the customer, with the first name and the last name  concatenated, Western style.

-- `Customer favorite_restaurant()`
 - returns the restaurant instance that has the highest star rating from this customer

--`Customer add_review(restaurant, rating)`
 - takes a `restaurant` (an instance of the `Restaurant` class) and a rating
 - creates a new review for the restaurant with the given `restaurant_id`

-- `Customer delete_reviews(restaurant)`
 - takes a `restaurant` (an instance of the `Restaurant` class) and

 - removes **all** their reviews for this restaurant

 - you will have to delete rows from the `reviews` table to get this to work!

 # Review
-- `Review full_review()`
*  should return a string formatted as follows:
Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.

# Restaurant
-- `Restaurant fanciest()`, this method should be a class method
 - returns _one_ restaurant instance for the restaurant that has the highest   price

-- `Restaurant all_reviews()`
 - should return a list of strings with all the reviews for this restaurant formatted as follows:

 ["Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars."]

# Author
Wanjira Faith(Software Engineer) 

# License
This project is licensed under the MIT License.

