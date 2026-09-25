import sqlite3
import json

import IngredientLister as IL

connection = sqlite3.connect("Database/RecipeBook.db")
cursor = connection.cursor()

def addRecipe(url):
    json_data = IL.recipe_scraper(url)
    name = json_data['title']
    servings = int(json_data['yields'][0])
    #at some point I should turn this into another database, probably. Keeping it simple for the time being for a proof of concept.
    ingredients = json.dumps(json_data["ingredient_groups"][0]["ingredients"])
    url = json_data['canonical_url']

    data = [name, servings, ingredients, url]
    cursor.execute("INSERT INTO 'Recipes' ('RecipeName', 'Servings', 'Ingredients', 'URL') VALUES (?,?,?,?)", data)
    connection.commit()

def listRecipes():
    result = cursor.execute("SELECT * FROM Recipes")
    recipes = result.fetchall()

    for recipe in recipes:
        print(str(recipe[0]) + " - ", recipe[1])
    return recipes