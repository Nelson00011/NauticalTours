# MVP
Initial Project Proposal
GITS: 
https://gist.github.com/Nelson00011/fbebcc152428b2c91ceb01d1124faf8a

https://github.com/Nelson00011/MVP/issues/1#issue-1534126780

# Nautical Tours


## Description
- Description here

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


