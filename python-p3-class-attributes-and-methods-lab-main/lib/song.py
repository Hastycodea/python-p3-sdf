class Song:

    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.increase_count()
        Song.add_genre_to_genres(self.genre)
        Song.add_artist_to_artists(self.artist)
        Song.genre_count[self.genre] = Song.genres.count(self.genre)
        Song.artist_count[self.artist] = Song.artists.count(self.artist)

    @classmethod
    def increase_count(cls, increment = 1):
        Song.count += increment

    @classmethod
    def add_genre_to_genres(cls, genre):
        Song.genres.append(genre)

    @classmethod
    def add_artist_to_artists(cls, artist):
        Song.artists.append(artist)

