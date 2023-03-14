"""Models for users Tours app. completed"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'
    #contact information for user
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    #login information for user
    password = db.Column(db.LargeBinary(), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    #payment information default zero
    balance = db.Column(db.Float, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
     
    trips = db.relationship('Trip', back_populates='user')
    rating = db.relationship('Rating', back_populates='user')

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'



class Trip(db.Model):
    """A trip."""

    __tablename__ = 'trip'
    #link to Tour package
    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.tour_id'))
    intention = db.Column(db.String(25), nullable=False)
    status = db.Column(db.String(25), nullable=True)
     
    user = db.relationship('User', back_populates='trips')
    tour = db.relationship("Tour", back_populates = 'trips')

    def __repr__(self):
        return f'<Trip trip_id={self.trip_id} user_id={self.user_id}>'



class Rating(db.Model):
    """A rating."""

    __tablename__ = 'rating'
    #link to Tour package
    rate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    tour_name  = db.Column(db.String, nullable = False)
    dates = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=True)
     
    user = db.relationship('User', back_populates='rating')
    
    def __repr__(self):
        return f'<Rating rating_id={self.rate_id} rating={self.rating}>'


class Tour(db.Model):
    """A tour package."""

    __tablename__ = 'tours'
    #link to Tour package
    tour_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tour_name = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable = False)
    price = db.Column(db.Integer, nullable=False)
    dates = db.Column(db.Date, nullable=False)
    days = db.Column(db.Integer)
    port_id = db.Column(db.String(10), nullable=False)
    port_name = db.Column(db.String(30), nullable=False)
    state_name = db.Column(db.String(30), nullable=False)

    trips = db.relationship("Trip", back_populates = 'tour')
       
    def __repr__(self):
        return f'<Tour tour_id={self.tour_id} tour_name={self.tour_name}>'



def connect_to_db(app,  db_uri="nautical", echo = False):
    """Connect to database."""
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_uri}"
    app.config["SQLALCHEMY_ECHO"] = echo
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    
    
    connect_to_db(app)
    db.create_all()    
    app.app_context().push()