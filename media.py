import webbrowser


# Creates the Movie Title, Poster Image and Youtube trailer
# Opens Youtube trailer in a webbrowser
class Movie():
    # Initalize Movie Title, Poster Image and Youtube trailer
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Opens Youtube trailer in a webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
