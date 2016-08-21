"""Protests Server"""

import os

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session, jsonify, g)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Event


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined

# Add Jasmine testing for JavaScript 
JS_TESTING_MODE = False

@app.before_request
def add_tests():
    g.jasmine_tests = JS_TESTING_MODE

@app.route('/')
def heat():
    """Heatmap of protests."""

    return render_template("heat.html")

#add info to route name, dynamically generate full_date
#refactor into class /events/<int:full_date>.json'
@app.route('/events/<fullDate>.json')
#more informative function name events?
def latlong(fullDate):
    """JSON information about events based on what the fullDate is."""

    events = {
        event.event_id: {
            "fullDate": event.full_date,
            "latitude": event.latitude,
            "longitude": event.longitude,
            "url": event.url
        }
        for event in Event.query.filter(Event.full_date == fullDate).all()}

    return jsonify(events)


@app.route('/events')
def getEvents():
    """JSON information about events."""

    events ={
        event.full_date: {
            "fullDate": event.full_date,
        }
    for event in sorted(set(db.session.query(Event.full_date).filter(Event.year =='2016')))}

    return jsonify(events)
   




if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "jstest":
        JS_TESTING_MODE = True

    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    # needed for running on vagrant
    app.run(host="0.0.0.0")
    app.run()





