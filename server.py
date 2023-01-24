from flask import (Flask, render_template, request,flash, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from datetime import datetime
# import bcrypt


app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined
# bcrypt = Bcrypt(app)

# routes and functions below

#hompage
@app.route('/')
def homepage():
    """View homepage for site"""
    session['status'] = session.get('status', False)
    logIn = session['status']

    return render_template('homepage.html', logIn = logIn)



#generating a user & account settings
@app.route('/account')
def account():
    """Ability to access account."""
    #redirect to user account page
    session['status'] = session.get('status', False)
    logIn = session['status']

    return render_template('account.html' , logIn = logIn)

# individual account
@app.route('/users', methods = ['POST'])
def register_user():
    """Create a new user."""
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    phone = request.form.get('phone')
   
    password = request.form.get('password')
    # password_hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    email = request.form.get('email')

    birthday = request.form.get('birthday')
    #force user to log into site
    
    user = crud.get_user_by_email(email)
    if user:
        Alert('Email already in use. Account already exists.')
    else:
        new_user = crud.create_user(fname, lname, phone, password, email, birthday, logIn)
        db.session.add(new_user)
        db.session.commit()
        
        Alert('Success! Account created.')
    
    return redirect('account.html', logIn = logIn)

@app.route('/login',  methods = ['POST'])
def login():
    """Login to user account."""
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user.password == password:
        session['primary_key'] = user.user_id
        session['status'] = True
        logIn = session['status']
        print(session)
        Alert('Logged In!')
    else:
        Alert('Password does not match.')
        
    return redirect('/' , logIn = logIn)




#major tour packages 
@app.route('/tours')
def tour_display():
    """General tours page."""
    
    
    logIn = session['status']
    return render_template('tours.html', logIn = logIn)

#individual packages page and port cities 
#google API
@app.route('/tours/<tour_id>')
def individual_tours(tour_id):
    """individual tours page."""
    logIn = session.get('status', False)
    
    return render_template('tour_details.html', logIn = logIn)



#history page
@app.route('/history')
def history():
    """General history page."""

    #redirect to user account page
    logIn = session.get('status', False)
    return render_template('history.html', logIn = logIn)


# #contact submission form for website (consider eliminating)
# @app.route('/contact')
# def contact_submission():
    
#     #redirect to user account page
#     logIn = session['status'] or False
#     return render_template('contact.html', logIn = logIn)








if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
    