from fractions import Fraction
import pint
import re
import json
ureg = pint.UnitRegistry()
from recipe_scrapers import scrape_me
from tokenize import TokenError

import DatabaseManager as DM

unit_aliases = {
    "tblsp": "tablespoon",
    "tbsp": "tablespoon",
    "Tblsp": "tablespoon",
    "Tbsp": "tablespoon"
}
ureg.define("count = []")

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

        #unicode fractions are annoying 
        unicode_fractions = {"½": "1/2",
    "⅓": "1/3", "⅔": "2/3", "¼": "1/4", "¾": "3/4", "⅕": "1/5", "⅖": "2/5", "⅗": "3/5", "⅘": "4/5", "⅙": "1/6", "⅚": "5/6", "⅛": "1/8", "⅜": "3/8", "⅝": "5/8", "⅞": "7/8"}

        for fraction, replacement in unicode_fractions.items():
            item = item.replace(fraction, replacement)

        item = re.sub(r'(\d+)\s+(\d+/\d+)',lambda m: str(Fraction(m.group(1)) + Fraction(m.group(2))), item)
        item = re.sub(r'(\d)([a-zA-Z]+)', r'\1 \2', item)

        #divide string into words
        words = item.split()

        #default units
        unit = "count"
        amount = 1
        ingredient = ""

        for i, word in enumerate(words):
            if not word.strip():
                continue

            if is_number_or_fraction(word):
                amount = float(Fraction(word))
            else:
                clean_word = word.rstrip(".")
                clean_word = unit_aliases.get(clean_word.lower(), clean_word)

                is_valid_unit = False

                if clean_word:
                    try:
                        ureg(clean_word)
                        is_valid_unit = True
                    except (Exception, TokenError):
                        pass

                if is_valid_unit:
                    unit = clean_word
                else:
                    ingredient = " ".join(words[i:])
                    break
                """try:
                    ureg(clean_word)
                    unit = clean_word

                except Exception:
                    ingredient = " ".join(words[i:])
                    break"""

        if not ingredient and words:
            ingredient = " ".join(words)

        if unit == "count":
            unit_obj = ureg.count
        elif unit and hasattr(ureg, unit):
            unit_obj = getattr(ureg, unit)
        else:
            unit_obj = ureg.count

        ingredient_list.append([ingredient, (amount * recipe_scalar) * unit_obj])

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
        if not original_servings:
            original_servings = 1
        recipe_scalar = int(servings) / original_servings
        ingredients = json.loads(DM.recipeIngredients(db_id)[0])

        scaled_ingredients = list_cleaner(ingredients, recipe_scalar)
        for ingredient in scaled_ingredients:
            if ingredient[0] in grocery_list:
                grocery_list[ingredient[0]] += ingredient[1]
            else:
                grocery_list[ingredient[0]] = ingredient[1]

    return grocery_list