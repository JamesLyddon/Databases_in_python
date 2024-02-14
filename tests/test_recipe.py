from lib.recipe import Recipe

"""
Recipe constructs an instance from the argument provided
"""

def test_initialisation():
    recipe = Recipe(1, 'Pasta', 15, 3)
    assert recipe.id == 1
    assert recipe.name == 'Pasta'
    assert recipe.avg_cooking_time == 15
    assert recipe.rating == 3

"""
Recipe prints out in our predefined format
"""

def test_print_recipe():
    recipe = Recipe(1, 'Pasta', 15, 3)
    assert str(recipe) == "Recipe(1, Pasta, 15, 3)"

"""
Test comparison implementation
"""

def test_recipes_are_equal():
    recipe_1 = Recipe(1, 'Pasta', 15, 3)
    recipe_2 = Recipe(1, 'Pasta', 15, 3)
    assert recipe_1 == recipe_2