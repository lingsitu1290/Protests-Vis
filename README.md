# Visualizations of 2016 Global Protests

Inspired by the attempted Turkish coup on July 15th 2016, this project was created to visualize and analyze 2016 protests around the world over time. Users can click on the slider in the map view to scroll through dates, which changes the map to display that day's protests. The size of markers depends on the number of events for that particular latitude and longitude. Markers are clickable for the first URL associated with the event. In the analysis view, users can select a month and day to display charts for further analysis. Lastly, an application programming interface was created for ease of access to the data for developers.

Learn more about the developer [here](https://www.linkedin.com/in/lingsitu1290)!

## Table of Contents

* [Tech Stack](#tech-stack)
* [Features](#features)
* [Testing Coverage](#test)
* [How to Run](#run)
* [Data](#data)
* [Future Development](#future)

## <a name="tech-stack"></a>Technology Stack

* Back-End: Python, Flask Restless
* Extraction, Transformation, Loading Data: Beautiful Soup, Python's OS Library
* Front-End: JavaScript, AJAX, jQuery UI, Chart.js, Bootstrap, HTML, CSS
* Database: PostgreSQL, SQLAlchemy
* APIs: Google Maps JavaScript API

## <name="features"></a>Features

In the map view, users can scroll through a slider of dates which changes the map to display the protests per day. When a marker is clicked, there will be a link to the associated URL.

![map](/static/gif/map.gif)

In the analysis view, users can select a month and day to display charts for further analysis.

![chart](/static/gif/chart.gif)

API allows for ease of access to data in various ways such as curling. 

![api](/static/gif/api.gif)

## <a name="test"></a>Testing Coverage

![test](/static/pic/test.png)

## <a name="run"></a>How to Run

Data back up is not available in repository as the file too big to push. To run on your local machine, running gdelt.py is required before starting server. 

  1. Create a virtual environment 
    ```
    > virtualenv env
    > source env/bin/activate
    ```
  2. Install the dependencies 
    ```
    > pip install -r requirements.txt

    ```
  3. Create a protests database
    ```
    > createdb protests
    
    ```
  4. Run gdelt file (DISCLAIMER: this can take some time)
    ```
    > python gdelt.py
    ``` 
  5. After gdelt.py is complete. In a new Terminal run App
    ```
    > python server.py
    ```
  6. Open your browser and navigate to 
    ```
    http://localhost:5000/
    ```

## <a name="data"></a>Data
Data was downloaded, processed, and stored into a PostgreSQL database from the Global Database of Events, Language, and Tone Project [website](http://data.gdeltproject.org/events/index.html) using the gdelt.py script. 

## <a name="future"></a>Future Development

* Sentiment Analysis using Natural Language Processing for content in associated URL!
* Celery Distributed Task Queue: For real-time processing of protests data!
* More charts!
