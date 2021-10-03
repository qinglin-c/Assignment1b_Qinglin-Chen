# Create a unit test method to test the calculate_avg_rating function created in the utils module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest
from app.src.utils import calculate_avg_rating

from app.src.Review import Review

class TestUtils(unittest.TestCase):
    def test_calc_avg_valid(self):
        input = [
            Review('Restaurant a', 'Awesome place to try', 'Recommend', 5.0),
            Review('Restaurant a', 'Awesome place to try', 'Recommend', 4.8),
        ]

        actual = calculate_avg_rating(input)
        expect = 4.9
        self.assertEqual(expect, actual)
        self.assertTrue(isinstance(actual, float))
   