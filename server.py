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
            "eventCode": event.event_code,
            "latitude": event.latitude,
            "longitude": event.longitude,
            "url": event.url
        }
        for event in Event.query.filter(Event.full_date == fullDate).all()}

    return jsonify(events)


@app.route('/events')
def getEvents():
    """JSON full date information for all events in 2016."""

    events ={
        event.full_date: {
            "fullDate": event.full_date,
        }
    for event in sorted(set(db.session.query(Event.full_date).filter(Event.year =='2016')))}

    return jsonify(events)


@app.route('/analyze')
def analyze():
    """ Displays analysis of events based on date given by user. """

    return render_template("analyze.html")


@app.route('/eventcode/<fullDate>.json')
#more informative function name events?
def eventCode(fullDate):
    """JSON information about events based on what the fullDate is."""

    eventCode141 = Event.query.filter(Event.full_date == fullDate, Event.event_code =='141').all()
    eventCode142 = Event.query.filter(Event.full_date == fullDate, Event.event_code =='142').all()
    eventCode143 = Event.query.filter(Event.full_date == fullDate, Event.event_code =='143').all()
    eventCode144 = Event.query.filter(Event.full_date == fullDate, Event.event_code =='144').all()
    eventCode145 =Event.query.filter(Event.full_date == fullDate, Event.event_code =='145').all()

    data_dict = {
                "labels": [
                    "141 : Demonstrate or rally",
                    "142 : Conduct hunger strike",
                    "143 : Conduct strike or boycott",
                    "144 : Obstruct passage, block",
                    "145 : Protest violently, riot",
                ],
                "datasets": [
                    {
                        # "data": [len(eventCode141), len(eventCode142), len(eventCode143), len(eventCode144), len(eventCode145)],
                        "data": [200, 50, 100, 20, 10],
                        "backgroundColor": [
                            "#FF6384",
                            "#4BC0C0",
                            "#FFCE56",
                            "#E7E9ED",
                            "#36A2EB"
                        ],
                        "hoverBackgroundColor": [
                            "#FF6384",
                            "#4BC0C0",
                            "#FFCE56",
                            "#E7E9ED",
                            "#36A2EB"
                        ]
                    }]
            }

    return jsonify(data_dict)




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





