from flask import (Flask, render_template, request,flash, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

# routes and functions below

#hompage
@app.route('/')
def homepage():
    '''View homepage for site'''
    return render_template('homepage.html')



#generating a user & account settings
@app.route('/account')
def account():
    #redirect to user account page

    return render_template('account.html')

# individual account
@app.route('/users', methods = ['POST'])
def register_user():
    """Create a new user."""
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    phone = request.form.get('phone')
   
    password = request.form.get('password')
    email = request.form.get('email')

    birthday = request.form.get('birthday')


    user = crud.get_user_by_email(email)
    if user:
        Alert('Email already in use. Account already exists.')
    else:
        new_user = crud.create_user(fname, lname, phone, password, email, birthday)
        db.session.add(new_user)
        db.session.commit()
        Alert('Success! Account created.')
    
    return redirect('account.html')

@app.route('/login',  methods = ['POST'])
def login():
    """Login to user account."""
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user.password == password:
        session['primary_key'] = user.user_id
        print(session)
        Alert('Logged In!')
    else:
        Alert('Password does not match.')
        
    return redirect('/')




#major tour packages 
@app.route('/tours')
def tour_display():
    
    
    return render_template('tours.html')



#individual packages page and port cities 
#google API



#history page
@app.route('/history')
def history():
    
    #redirect to user account page

    return render_template('history.html')


#contact submission form for website
@app.route('/contact')
def contact_submission():
    
    #redirect to user account page

    return render_template('contact.html')








if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
    