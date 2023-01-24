"""CRUD operations"""

from model import db, User, Trip, Tour, connect_to_db


def create_user(fname, lname, phone, password, email, birthday):
    """Create and return a new user."""
    
    user = User(
        fname = fname, 
        lname = lname,
        phone = phone,
        password = password,
        email = email,
        birthday = birthday
        )

    return user

def get_user_by_email(email):
    """Return a user if email exists."""
    
    return User.query.filter(User.email == email).first()

def create_trip():
    """Create and return a new trip."""
    pass
    


def create_tour():
    """Create and return a new tour."""
    pass



if __name__ == '__main__':
    from server import app
    connect_to_db(app)