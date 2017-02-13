import webbrowser
class Movie():
    """this class provides a way to store movie related info.."""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self, movie_title, movie_storyline,poster_image,trailer_youtube):
#initialize space in memory for remembering details like title, storyline, etc...
#self is the object being created
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
         webbrowser.open(self.trailer_youtube_url)
