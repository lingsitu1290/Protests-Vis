"""Protests Server"""

import os

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session, jsonify)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Event


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def heat():
    """Heatmap of protests."""

    return render_template("heat.html")

@app.route('/events.json')
def latlong():
    """JSON information about events."""

    events = {
        event.event_id: {
            "fullDate": event.full_date,
            "latitude":event.latitude,
            "longitude":event.longitude,
            "url":event.url
        }
        for event in Event.query.filter(Event.full_date=='20160815')}

    return jsonify(events)

@app.route('/analyze')
def analyze():
    """Interactively analyze Gdelt data."""

    return render_template("analyze.html")



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    # needed for running on vagrant
    app.run(host="0.0.0.0")
    app.run()