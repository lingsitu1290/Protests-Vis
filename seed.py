"""File to seed data from ETL into protests database."""

from sqlalchemy import func
from model import Event

from model import connect_to_db, db
from server import app

# from datetime import datetime

#import from gdelt process_csv to obtain protests_data list 
from gdelt import process_csv, DATA_DIR

# Seed data into database
# Load events table                    
def load_events(protests_data):
    """Load events into database."""

    print "Events"
    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate events 
    Event.query.delete()

    # Read through each protest event all need info
    for protest in protests_data:
        event_id = protest[0]
        full_date = protest[1]
        year = protest[3]
        event_code = protest[27]
        full_location = protest[36]
        latitude = protest[39]
        longitude = protest[40]
        url = protest[57]

        if latitude == "" or longitude == "":
            continue

        event = Event(event_id=event_id,
                      full_date=full_date,
                      year=year, 
                      event_code=event_code, 
                      full_location=full_location,
                      latitude=latitude,
                      longitude=longitude,
                      url=url)

        # Add event to session
        db.session.add(event)

    # Commit to database
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    #Run protests_data function from gdelt.py and bind to protests_data
    protests_data = process_csv(DATA_DIR)

    # In case tables haven't been created, create them
    db.create_all()

    #Run load_events function with protests_data passed in
    load_events(protests_data)
