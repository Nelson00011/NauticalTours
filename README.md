# Nautical Tours


## Description
- Nautical Tours is a Flask app built on Python and Jinja. The website is designed to allow active users to book trips to specific tours. To learn more about the company a contact form uses Twilio (Sendgrid) to send a confirmation email to user and an internal company members. Users can rate every tour they have attended with an interactive form.  Every Tour, User, Trip and Rating is saved using SQL Alchemy to communicate with PostgreSQL database. Google Maps API uses AJAX to call a specific port city that users can than explore with Google Places API to look up specific tourist attractions in the surrounding area. Bootstraps is utilized in combination with traditional CSS to have a consistent design aesthetic through-out the site.

## Screen Shots
- Sendgrid (twilio) form with character limit enforced:

![image](https://user-images.githubusercontent.com/112737682/220435463-ef5e1079-a937-46cf-a6c5-e657cb83c128.png)
-
![image](https://user-images.githubusercontent.com/112737682/221693842-5dc611fe-0515-472e-b462-92e39d30ab8a.png)


- Google Maps API with specialized Google Places markers (defined by type)
![image](https://user-images.githubusercontent.com/112737682/221691955-49a15cba-63af-4b50-8e48-14158c66bd22.png)


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


