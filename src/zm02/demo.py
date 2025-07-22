def hello(name:str) -> str:
    return f"Hello, {name}!"





import random

def get_random_movie():
    movies = [
        "The Shawshank Redemption",
        "The Godfather",
        "Forrest Gump",
        "Inception",
        "The Dark Knight",
        "Pulp Fiction",
        "Fight Club",
        "The Matrix",
        "Interstellar",
        "Gladiator",
        "The Silence of the Lambs",
        "Schindler's List",
        "Saving Private Ryan",
        "Titanic",
        "The Green Mile",
        "The Prestige",
        "The Departed",
        "Braveheart",
        "The Wolf of Wall Street",
        "La La Land",
        "Django Unchained",
        "Whiplash",
        "Avengers: Endgame",
        "Avatar",
        "The Revenant",
        "Joker",
        "The Social Network",
        "No Country for Old Men",
        "Mad Max: Fury Road",
        "Everything Everywhere All At Once"
    ]
    return random.choice(movies)
