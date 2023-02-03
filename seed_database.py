"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server


# database will be dropped first than created
os.system('dropdb nautical')
os.system('createdb nautical')
model.connect_to_db(server.app)
model.db.create_all()

#MOCK DATA
tours = [{
    'name': "Artic Winds",
    'details': " Massive, magnificent, and unforgiving, Alaska is a land area of superlatives that will leave your mind searching for words to describe it. Each day presents a new discovery, whether you’re cruising through ice-choked waterways, trekking through chattering puffins rookeries, or catching artic fox and humpbacks breaching in the pristine waters",
    'price': 1500, 
    'date': '2023-06-29',
    'days' : 8,
    'port_id': '24', 
    'port_name': 'Port of Anchorage',
    'state_name': 'alaska'
    },
    {
    'name': "Polynesian Breezes",
    'details': "A magical blend of culture, people, nature, activities, weather, culinary delights, nightlife, and beautiful accommodation",
    'price': 2000, 
    'date': '2023-05-03',
    'days': 10,
    'port_id': '39', 
    'port_name': 'Port of Honolulu',
    'state_name': 'hawaii'
    },
    {
    'name': "NorthWest Best",
    'details': "A dynamic, urban city surrounded by unmatched natural beauty—and now it’s all open for you to explore",
    'price': 1700, 
    'date': '2023-07-15',
    'days': 10,
    'port_id': '30', 
    'port_name': 'Port of Seattle',
    'state_name': 'washington'
    },
    {
    'name': "Artic Winds",
    'details': " Massive, magnificent, and unforgiving, Alaska is a land area of superlatives that will leave your mind searching for words to describe it. Each day presents a new discovery, whether you’re cruising through ice-choked waterways, trekking through chattering puffins rookeries, or catching artic fox and humpbacks breaching in the pristine waters",
    'price': 1500, 
    'date': '2019-06-29',
    'days' : 8,
    'port_id': '24', 
    'port_name': 'Port of Anchorage',
    'state_name': 'alaska'
    }
]

user_list = [
    ("John","Doe", '555-555-5555', "ego", "John@doe.com", '01/01/1994'),
    ("Jane","Doe", '777-777-7777','ego', "Jane@doe.com", '02/02/1990'),
    ("Lulu", "Blu", '666-666-6666', 'blue', 'lulu@blu.com', '03/03/1990')
    ]

rating_list = [
    (3, "Artic Winds", 5, "Amazing experience once in a life time for the 2019 sailing tour"),
    (3, "Polynesian Breezes", 4, "Couldn't ask for better tour guides"),
    (3, "NorthWest Best", 5, "Loved the Urban vibes once we docked, great team! Helpful in training entry level crewman like me."),
    (2, "Artic Winds", 5, "This is an amazing experience that couldn't be described"),
    (2, "Polynesian Breezes", 5, "Positive life experience I wouldn't change for anything"),
    (2, "NorthWest Best", 5, "Loved the sailing tour and the port trip was incredible"),
    (1, "Artic Winds", 5, "Enjoyed the sailboat we learned to sail with and helped get sea legs"),
    (1, "Polynesian Breezes", 5, "Amazing experience once in a life time")
    ]
 
trip_list = [
    (3,4, 'Book Trip')
    ]


# Create Tours, store them in list so we can use them
def tour_database():
    """Generate Tour Database"""
    tours_in_db = []
    for index,item in enumerate(tours):
        tour_name = tours[index]['name']
        details = tours[index]['details']
        price = tours[index]['price']
        date = datetime.strptime(tours[index]['date'], '%Y-%m-%d')
        days = tours[index]['days']
        port_id = tours[index]['port_id']
        port_name = tours[index]['port_name']
        state_name = tours[index]['state_name']
                
        #create individual tour classes and append here
        db_tour = crud.create_tour(tour_name, details, price, date, port_id, port_name, state_name, days = 9)
        tours_in_db.append(db_tour)
        
    model.db.session.add_all(tours_in_db)
    model.db.session.commit()

# for userfille
def user_database():
    """Generate User Database"""
    users_in_db = []
    for person in user_list:
        fname, lname, phone, password, email, birthday = person
        db_user = crud.create_user(fname, lname, phone, password, email, birthday)
        users_in_db.append(db_user)
        
    model.db.session.add_all(users_in_db)
    model.db.session.commit()


def rating_database():
    """Generate Rating Database"""
    rating_in_db = []
    for rate in rating_list:
        user_id, tour_id, rating, review = rate
        db_rating = crud.create_rating(user_id, tour_id, rating, review)
        rating_in_db.append(db_rating)
    model.db.session.add_all(rating_in_db)
    model.db.session.commit()

def trip_database():
    """Generate Rating Database"""
    trip_in_db = []
    for trip in trip_list:
        user_id, tour_id, intention = trip 
        db_trip = crud.create_trip(user_id, tour_id, intention, status='completed')
        trip_in_db.append(db_trip)
    model.db.session.add_all(trip_in_db)
    model.db.session.commit()


    

#call functions
tour_database()
user_database()
rating_database()
trip_database()