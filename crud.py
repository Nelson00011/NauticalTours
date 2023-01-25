"""CRUD operations"""

from model import db, User, Trip, Tour, connect_to_db

#User related functions
def create_user(fname, lname, phone, password, email, birthday):
    """Create and return a new user."""
    
    user = User(
        fname = fname, 
        lname = lname,
        phone = phone,
        password = password,
        email = email,
        balance = 0,
        birthday = birthday
     )

    return user

def get_user_by_email(email):
    """Return a user if email exists."""
    
    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Returns user with specified id. """
    
    return User.query.get(user_id)


#Trip Related Functions
def create_trip(user_id, tour_id, status='like'):
    """Create and return a new trip."""
    trip = Trip(
        user_id = user_id,
        tour_id = tour_id,
        status = status
     )

    return trip 
  
#booking or liking a trip

#Tour Related Functions
def create_tour(tour_name, details, price, date, days = 9):
    """Create and return a new tour."""
    tour = Tour(
        tour_name = tour_name,
        details = details,
        price = price,
        date = date,
        days = days
     )

    return tour

def get_tours():
    """Return all tours."""

    return Tour.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)