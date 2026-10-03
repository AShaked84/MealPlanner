import json
import DatabaseManager as DM
import IngredientManager as IM

from fractions import Fraction
import pint
import re
ureg = pint.UnitRegistry()
from datetime import date
import datetime

#once our meal plan is done we can count the instances of each meal, this way we know how many servings to prepare of each recipe.
#this function recieves the meal plan for the chosen dates ahead, then iterates through it to count instances of each recipe. 
# It returns a new dictionary {recipe_id:count}
def mealCounter(dates):
    meal_counts = {}
    rows = DM.daysAhead(dates)

    #row[0] - date row[1] - recipe_id row[2] - servings
    for row in rows:
        if row[1] in meal_counts:
            meal_counts[row[1]] += row[2]
        else:
            meal_counts[row[1]] = row[2]
    return meal_counts

"""
#function recieves a dictionary of {db_id:amount of servings} and returns a dictionary of {amount:ingredient}
def shoppingList(meal_counts):
    ingredient_list = []
    for db_id, servings in meal_counts.items():
        original_servings = DM.recipeServings(db_id)
        recipe_scalar = servings / original_servings[0]
        ingredients = DM.recipeIngredients(db_id)
        print(ingredients[0])
        ingredient_list.extend(json.loads(ingredients[0]))

       # shopping_list = IL.groceryList(ingredient_list, DM.recipeServings(db_id)[0], servings)

    
   # return shopping_list
"""