import server
import unittest

class MyAppIntegrationTestCase(unittest.TestCase):
    """ Testing Flask Server. """

    def test_index(self):
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn('<div id="map-canvas"/> </div>', result.data)

if __name__ == '__main__':
    # If script is called, run our tests
    unittest.main()