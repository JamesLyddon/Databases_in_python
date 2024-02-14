from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

# Sequence Diagram
# [MermaidChart: 73fb2cef-af64-47d5-a989-a9aab82f8b01]


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# Retrieve all albums
album_repository = AlbumRepository(connection)
albums = album_repository.all()

def list_all_artists():
    for artist in artists:
        print(artist)

def list_all_albums():
    for album in albums:
        print(album)

def list_album_by_id(id):
    album = album_repository.find(id)
    print(album)

list_album_by_id(2)