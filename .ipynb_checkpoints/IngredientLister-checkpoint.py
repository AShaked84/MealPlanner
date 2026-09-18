from fractions import Fraction
from collections import defaultdict, Counter
from recipe_scrapers import scrape_me
import pint
import re
ureg = pint.UnitRegistry()

#scrape recipe from card. Function recieves a url string and returns a json file 
def recipe_scraper(url):
    scraper = scrape_me(url)
    scraper.title()
    scraper.instructions()
    json_data = scraper.to_json()
    return json_data["ingredient_groups"][0]["ingredients"]
    

#function recieves a string, returns a boolean on whether it is a number, includes fractions ("1/4") and decimals ("3.14")
#used to find quantities
def is_number_or_fraction(word):
    try:
        Fraction(word)
        return True
    except ValueError:
        return False

#function recieves a list of ingredients (string), splits it into a dictionary with ingredient(string):PINT Quantity(float, string)
def listCleaner(ingredients):
    ingredientDict = {}
    for item in ingredients:
        item = item.split(" ($")[0]
        item = item.replace("*", "")
        item = re.sub(r"\([^)]*\)", "", item)
        words = item.split()

        unit = "count"
        amount = 1

        for i, word in enumerate(words):
            if is_number_or_fraction(word):
                amount = float(Fraction(word))
            elif word.rstrip(".") in ureg:
                unit = word.rstrip(".")
            else:
                ingredient = " ".join(words[i:])
                break

        ingredientDict[ingredient] = amount * getattr(ureg, unit)

    return ingredientDict

#function recieves a list of ingredients (string), the number of servings the recipe yields as written, and the number of servings the user wants in practice. The list is ran through the listCleaner function to create a dictionary(see above), and the amounts are adjusted to suit user needs.
def groceryList(ingredients, default_servings, required_servings):
    ingredient_dict = listCleaner(ingredients)
    serving_factor = required_servings/default_servings

    scaled_ingredients = {key: value * serving_factor for key, value in ingredient_dict.items()}

    return scaled_ingredients

#function recieves a list of cleaned dictionaries (after listCleaner) and returns a master dictionary of all the ingredients added up. 
#need a solution for similarly worded ingredients (ie lemon vs. fresh lemon) and items "to taste" (ie salt and pepper)
def combineLists(dict_list):
    master_list = Counter()

    for d in dict_list:
        master_list.update(d)

    result = dict(master_list)

    return result