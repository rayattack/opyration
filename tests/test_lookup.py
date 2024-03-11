from unittest import TestCase

from opyration.results import Lookup, Results


DATA = {
    'id': 1,
    'username': 'test',
    'works': True,
    'address': {
        'street': '123 Main St',
        'number': 123,
        'city': 'New York',
        'state': 'NY'
    }
}


class ResultsTest(TestCase):
    def setUp(self):
        self.results = Results([DATA])
    
    def tearDown(self):
        pass

    def test_data(self):
        self.assertEqual(self.results.data(), [DATA])
    
    def test_next(self):
        self.assertEqual(self.results.next(), DATA)
    
    def test_pop(self):
        self.assertEqual(self.results.pop(), DATA)
        self.assertEqual(self.results.pop(), None)
    
    def test_reset(self):
        self.results.reset()
        self.assertEqual(self.results.next(), DATA)
