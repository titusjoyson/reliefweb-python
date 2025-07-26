import unittest
from reliefweb.client import ReliefWebClient

class TestReliefWebClient(unittest.TestCase):
    def setUp(self):
        self.client = ReliefWebClient(appname="reliefweb-python-client-GA-runner-test")

    def test_get_reports(self):
        result = self.client.get_reports(limit=1)
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)

    def test_get_jobs(self):
        result = self.client.get_jobs(limit=1)
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)

    def test_get_training(self):
        result = self.client.get_training(limit=1)
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)

    def test_get_disasters(self):
        result = self.client.get_disasters(limit=1)
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)

    def test_get_sources(self):
        result = self.client.get_sources(limit=1)
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)

    def test_get_countries(self):
        result = self.client.get_countries(limit=1)
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)

    def test_get_blog(self):
        result = self.client.get_blog(limit=1)
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)

    def test_get_books(self):
        result = self.client.get_books(limit=1)
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)

    def test_get_references(self):
        result = self.client.get_references(limit=1)
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)

if __name__ == '__main__':
    unittest.main()
