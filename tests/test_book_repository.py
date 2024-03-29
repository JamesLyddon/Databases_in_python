from lib.book_repository import BookRepository
from lib.book import Book

"""
When we call BookRepository.all()
We get a list of Book objects reflecting the seed data.
"""

def test_get_all_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)

    books = repo.all()

    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]

# """
# When we call RecipeRepository.find(id)
# We get the Recipe object with that id
# """

# def test_find_by_id(db_connection):
#     db_connection.seed("seeds/recipes_seed.sql")
#     repo = RecipeRepository(db_connection)

#     recipe = repo.find(2)
#     assert recipe == Recipe(2, 'Sandwich', 2, 3)
