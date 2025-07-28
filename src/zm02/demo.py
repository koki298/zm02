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


def caesar_code(text):
    result = ""
    for ch in text:
        code = ord(ch)
        if "A" <= ch <= "Z":
            result += chr((code - ord("A") + 3) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            result += chr((code - ord("a") + 3) % 26 + ord("a"))
        elif "0" <= ch <= "9":
            result += str(9 - int(ch))
        else:
            result += ch
    return result


def decode_caesar(text):
    result = ""
    for ch in text:
        code = ord(ch)
        if "A" <= ch <= "Z":
            result += chr((code - ord("A") - 3) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            result += chr((code - ord("a") - 3) % 26 + ord("a"))
        elif "0" <= ch <= "9":
            result += str(9 - int(ch))
        else:
            result += ch
    return result

