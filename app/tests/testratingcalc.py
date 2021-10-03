# Use unittest library to create a unit test method to test the calc_avg_rating function created in the ratingscalc module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest
from app.src.Review import Review
from app.src.ratingscalc import calc_avg_rating

class TestRatingcalc(unittest.TestCase):
    def test_is_resturant_unqiue(self):
        input = [ 
            Review('Restaurant a', 'Awesome place to try', 'Recommend', 5.0),
            Review('Restaurant a', 'Awesome place to try', 'Recommend', 4.8),
            Review('Restaurant b', 'Awesome place to try', 'Recommend', 4.5),
            Review('Restaurant b', 'I love this place', 'Recommend', 4.3),
            Review('Restaurant c', 'This place is dirty', 'Do not Recommend', 2.4),
            Review('Restaurant c', 'This place is aweful', 'Do not Recommend', 1.8),
        ]

        expect = {
            'Restaurant a': 4.9,
            'Restaurant b': 4.4,
            'Restaurant c': 2.1
        }


        actual = calc_avg_rating(input)
        self.assertEqual(expect, actual)
        self.assertFalse(len(actual) == 0)
        self.assertIn('Restaurant a', actual.keys())
        self.assertIn('Restaurant b', actual.keys())




    