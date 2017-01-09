import fresh_tomatoes
import media

empire_strikes_back = media.Movie(
        "Star Wars",
        "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",  # noqa
        "https://youtu.be/xESiohGGP7g")

the_godfather = media.Movie(
        "The_GodFather",
        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
        "https://youtu.be/YYKxj8qiLTg")

the_five_heartbeats = media.Movie(
        "The Five Heartbeats",
        "https://upload.wikimedia.org/wikipedia/en/7/7f/The_Five_Heartbeats.jpg",  # noqa
        "https://www.youtube.com/watch?v=IKhZXOU5SCg")

movies = [empire_strikes_back, the_godfather, the_five_heartbeats]

# Calls the fresh fresh_tomatoes script
# Opens page in a webbrowser by calling the movies class
fresh_tomatoes.open_movies_page(movies)
