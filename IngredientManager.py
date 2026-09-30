from fractions import Fraction
import pint
import re
import json
ureg = pint.UnitRegistry()
from recipe_scrapers import scrape_me

import DatabaseManager as DM

#scrape recipe from card. Function recieves a url string and returns a json file 
def recipe_scraper(url):
    scraper = scrape_me(url)
    scraper.title()
    scraper.instructions()
    json_data = scraper.to_json()
    return json_data

def is_number_or_fraction(word):
    try:
        Fraction(word)
        return True
    except ValueError:
        return False

#get a list of strings
#iterate through the list.
#for each string break it up by words, clean them up, and divide into ingredient, number amount.
#return list of lists (ingredient_string, PINT quantity_float]
def list_cleaner(ingredients, recipe_scalar):
    ingredient_list = []

    for item in ingredients:
        #clean up the string
        item = item.strip()
        item = item.split(" ($")[0]
        item = item.split(" $")[0]
        item = item.replace("*", "")
        item = re.sub(r"\([^)]*\)", "", item)

        #divide string into words
        words = item.split()

        #default units
        unit = "count"
        amount = 1

        for i, word in enumerate(words):
            if is_number_or_fraction(word):
                amount = float(Fraction(word))
            else:
                clean_word = word.rstrip(".")
                try:
                    ureg(clean_word)
                    unit = clean_word

                except Exception:
                    ingredient = " ".join(words[i:])
                    break

        ingredient_list.append([ingredient, (amount * recipe_scalar) * getattr(ureg, unit)])

    return ingredient_list

#ing1 = json.loads(DM.recipeIngredients(5)[0])
#ing2 = json.loads(DM.recipeIngredients(6)[0])

"""
#recieves a list of strings and a float scalar
#passes the list of strings through the list clearner function
#iterates through the list of lists and returns a dictionary shopping list
def ingredient_scalar(ingredients, recipe_scalar):
    ingredient_list = list_cleaner(ingredients, recipe_scalar)
    for ingredient in ingredient_list:
        ingredient[1] * recipe_scalar

    return ingredient_list"""

#recieves a dictionary of meal counts {db_id:number of servings}
#iterates through them, find the recipe scalar by dividing the servings needed by the original size
#passes each db_id through the database to get the json of the ingredients and extracts a list
#passes the list and the recipe scalar through the ingredient scalar function
#updates the grocery list dictionary with new ingredients and updated amounts
def grocery_lister(meal_counts):
    grocery_list = {}
    for db_id, servings in meal_counts.items():
        original_servings = DM.recipeServings(db_id)[0]
        recipe_scalar = servings / original_servings
        ingredients = json.loads(DM.recipeIngredients(db_id)[0])

        scaled_ingredients = list_cleaner(ingredients, recipe_scalar)
        for ingredient in scaled_ingredients:
            if ingredient[0] in grocery_list:
                grocery_list[ingredient[0]] += ingredient[1]
            else:
                grocery_list[ingredient[0]] = ingredient[1]

    return grocery_list