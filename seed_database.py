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

#mock data
tours = [{
    'name': "Artic Winds",
    'details': " Massive, magnificent, and unforgiving, Alaska is a land area of superlatives that will leave your mind searching for words to describe it. Each day presents a new discovery, whether you\’re cruising through ice-choked waterways, trekking through chattering puffins rookeries, or catching artic fox and humpbacks breaching in the pristine waters",
    'price': 1500, 
    'date': '2023-10-29',
    'day' : 8
    },
{
    'name': "Polynesian Breezes",
    'details': "A magical blend of culture, people, nature, activities, weather, culinary delights, nightlife, and beautiful accommodation.",
    'price': 2000, 
    'date': '2023-05-03',
    'days': 10
},
{
    'name': "NorthWest Best",
    'details': "A dynamic, urban city surrounded by unmatched natural beauty—and now it\’s all open for you to explore.",
    'price': 1700, 
    'date': '2023-03-15',
    'days': 10
}
]

# user_test = [(name, email, etc... )]
# Create Tours, store them in list so we can use them
# to create fake Tours to populate
tours_in_db = []
for index in tours:
    # TODO: get the title, overview, and poster_path from the movie dictionary. 
       
    tour_name = tours[index][0]['name']
    tour_na = tours[0]['name']
    print("TEST")
    print(tour_name)
    print(tour_na)
    details = tours[index]['details']
    price = tours[index]['price']
    date = datetime.strptime(tours[index]['date'], '%Y-%m-%d')
    days = tours[index]['days']
    
    
    # TODO: create a movie here and append it to movies_in_db
    db_tour = crud.create_tour(tour_name, details, price, date, days)
    tours_in_db.append(db_tour)
    print(db_tour)
    #add individual in the scope of the loop.
    model.db.session.add(db_tour)
model.db.session.add_all(tours_in_db)
model.db.session.commit()

# for index 