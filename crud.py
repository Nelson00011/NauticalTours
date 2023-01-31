"""CRUD operations"""

from model import db, User, Trip, Tour, connect_to_db

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




def get_profile_list(trip_list):
    """Returns trips  information with specified user_id. """
    output = []
    if trip_list == []:
        return False
    
    for trip in trip_list:
        Tour = get_tour_by_id(trip.tour_id)
        obj = {}
        obj['tour'] = Tour.tour_name
        obj['date'] = Tour.date
        action = trip.intention.split()[0]
        print(action)
        if action.endswith('e'):
            action=action+"d" 
        else:
            action=action+"ed"
        obj['action'] = action
        obj['status'] = trip.status

        output.append(obj)
     
    return output



#Tour Related Functions
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
    """Returns user with specified id. """
    
    return Tour.query.get(tour_id)


    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)