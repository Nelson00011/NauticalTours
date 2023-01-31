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


#hompage
@app.route('/')
@app.route('/homepage')
def homepage():
    """View homepage for site"""
    user_id = session.get('primary_key', 0)
    if user_id == 0:
        logIn = False
    else:
        session['status'] = session.get('status', False)
        logIn = session.get('status', False)
    

    return render_template('homepage.html', logIn = logIn)



#generating a user & account settings
@app.route('/account')
def account():
    """Ability to access account."""
    #redirect to user account page
    logIn = session.get('status', False)
    user_id = session['primary_key']
    user = crud.get_user_by_id(user_id)
    trips = crud.get_trips_by_id(user_id)
    # if trips:
    #     trips = False
    print("TEST")
    print(trips)
    
    profile_list = crud.get_profile_list(trips)
   

    return render_template('account.html', logIn=logIn, user=user, trips=trips, profile=profile_list)

#direct to sign-up page
@app.route("/sign_up")
def sign_up_page():
    """Ability to access account."""
    #redirect to user account page
    logIn = session.get('status', False)
    
    return render_template('sign_up.html' , logIn = logIn)

#direct to login page
@app.route("/login_page")
def login_page():
    """Ability to access account."""
    #redirect to user account page
    logIn = session.get('status', False)
    
    return render_template('login.html' , logIn = logIn)

#generate user account HELP HERE
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
        flash('Email already in use. Account already exists.')
    else:
        new_user = crud.create_user(fname, lname, phone, password, email, birthday)
        db.session.add(new_user)
        db.session.commit()
        session['status'] = True
        flash('Success! Account created.')
    
    logIn = session.get('status', False)
    return render_template('login.html', logIn = logIn)


#login to user account
@app.route('/login',  methods = ['POST'])
def login():
    """Login to user account."""
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = crud.get_user_by_email(email)

    if not user:
        flash('User does not exist. Please check spelling or Sign-up for Account.')
    elif user.password == password:
        user = crud.get_user_by_id(user.user_id)
        session['primary_key'] = user.user_id
        session['status'] = True
        logIn = session.get('status', False)
        # logged in maybe
        return redirect('/account')    
    else:
        flash('Password does not match. Please try again.')

    logIn = session.get('status', False)
    return render_template('login.html', logIn=logIn)
  

# 
# @app.route('/logged_in')
# def logged_in(user_info):
#     logIn = session.get('status', False) 
#     return render_template('account.html', logIn=logIn)


#log out of user account
@app.route('/logout', methods = ['GET','POST'])
def logout():
    """Logout to of a user account."""
    session['status'] = False
    session['primary_key'] = False
    logIn = session['status']

    return render_template('homepage.html', logIn=logIn)


#major tour packages 
@app.route('/tours')
def tour_display():
    """General tours page."""
    #get Tour classes
    tours = crud.get_tours()
    
    logIn = session.get('status', False)
    return render_template('tours.html', logIn=logIn, tours=tours)

#individual packages page and port cities 
#google API
@app.route('/tours/<tour_id>')
def individual_tours(tour_id):
    """individual tours page."""
    tour = crud.get_tour_by_id(tour_id)

    logIn = session.get('status', False)
    return render_template('tour_details.html', logIn=logIn, tour=tour)

@app.route('/bookTrip', methods = ['POST'])
def book_trip():
    """book trip JSON"""
    user_id = session['primary_key']
    tour_id = request.json.get("trip_id")
    intention = request.json.get("intention")
    
    #check if a trip already exists
    booked = crud.get_triplist_by_user_tour(user_id, tour_id, "Book Trip")
    saved = crud.get_triplist_by_user_tour(user_id, tour_id, "Save Trip")
    print(saved)
    print(booked)

    current = crud.get_triplist_by_user_tour(user_id, tour_id, intention)
    print(booked)
    print(current)
    
    if not booked and not current:
        #book a trip and update the crud database.
        #TODO eventually convert previously saved trips to booked
        #can use for user data?

        
        trip = crud.create_trip(user_id, tour_id, intention, status='submitted')
        db.session.add(trip)
        db.session.commit()
        #update the model here on line 
        tour_name = crud.get_tour_by_id(tour_id).tour_name
        return {
            "success": True, 
            "status": f"Congratulations you have completed added Tour: {tour_name}, Intention: {intention}"}
    else:
        tour_name = crud.get_tour_by_id(tour_id).tour_name
        return {
            "success": False, 
            "status": f"Unable to complete task for Tour: {tour_name}, Intention has already been declared: {intention}"}



#about page
@app.route('/about')
def about():
    """General about page."""

    #redirect to user account page
    logIn=session.get('status', False)
    return render_template('about.html', logIn = logIn)


# #contact submission form for website (consider eliminating)
# @app.route('/contact')
# def contact_submission():
    
#     #redirect to user account page
#     logIn = session['status'] or False
#     return render_template('contact.html', logIn = logIn)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
    