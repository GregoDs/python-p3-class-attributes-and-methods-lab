class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_genres()
        self.add_to_artists()
        Song.add_song_to_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

    @classmethod
    def add_to_genre_count(cls):
        genre_count = {}
        for song in cls.genres:
            if song in genre_count:
                genre_count[song] += 1
            else:
                genre_count[song] = 1
        cls.genre_count = genre_count

    @classmethod
    def add_to_artist_count(cls):
        artist_count = {}
        for song in cls.artists:
            if song in artist_count:
                artist_count[song] += 1
            else:
                artist_count[song] = 1
        cls.artist_count = artist_count


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
ninety_nine_problems.name
# "99 Problems"

ninety_nine_problems.artist
# "Jay-Z"

ninety_nine_problems.genre
# "Rap"

print("Count of songs:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)
