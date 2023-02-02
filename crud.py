"""CRUD operations"""

from model import db, User, Trip, Tour, Rating, connect_to_db

#User related functions
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





#Trip Related Functions
def create_trip(user_id, tour_id, intention, status='submitted'):
    """Create and return a new trip."""
    if intention == "Book Trip":
        tour = get_tour_by_id(tour_id)
        price = tour.price
        update_user_balance(price, user_id)

    trip = Trip(
        user_id = user_id,
        tour_id = tour_id,
        intention = intention,
        status = status
     )

    return trip 
  
#booking or liking a trip
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


def get_profile_list(trip_list):
    """Returns trips  information with specified user_id. """
    output = []
    if trip_list == []:
        return False
    
    for trip in trip_list:
        Tour = get_tour_by_id(trip.tour_id)
        obj = {}
        obj['tour_id'] = Tour.tour_id
        obj['tour'] = Tour.tour_name
        obj['date'] = Tour.date
        action = trip.intention.split()[0]
        if action == 'Save':
            obj['price'] = 0.00
        else:
             obj['price'] = Tour.price
        if action.endswith('e'):
            action=action+"d" 
        else:
            action=action+"ed"
        obj['action'] = action
        obj['status'] = trip.status 

        output.append(obj)
     
    return output


#Rating related functions
def create_rating(user_id, tour_id, rating, review):
    """Create and return a new tour rating"""
    rating = Rating(
        user_id = user_id,
        tour_id = tour_id,
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

def get_rating_by_tour_id(tour_id):
    """Returns ratings with specified trip_id."""
    
    return Rating.query.filter(Rating.tour_id_== tour_id).all()

def update_rating_by_id(rate_id, user_id, comment):
    """Returns ratings with specified user_id."""

    rating = Rating.query.filter(Rating.rate_id==rate_id).all()
    if rating[0].user_id == user_id:
        rating.review = comment
        db.session.commit()
        return {'status': 'success',
        'reason': 'none'}
    else:
        return {'status': 'success',
        'reason': 'user_id'}





#Tour related Functions
def create_tour(tour_name, details, price, date, port_id, port_name,state_name, days = 9):
    """Create and return a new tour."""
    tour = Tour(
        tour_name = tour_name,
        details = details,
        price = price,
        date = date,
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




if __name__ == '__main__':
    from server import app
    connect_to_db(app)