from lib.book import Book

"""
Book constructs with an title and author_name
"""
def test_artist_constructs():
    book = Book(1, "Test Title", "Test Author")
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author_name == "Test Author"


"""
We can format books to strings nicely
"""
def test_books_format_nicely():
    book = Book(1, "Test Title", "Test Author")
    assert str(book) == "1 - Test Title - Test Author"

"""
We can compare two identical artists
And have them be equal
"""
def test_books_are_equal():
    book_1 = Book(1, "Test Title", "Test Author")
    book_2 = Book(1, "Test Title", "Test Author")
    assert book_1 == book_2