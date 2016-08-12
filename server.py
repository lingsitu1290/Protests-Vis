"""Protests Server"""

# from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

# from model import connect_to_db, db, Event


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
# app.jinja_env.undefined = StrictUndefined

@app.route('/')
def heat():
    """Heatmap of protests."""

    return render_template("heat.html")

@app.route('/analyze')
def analyze():
    """Interactively analyze Gdelt data."""

    return render_template("analyze.html")

@app.route('/sentiment')
def sentiment():
    """Sentiment analysis of events."""

    return render_template("sentiment.html")

## Add feature?
# @app.route('/submit')
# def submit():
#     """User can submit articles."""

#     pass


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    # needed for running on vagrant
    app.run(host="0.0.0.0")
    app.run()