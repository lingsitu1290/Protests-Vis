import server
import unittest

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


if __name__ == '__main__':
    # If script is called, run our tests
    unittest.main()