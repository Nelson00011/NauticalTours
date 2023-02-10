"""CRUD operations"""

from model import db, User, Trip, Tour, Rating, connect_to_db
from datetime import datetime, date, timedelta

#User functions
def create_user(fname, lname, phone, password, email, birthday):
    """Create and return a new user."""
    
    user = User(
        fname = fname.title(), 
        lname = lname.title(),
        phone = phone,
        password = password,
        email = email,
        balance = 0.00,
        birthday = birthday
    )

    return user

def get_user_by_email(email):
    """Return a user if email exists."""
    
    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Returns user with specified id. """
    
    return User.query.get(user_id)

def update_user_balance(amount, user_id):
    """Updates user balance based on amount changed. """
    user = get_user_by_id(user_id)
    user.balance += amount
    db.session.commit()


#Trip functions
def create_trip(user_id, tour_id, intention, status='submitted'):
    """Create and return a new trip."""
    if intention == "Book Trip":
        tour = get_tour_by_id(tour_id)
        price = tour.price
        if status!='completed':
            update_user_balance(price, user_id)

    trip = Trip(
        user_id = user_id,
        tour_id = tour_id,
        intention = intention,
        status = status
     )

    return trip 
  

#Booking functions
def get_trips_by_trip_id(trip_id):
    """Returns trips with specified user_id."""
    
    return Trip.query.filter(Trip.trip_id==trip_id).one()


def get_trips_by_id(user_id):
    """Returns trips with specified user_id."""
    
    return Trip.query.filter(Trip.user_id==user_id).all()

def get_triplist_by_user_tour(user_id, tour_id, intention="Book Trip"):
    """Returns trips with specified user_id, tour_id, intention."""
    
    return Trip.query.filter(Trip.user_id==user_id, Trip.tour_id==tour_id, Trip.intention==intention).all()

def update_saved_trips(user_id, tour_id, intention):
    """Updates the saved trips with specified user_id, tour_id, intention."""
    saved = get_triplist_by_user_tour(user_id, tour_id, intention="Save Trip")
    if saved:
        saved[0].status =  "booked"
        db.session.commit()


#Rating functions
def create_rating(user_id, tour_name, dates, rating, review):
    """Create and return a new tour rating"""
    rating = Rating(
        user_id = user_id,
        tour_name = tour_name,
        dates = dates, 
        rating = rating,
        review = review
    )

    return rating


def get_rating_by_id(rate_id):
    """Returns ratings with specified rate_id."""
    
    return Rating.query.filter(Rating.rate_id==rate_id).all()


def get_rating_by_user_id(user_id):
    """Returns ratings with specified user_id."""
    
    return Rating.query.filter(Rating.user_id==user_id).all()


def get_rating_by_tour_name(tour_name):
    """Returns ratings with specified tour_name."""
    
    return Rating.query.filter(Rating.tour_name==tour_name).all()


def get_rating_by_user_id_tour_id(user_id,tour_id):
    """Returns ratings with specified user_id, tour_id."""
    tour = get_tour_by_id(tour_id)
    return Rating.query.filter(Rating.user_id==user_id, Rating.tour_name==tour.tour_name).all()

def get_rating_by_user_id_tour_id_dates(user_id,tour_id, dates):
    """Returns ratings with specified user_id,tour_id, dates."""

    tour = get_tour_by_id(tour_id)
    return Rating.query.filter(Rating.user_id==user_id, Rating.tour_name==tour.tour_name, Rating.dates==dates).all()


def update_rating_by_rating_id(user_id, tour_id, dates, score, reviews):
    """Returns ratings with specified user_id."""

    rating_list=get_rating_by_user_id_tour_id_dates(user_id, tour_id, dates)
    ratings=rating_list[0]
    
    ratings.rating = score
    ratings.review = reviews
    db.session.commit()
    


#Tour functions
def create_tour(tour_name, details, price, dates, port_id, port_name,state_name, days = 9):
    """Create and return a new tour."""
    tour = Tour(
        tour_name = tour_name,
        details = details,
        price = price,
        dates = dates,
        days = days,
        port_id = port_id,
        port_name = port_name,
        state_name = state_name
     )

    return tour

def get_tours():
    """Return all tours."""

    return Tour.query.all()

def get_tour_by_id(tour_id):
    """Returns tour with specified id. """
    
    return Tour.query.get(tour_id)




def get_profile_list(trip_list):
    """Returns trips  information with specified user_id. """
    output = []
    if trip_list == []:
        return False
    
    today = date.today()
    
    for trip in trip_list:
        tour = get_tour_by_id(trip.tour_id)
        ratings = get_rating_by_user_id_tour_id(trip.user_id, trip.tour_id)
        
        obj = {}
        obj['trip_id'] = trip.trip_id
        obj['tour_id'] = tour.tour_id
        obj['tour'] = tour.tour_name
        obj['dates'] = tour.dates
        #assigning price value based on action
        action = trip.intention.split()[0]

        if action == 'Save':
            obj['price'] = 0.00
        elif trip.status == 'completed':
            obj['price'] = 0.00
            
        else:
             obj['price'] = tour.price
        #action name visible to user
        if action.endswith('e'):
            action=action+"d" 
        else:
            action=action+"ed"
        obj['action'] = action
        obj['status'] = trip.status 
        
        if tour.dates.strftime('%Y-%m-%d') < today.strftime('%Y-%m-%d'):
            if not ratings:
                obj['rating'] = True
                obj['review'] = False
            else:
                obj['rating'] = True
                obj['review'] = True
        else:
            obj['rating'] = False
            obj['review'] = True
        

        output.append(obj)
     
    return output



if __name__ == '__main__':
    from server import app
    connect_to_db(app)