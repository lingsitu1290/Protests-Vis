"""Models and database functions for Protests Project."""

from flask_sqlalchemy import SQLAlchemy

#Instantiate SQLAlchemy object
db = SQLAlchemy()

# Model definitions

class Event(db.Model):
    """Protest event time and date."""

    __tablename__ = "events"

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    full_date = db.Column(db.String(20), nullable=False)
    event_code = db.Column(db.String(20), nullable=False)
    full_location = db.Column(db.String(300), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    url = db.Column(db.String(600), nullable=True)

    def __repr__(self):
        """Present event details when printed."""

        return "<Event=%s full_date=%s full_location=%s>" %(self.event_id, self.full_date, self.full_location)

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///protests'
    db.app = app 
    db.init_app(app)

if __name__ == "__main__":
    # Used to run module interactively 
    import os
    os.system("dropdb protests")
    os.system("createdb protests")

    from server import app
    connect_to_db(app)
    print "Connect to DB."