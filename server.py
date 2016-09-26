"""Protests Server"""

import os

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session, jsonify, g)
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.restless import APIManager

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
def index():
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

    eventCode140 = Event.query.filter(Event.full_date == fullDate, Event.event_code =='140').all()
    eventCode141 = Event.query.filter(Event.full_date == fullDate, Event.event_code =='141').all()
    eventCode142 = Event.query.filter(Event.full_date == fullDate, Event.event_code =='142').all()
    eventCode143 = Event.query.filter(Event.full_date == fullDate, Event.event_code =='143').all()
    eventCode144 = Event.query.filter(Event.full_date == fullDate, Event.event_code =='144').all()
    eventCode145 = Event.query.filter(Event.full_date == fullDate, Event.event_code =='145').all()

    data_dict = {
                "labels": [
                    # 140, 141, 142, 143, 144, 145
                    "Engage in Political dissent",
                    "Demonstrate or rally",
                    "Conduct hunger strike",
                    "Conduct strike or boycott",
                    "Obstruct passage, block",
                    "Protest violently, riot",
                ],
                "datasets": [
                    {
                        "data": [len(eventCode140), 
                                 len(eventCode141), 
                                 len(eventCode142), 
                                 len(eventCode143), 
                                 len(eventCode144), 
                                 len(eventCode145)],
                        "backgroundColor": [
                            "#FF6384",
                            "#4BC0C0",
                            "#FFCE56",
                            "#E7E9ED",
                            "#36A2EB",
                            "#ccb3ff",

                        ],
                        "hoverBackgroundColor": [
                            "#FF6384",
                            "#4BC0C0",
                            "#FFCE56",
                            "#E7E9ED",
                            "#36A2EB",
                            "#ccb3ff",
                        ]
                    }]
            };

    return jsonify(data_dict)

@app.route('/yearchart.json')
#more informative function name events?
def year_data():
    """JSON information about events based on what the fullDate is."""
    
    jan = Event.query.filter(Event.full_date.like('201601%'))
    feb = Event.query.filter(Event.full_date.like('201602%'))
    mar = Event.query.filter(Event.full_date.like('201603%'))
    apr = Event.query.filter(Event.full_date.like('201604%'))
    may = Event.query.filter(Event.full_date.like('201605%'))
    june = Event.query.filter(Event.full_date.like('201606%'))
    july = Event.query.filter(Event.full_date.like('201607%'))
    aug = Event.query.filter(Event.full_date.like('201608%'))

    data_dict = {
                "labels": ["January", "February", "March", "April", "May", "June", "July", "August"],
                "datasets": [
                    {
                        "label": "Protests in 2016",
                        "backgroundColor": [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                        ],
                        "borderColor": [
                            'rgba(255,99,132,1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)',
                            'rgba(54, 162, 235, 0.2)',
                        ],
                        "borderWidth": 1,
                        "data": [len(jan.all()), len(feb.all()), len(mar.all()), len(apr.all()), len(may.all()), len(june.all()), len(july.all()), len(aug.all())]
                    }
                ]
            };

    return jsonify(data_dict)

# Include only these columns in API
includes = ['event_id', 'event_code', 'full_date', 'latitude', 'longitude', 'full_location','url']

manager = APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Event, results_per_page=30, 
                          primary_key='event_id',
                          include_columns=includes,
                          methods=['GET'])

if __name__ == "__main__":
    # For Jasmine testing: to run type in python server.py jstest
    import sys
    if sys.argv[-1] == "jstest":
        JS_TESTING_MODE = True

    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    # app.debug = True

    connect_to_db(app, os.environ.get("DATABASE_URL"))


    # Use the DebugToolbar
    DebugToolbarExtension(app)
    # needed for running on vagrant
    app.run(host="0.0.0.0")
    app.run()