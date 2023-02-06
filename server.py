from flask import (Flask, render_template, request,flash, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from datetime import datetime, date, timedelta
from flask_bcrypt import Bcrypt
import sendgrid
import os
from sendgrid.helpers.mail import *


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

# bcrypt = Bcrypt(app)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']


#hompage
@app.route('/')
@app.route('/homepage')
def homepage():
    """View homepage for site"""
    session['primary_key'] = session.get('primary_key', False)
    user_id = session.get('primary_key', False)
    if not user_id:
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

#generate user account 
@app.route('/users', methods = ['POST'])
def register_user():
    """Create a new user."""
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    phone = request.form.get('phone')
       
    password = request.form.get('password')
    pw_hash = bcrypt.generate_password_hash(password)
    
    email = request.form.get('email')
    birthday = request.form.get('birthday')
    #force user to log into site
    
    user = crud.get_user_by_email(email)
    if user:
        flash('Email already in use. Account already exists.')
    else:
        new_user = crud.create_user(fname, lname, phone, pw_hash, email, birthday)
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
    pw_hash = user.password
    #confirmation that hash password matches stored password
    confirmation = bcrypt.check_password_hash(pw_hash, password)
    
    if not user:
        flash('User does not exist. Please check spelling or Sign-up for Account.')
    elif confirmation:
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
    today = date.today()

    #compose list of future tours only
    tour_list = []
    for tour in tours:     
        if tour.date.strftime('%Y-%m-%d') > today.strftime('%Y-%m-%d'):
            tour_list.append(tour)
    tour_list = sorted(tour_list, key=lambda x: x.date.strftime('%Y-%m-%d'))
    logIn = session.get('status', False)
    return render_template('tours.html', logIn=logIn, tours=tour_list)

#individual packages page and port cities 
#google API
@app.route('/tours/<tour_id>')
def individual_tours(tour_id):
    """individual tours page."""
    tour = crud.get_tour_by_id(tour_id)
    ratings = crud.get_rating_by_tour_name(tour.tour_name)

    logIn = session.get('status', False)
    return render_template('tour_details.html', logIn=logIn, tour=tour, ratings=ratings)

@app.route('/bookTrip', methods = ['POST'])
def book_trip():
    """book trip JSON"""
    user_id = session['primary_key']
    print("TEST")
    print(user_id)
    tour_id = request.json.get("trip_id")
    intention = request.json.get("intention")
    tour_name = crud.get_tour_by_id(tour_id).tour_name
    
    #check if a trip already exists
    if not user_id:
        
        return {
            "success": False, 
            "status": f"Unable to complete task for Tour: {tour_name}, not Logged In."}
    
    booked = crud.get_triplist_by_user_tour(user_id, tour_id, "Book Trip")
    saved = crud.get_triplist_by_user_tour(user_id, tour_id, "Save Trip")
    current = crud.get_triplist_by_user_tour(user_id, tour_id, intention)
        
    if not booked and not current:
        #book a trip and update the crud database.
        #TODO eventually convert previously saved trips to booked
        if intention == "Book Trip":
            crud.update_saved_trips(user_id, tour_id, intention)
        
        trip = crud.create_trip(user_id, tour_id, intention, status='submitted')
        db.session.add(trip)
        db.session.commit()
        #update the model here on line 
        
        return {
            "success": True, 
            "status": f"Congratulations you have completed added Tour: {tour_name}, and the you have {intention}"}
    
    else:
        tour_name = crud.get_tour_by_id(tour_id).tour_name
        return {
            "success": False, 
            "status": f"Unable to complete task for Tour: {tour_name}, the Tour has already been booked or saved."}
    



#about page
@app.route('/about')
def about():
    """General about page."""

    #redirect to user account page
    logIn=session.get('status', False)
    return render_template('about.html', logIn = logIn)


#contact form that sends 
#email to use confirming that their comment was submited
#sends email the company as for them to respond to. 
@app.route('/comment', methods = ['POST'])
def comment_submission():
    email = request.form.get('email')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    comments = request.form.get('comments')
    #send email to self first to be responded to. 
    #send email to confirmation Email next
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    sender_email = os.environ.get("EMAIL")
    from_email = Email(sender_email)
    user = To(email)
    company = To(sender_email)
    subject = "Confirmation of Comment: Nautical Tours"

    #email to internal
    mail = Mail(from_email, company, subject)
    mail.dynamic_template_data = {
        'first_name': fname,
        'last_name': lname,
        'email': email,
        'comments': comments
    }
    mail.template_id = 'd-d2e504db0885402bab831f6fe166794d'

    #email to individual
    
    confirmation_email = Mail(from_email, user, subject)
    confirmation_email.dynamic_template_data = {
    'first_name': fname,
    }

    confirmation_email.template_id = 'd-228a5378ba514fe3973179a20035a5aa'
    response = sg.client.mail.send.post(request_body=mail.get())
    response = sg.client.mail.send.post(request_body=confirmation_email.get())
    flash('Thank you for submitting your comment. You will recieve a confirmation email soon.')
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return redirect('/about')


#review page
@app.route('/review')
def review():
    """General a review page."""

    #redirect to user account page
    logIn=session.get('status', False)
    return render_template('review.html', logIn = logIn)

@app.route('/review_submission',  methods = ['POST'])
def review_submission():
    """Review Submission to user account."""
    tour_name = request.form.get('tour')
    rating = request.form.get('rating')
    review = request.form.get('comment')
    user_id = session['primary_key']
    user = crud.get_user_by_id(user_id)
    trips = crud.get_trips_by_id(user_id)
         
    profile_list = crud.get_profile_list(trips)

    rating = crud.create_rating(user_id, tour_name, rating, review)
    db.session.add(rating)
    db.session.commit()
    flash('Thank you for submitting a Review!')

    logIn = session.get('status', False)
    return render_template('account.html', logIn=logIn, user=user, trips=trips, profile=profile_list)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
    