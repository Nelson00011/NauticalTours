# MVP
Initial Project Proposal
GITS: 
https://gist.github.com/Nelson00011/fbebcc152428b2c91ceb01d1124faf8a

https://github.com/Nelson00011/MVP/issues/1#issue-1534126780

# Nautical Tours


## Description
- Nautical Tours is a Flask app built on Python and Jinja. The website is designed to allow active users to book trips to specific tours. To learn more about the company a contact form uses Twilio (Sendgrid) to send a confirmation email to user and an internal company members. Users can rate every tour they have attended with an interactive form.  Every Tour, User, Trip and Rating is saved using SQL Alchemy to communicate with PostgreSQL database. Google Maps API uses AJAX to call a specific port city that users can than explore with Google Places API to look up specific tourist attractions in the surrounding area. Bootstraps is utilized in combination with traditional CSS to have a consistent design aesthetic through-out the site.

## Screen Shots
- Sendgrid (twilio) form with character limit enforced:

![image](https://user-images.githubusercontent.com/112737682/220435463-ef5e1079-a937-46cf-a6c5-e657cb83c128.png)


## Technology stack
**Back-End:** Python, Flask, Jinja, SQLAlchemy, Bcrypt...

**APIs:** Google Maps, Twilio (SendGrid)

**Front-End:** HTML5, CSS, Boostraps, Javascript...

## Run Code (Environment)

- Create and activate virtual environment 
 ```
> pip3 install virtualenv
> virtualenv env
> source env/bin/activate
```

- Install the dependences/requirements
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


