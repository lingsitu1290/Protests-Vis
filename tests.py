from unittest import TestCase
from model import Event, connect_to_db, db
from server import app
import server
import json

import gdelt
import unittest
import doctest

class GdeltTestCase(unittest.TestCase):

    def test_get_URLs(self):
        assert gdelt.get_URLs()[-5:-1] == ['1983.zip', '1982.zip', '1981.zip', '1980.zip']

    def test_process_URL(self):
        self.assertEqual(gdelt.process_URL('20160818.export.CSV.zip'), 'http://data.gdeltproject.org/events/20160818.export.CSV.zip')

    def test_get_URLs_len(self):
        self.assertEqual(len(gdelt.get_URLs()[-6:-1]), 5)

# Runs docts and file-based doctests
def load_tests(loader, tests, ignore):
    """Also run our doctests and file-based doctests.

    This function name, ``load_tests``, is required.
    """

    tests.addTests(doctest.DocTestSuite(gdelt))
    tests.addTests(doctest.DocFileSuite("gdeltdoctests.txt"))
    return tests


# Flask Testing
class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app)

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()

    def test_find_event(self):
        """Can we find an event in the database?"""

        event1 = Event.query.filter(Event.event_id == 253461643).one()
        self.assertEqual(event1.full_location, "Kathmandu, Bagmati, Nepal")


# Server tests

app.config['TESTING'] = True

connect_to_db(app)

class MyAppIntegrationTestCase(unittest.TestCase):
    """ Testing Flask Server. """

    def test_index(self):
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn('<div id="map-canvas"/> </div>', result.data)
        self.assertEqual(result.status_code, 200)

    def test_analyze(self):
        client = server.app.test_client()
        result = client.get('/analyze')
        self.assertIn('<canvas id="barChart"></canvas>', result.data)
        self.assertIn('<canvas id="donutChart"></canvas>', result.data)
        self.assertEqual(result.status_code, 200)

    # Testing json responses
    def test_events_json(self):
        client = server.app.test_client()
        result = client.get('/events/20160811.json')
        # Turn result.data(string) into a dictionary
        data = json.loads(result.data)
        # Assert that this event id is a key in the dictionary
        self.assertIn('568274302', data)
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    import unittest

    unittest.main()
