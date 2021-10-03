# Create a function called: calc_avg_rating
# Parameters: the function should receive 1 parameter: a list of review objects
#             Remember a list can contain duplicates, so you can expect multiple reviews for the same restaurant
# Returns: the function should return a dictionary with restaurant name as key and average rating as value
#
#
# If the list of reviews is empty, return an empty dictionary
# Make sure that you add type hints to the function paramter and return value

import typing as t
from app.src.Review import Review
from app.src.utils import calculate_avg_rating

def calc_avg_rating(reviews: t.List[Review]) -> dict[str, float]:
    if len(reviews) == 0:
        return {}

    # group the list by restuarent name
    restaurant_name: dict[str, list[Review]] = {}
    for review in reviews:
        restaurant: str = review.restaurant
        #if restaurant in restaurant_name.key():
        if restaurant in restaurant_name:
            restaurant_name.get(restaurant).append(review)
        else:
            restaurant_name[restaurant] = [review]
            
    restaurant_avg_rating: dict[str, float] = {}
    for restaurant, reviews in restaurant_name.items():
        avg_rating = calculate_avg_rating(reviews)
        restaurant_avg_rating[restaurant] = avg_rating
    return restaurant_avg_rating
    """""
    for restaurant, rating in restaurant_name.items():
        avg_rating = calculate_avg_rating(rating)
        restaurant_avg_rating[restaurant] = avg_rating
    return restaurant_avg_rating
    """

