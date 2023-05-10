<h1 align="center">Nautical Tours</h1>

![homePage](https://user-images.githubusercontent.com/112737682/225162610-5ab2d59f-6c9e-45ac-a8f8-c786f76ae8a9.jpg)

## Description
**Nautical Tours** is a ***Flask*** app built on ***Python*** and ***Jinja***. The website is designed to allow active users to book and save trips to specific tour locations. Explore more about the Sailing Tours the company offers, including personalized customer reviews. 
- For Inqueries a contact form uses ***Twilio*** (Sendgrid) to send a confirmation email to user's and an internal company members to respond to. 
- Every Tour, User, Trip and Rating is saved using ***SQL Alchemy*** to communicate with ***PostgreSQL*** database. Users can rate every tour they have attended with an interactive form, that allows review generation, editing and deletion. 
- ***Google Maps API*** uses AJAX to call a specific port city that users can than explore with ***Google Places API*** to look up specific tourist attractions in the surrounding area. 
- ***Bootstraps*** is utilized in combination with traditional CSS to have a consistent design aesthetic through-out the site.

## Demo Youtube Video
- Youtube Video **[LINK HERE](https://youtu.be/-PKyqMkmOHw)**

## Screen Shots
- Sendgrid (twilio) form with character limit enforced:

![image](https://user-images.githubusercontent.com/112737682/220435463-ef5e1079-a937-46cf-a6c5-e657cb83c128.png)

![image](https://user-images.githubusercontent.com/112737682/221693842-5dc611fe-0515-472e-b462-92e39d30ab8a.png)

- Google Maps API with specialized Google Places markers (defined by type)

![polyTour](https://user-images.githubusercontent.com/112737682/225162285-e1a95918-0e96-4cb4-a8bd-639be245eae0.jpg)

![reviews](https://user-images.githubusercontent.com/112737682/225162356-451dd1d2-7264-4dc2-81f0-bc7da6680985.jpg)

## Technology stack
**Back-End:** Python, Flask, Jinja, SQLAlchemy, Bcrypt

**APIs:** Google Maps, Twilio (SendGrid)

**Front-End:** HTML5, CSS, Bootstrap, Javascript

## Run Code (Environment)

- Create and activate virtual environment (local dev only):
 ```
> pip3 install virtualenv
> virtualenv env
> source env/bin/activate
```

- Install the dependences/requirements (localhost:5000):
```
> pip3 install -r requirements.txt
```


- Create test database
```
> python3 seed_database.py
```

- Run the app:
```
> python server.py
```

- Open your browser and navigate to

http://localhost:5000/

Additional information: The login functionality requires that you have a secret.sh set as local environment variables:

SENDGRID_API_KEY

## Resources & Helpful Hints: 
- Flask installation info [here](https://flask.palletsprojects.com/en/2.3.x/):
    - [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/) for python
- Jinja Information [here](https://jinja.palletsprojects.com/en/3.1.x/)
- SQLAlchemy Database for Python [here](https://www.sqlalchemy.org/)
- Initial Proposal Approved by Hackbright [here](https://gist.github.com/Nelson00011/fbebcc152428b2c91ceb01d1124faf8a)




#### Helpful Hints
- developement environment will play a large role in dependencies/requirements
