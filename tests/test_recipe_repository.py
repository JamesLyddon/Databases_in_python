from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository.all()
We get a list of Recipe objects reflecting the seed data.
"""

def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipes_seed.sql")
    repo = RecipeRepository(db_connection)

    recipes = repo.all()

    assert recipes == [
        Recipe(1, 'Pasta', 10, 4),
        Recipe(2, 'Sandwich', 2, 3),
        Recipe(3, 'Soup', 15, 2)
    ]