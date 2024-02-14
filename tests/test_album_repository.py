from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository.all()
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2),
    ]

"""
When we call AlbumRepository.find(id)
We get the specified Album object reflecting the id argument passed in
"""
def test_find_album_id(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album_5 = repository.find(5)
    album_1 = repository.find(1)
    album_9 = repository.find(9)

    assert album_5 == Album(5, "Bossanova", 1990, 1)
    assert album_1 == Album(1, "Doolittle", 1989, 1)
    assert album_9 == Album(9, "Baltimore", 1978, 4)