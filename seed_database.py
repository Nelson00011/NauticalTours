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
    }
]

user_list = [
    ("John","Doe", '555-555-5555', "ego", "John@doe.com", '01/01/1994'),
    ("Jane","Doe", '777-777-7777','ego', "Jane@doe.com", '02/02/1990'),
    ("Lulu", "Blu", '666-666-6666', 'blue', 'lulu@blu.com', '03/03/1990')
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

#call functions
tour_database()
user_database()