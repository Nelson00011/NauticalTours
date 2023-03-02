from flask import (Flask, render_template, request,flash, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from datetime import datetime, date, timedelta
from flask_bcrypt import Bcrypt
import sendgrid
import os
from sendgrid.helpers.mail import *
import babel



app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    
    #get Tour classes
    tours = crud.get_tours()
    today = date.today()

    #compose list of future tours only
    tour_list = []
    for tour in tours:     
        if tour.dates.strftime('%Y-%m-%d') > today.strftime('%Y-%m-%d'):
            tour_list.append(tour)
    tour_list = sorted(tour_list, key=lambda x: x.dates.strftime('%Y-%m-%d'))

    return render_template('homepage.html', logIn = logIn, tours=tour_list)


#account/profile page
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

#login page
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
    print("PASSWORD RAW")
    print(password)
    pw_hash = bcrypt.generate_password_hash(password)
    print("Password Lime1111*")
    print(pw_hash)
    email = request.form.get('email')
    birthday = request.form.get('birthday')
   
    
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
    #confirmation that hash password == stored password
    confirmation = bcrypt.check_password_hash(pw_hash, password)
    
    if not user:
        flash('User does not exist. Please check spelling or Sign-up for Account.')
    elif confirmation:
        user = crud.get_user_by_id(user.user_id)
        session['primary_key'] = user.user_id
        session['status'] = True
        logIn = session.get('status', False)
        return redirect('/account')
    else:
        flash('Password does not match. Please try again.')

    logIn = session.get('status', False)
    return render_template('login.html', logIn=logIn)
  


#logout
@app.route('/logout', methods = ['GET','POST'])
def logout():
    """Logout to of a user account."""
    session['status'] = False
    session['primary_key'] = False
    logIn = session['status']

    return redirect('/')

#date converters
@app.template_filter()
def format_datetime(value, format='medium'):
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    return babel.dates.format_datetime(value, format)
    
#tours page
@app.route('/tours')
def tour_display():
    """General tours page."""
    #get Tour classes
    tours = crud.get_tours()
    today = date.today()

    #compose list of future tours only
    tour_list = []
    for tour in tours:     
        if tour.dates.strftime('%Y-%m-%d') > today.strftime('%Y-%m-%d'):
            tour_list.append(tour)
    tour_list = sorted(tour_list, key=lambda x: x.dates.strftime('%Y-%m-%d'))
    logIn = session.get('status', False)
    return render_template('tours.html', logIn=logIn, tours=tour_list)

#Individual Port Pages.
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
    tour_id = request.json.get("tour_id")
    intention = request.json.get("intention")
    tour_name = crud.get_tour_by_id(tour_id).tour_name
    
    if not user_id:
        return {
            "success": False, 
            "status": f"Unable to complete task for Tour: {tour_name}, not Logged In."}
    
    booked = crud.get_triplist_by_user_tour(user_id, tour_id, "Book Trip")
    saved = crud.get_triplist_by_user_tour(user_id, tour_id, "Save Trip")
    current = crud.get_triplist_by_user_tour(user_id, tour_id, intention)
        
    if not booked and not current:
        if intention == "Book Trip":
            crud.update_saved_trips(user_id, tour_id, intention)
        
        trip = crud.create_trip(user_id, tour_id, intention, status='submitted')
        db.session.add(trip)
        db.session.commit()
        
        return {
            "success": True, 
            "status": f"Congratulations you have completed added Tour: {tour_name}, and the you have {intention}"}
    
    else:
        tour_name = crud.get_tour_by_id(tour_id).tour_name
        return {
            "success": False, 
            "status": f"Unable to complete task for Tour: {tour_name}, the Tour has already been booked or saved."}
    

@app.route("/removeTrip", methods = ['POST'])
def remove_trip():
    """remove book trip JSON"""
    user_id = session['primary_key']
    trip_id = request.json.get("trip_id")
    intention = request.json.get("intention")
    action = request.json.get("action")
    
    trip = crud.get_trips_by_trip_id(trip_id)
    tour = crud.get_tour_by_id(trip.tour_id)
    
    
    if action!="Saved":
        crud.update_user_balance(-(tour.price), user_id)
    user = crud.get_user_by_id(user_id)
        
    db.session.delete(trip)
    db.session.commit()
    
    return {
            "success": True, 
            "status": f"Congratulations you have removed Tour: {tour.tour_name} .",
            "balance": user.balance }


#About Page
@app.route('/about')
def about():
    """General about page."""

    #redirect to user account page
    logIn=session.get('status', False)
    return render_template('about.html', logIn = logIn)

#Contact/Comments send emails confirmation to User & Company
@app.route('/comment', methods = ['POST'])
def comment_submission():
    email = request.form.get('email')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    comments = request.form.get('comments')
    
    #send confirmation email to client
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    sender_email = os.environ.get("EMAIL")
    from_email = Email(sender_email)
    user = To(email)
    company = To(sender_email)
    subject = "Confirmation of Comment: Nautical Tours"

    #send confirmation email to internal
    mail = Mail(from_email, company, subject)
    mail.dynamic_template_data = {
        'first_name': fname,
        'last_name': lname,
        'email': email,
        'comments': comments
    }
    mail.template_id = 'd-d2e504db0885402bab831f6fe166794d'

    confirmation_email = Mail(from_email, user, subject)
    confirmation_email.dynamic_template_data = {
    'first_name': fname,
    }

    confirmation_email.template_id = 'd-228a5378ba514fe3973179a20035a5aa'
    response = sg.client.mail.send.post(request_body=mail.get())
    response = sg.client.mail.send.post(request_body=confirmation_email.get())
    flash('Thank you for submitting your comment. You will recieve a confirmation email soon.')
  
    return redirect('/about')


#review page
@app.route('/review/<trip_id>')
def review(trip_id):
    """General a review page."""
    #get rating for trip by tour_id name of the tour
    trip = crud.get_trips_by_trip_id(trip_id)
    tour = crud.get_tour_by_id(trip.tour_id)
    
    #storing current trip date
    #storing current trip name
    session['dates'] = tour.dates
    session['tour_id'] = tour.tour_id
    #redirect to user account page
    logIn=session.get('status', False)
    return render_template('review.html', logIn = logIn, tour=tour)


@app.route('/review_submission',  methods = ['POST'])
def review_submission():
    """Review Submission to user account."""
    user_id = session['primary_key']
    user = crud.get_user_by_id(user_id)

    tour_id = session['tour_id']
    dates = session['dates']

    score = request.form.get('star')
    reviews = request.form.get('comments')
    tour = crud.get_tour_by_id(tour_id)
    tour_name=tour.tour_name
    trips = crud.get_trips_by_id(user_id)
    profile_list = crud.get_profile_list(trips)

    rating = crud.get_rating_by_user_id_tour_id_dates(user_id,tour_id, dates)
    
    if rating:
        crud.update_rating_by_rating_id(user_id, tour_id, dates, score, reviews)
        
        flash('Thank you for updating a Review!')
    else:   
        rating = crud.create_rating(user_id, tour_name, dates, score, reviews)
        db.session.add(rating)
        db.session.commit()
        flash('Thank you for submitting a Review!')

    logIn = session.get('status', False)
    return render_template('account.html', logIn=logIn, user=user, trips=trips, profile=profile_list)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
    