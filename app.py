from lib.database_connection import DatabaseConnection
# from lib.artist_repository import ArtistRepository
# from lib.album_repository import AlbumRepository
# from lib.recipe_repository import RecipeRepository
from lib.user import User
from lib.post import Post
from lib.user_repository import UserRepository
from lib.post_repository import PostRepository


# Sequence Diagram
# [MermaidChart: 73fb2cef-af64-47d5-a989-a9aab82f8b01]


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
# connection.seed("seeds/music_library.sql")
# connection.seed("seeds/recipes_seed.sql")
connection.seed("seeds/social_tables.sql")

# Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# Retrieve all albums
# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# Retrieve all recipes
# recipe_repository = RecipeRepository(connection)
# recipes = recipe_repository.all()

# Retrieve all Users
user_repository = UserRepository(connection)
users = user_repository.all()

# Retrieve all Posts
post_repository = PostRepository(connection)
posts = post_repository.all()

# def list_all_artists():
#     for artist in artists:
#         print(artist)

# def list_all_albums():
#     for album in albums:
#         print(album)

# def list_album_by_id(id):
#     album = album_repository.find(id)
#     print(album)

# def list_all_recipes():
#     for recipe in recipes:
#         print(recipe)

def list_all_users():
    for user in users:
        print(user)

def get_user_by_id(id):
    user = user_repository.find(id)
    print(user)

def list_all_posts():
    for post in posts:
        print(post)

def get_post_by_id(id):
    post = post_repository.find(id)
    print(post)

# list_all_users()
# list_all_posts()
# get_user_by_id(2)
# get_post_by_id(3)