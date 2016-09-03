# Visualizations of 2016 Global Protests

Inspired by the attempted Turkish coup on July 15th 2016, this project was created to visualize and analyze 2016 protests around the world over time. An application programming interface was also created for ease of access to the data for developers. Users can click on the slider in the map view to scroll through dates, which changes the map to display that day's protests. The size of markers depends on the number of events for that particular latitude and longitude. Markers are also clickable for the first URL associated with the event. In the analysis view, users can select a month and day to display charts for further analysis.

Learn more about the developer [here](www.linkedin.com/in/lingsitu1290)!

## Table of Contents

* [Tech Stack](#tech-stack)
* [Features](#features)
* [Testing Coverage](#test)
* [How to Run](#run)
* [Data](#data)
* [Future Development](#future)

## <a name="tech-stack"></a>Technology Stack

* Back-End: Python, JavaSript, Flask Restless, Beautiful Soup, Python's OS Library
* Front-End: JavaScript, jQuery, AJAX, jQuery UI, Chart.js, Bootstrap, HTML, CSS
* Database: PostgreSQL, SQLAlchemy ORM
* APIs: Google Maps JavaScript API

## <name="features"></a>Features

## <a name="test"></a>Testing Coverage

## <a name="run"></a>How to Run

  1. Create a virtual environment 
    ```
    > virtualenv env
    > source env/bin/activate
    ```
  2. Install the dependencies 
    ```
    > pip install -r requirements.txt
    ```
  3. In a new Terminal run App
    ```
    > python server.py
    ```
  4. Open your browser and navigate to 
    ```
    http://localhost:5000/
    ```

## <a name="data"></a>Data
Data was downloaded, processed, and stored into a PostgreSQL database from the Global Database of Events, Language, and Tone Project [website](http://data.gdeltproject.org/events/index.html) using the gdelt.py script. 

## <a name="future"></a>Future Development

* Celery Distributed Task Queue: For real-time processing of protests data!
