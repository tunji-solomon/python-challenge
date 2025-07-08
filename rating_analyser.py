
#Question: Movie Ratings Analyzer
# Write a Python function called analyze_ratings that:

# Accepts a list of dictionaries. Each dictionary represents a movie and has:

# 'title': the movie name

# 'ratings': a list of integers representing user ratings (from 1 to 5)

# The function should return a new dictionary mapping each movie title to its average rating, rounded to 2 decimal places.

# If a movie has no ratings, its average should be 0.



def rating_analyser(movie_collection: list[dict]) -> dict:
    new_dictionary = {}

    for movie in movie_collection:
        new_key = movie.get("title")
        ratings = movie.get("ratings", [])
        total_rating = 0
        average_rating = 0
        if len(ratings) == 0:
            average_rating = 0
        else:
            for rating in ratings: 
                total_rating += int(rating)
            average_rating = round(total_rating / len(ratings), 2)
        new_dictionary[new_key] = average_rating
    
    return new_dictionary

movies = [
    {"title": "Inception", "ratings": [5, 4, 5, 5, 4]},
    {"title": "Titanic", "ratings": [4, 5, 4]},
    {"title": "Avatar", "ratings": []}
]
print(rating_analyser(movies))
        
            
                
                    