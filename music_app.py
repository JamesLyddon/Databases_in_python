from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    print("What would you like to do?")
    print("1 - List all albums")
    print("2 - List all artists")
    response = input("selection --> ")

    if response == "1":
        album_repository = AlbumRepository(self._connection)
        albums = album_repository.all()
        for album in albums:
            print(f"* {album.id} - {album.title}")
    elif response == "2":
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()
        for artist in artists:
            print(f"* {artist.id} - {artist.name}")
    else:
       print("Invalid selection. Must choose either 1 or 2.")
       app = Application()
       app.run()

if __name__ == '__main__':
    app = Application()
    app.run()