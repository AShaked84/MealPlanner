import sqlite3
import json
import pandas as pd

import IngredientLister as IL

#get the meal plan table to initialize the app and turn it into a pandas database
def getMealPlan():
    connection = sqlite3.connect("Database/RecipeBook.db")
    cursor = connection.cursor()
    
    meal_plan = pd.read_sql_query("SELECT * FROM MealPlan", connection)

    return meal_plan

#function will recieve either a link to a recipe or a string with the recipe information [recipe title, servings, ingredients] and add the recipe to the database
def addRecipe(recipe: str | list[str]):
    connection = sqlite3.connect("Database/RecipeBook.db")
    cursor = connection.cursor()

    if isinstance(recipe, str):
        json_data = IL.recipe_scraper(recipe)
        name = json_data['title']
        servings = int(json_data['yields'][0])
        #at some point I should turn this into another database, probably. Keeping it simple for the time being for a proof of concept.
        ingredients = json.dumps(json_data["ingredient_groups"][0]["ingredients"])
        url = json_data['canonical_url']
        data = [name, servings, ingredients, url]

    elif isinstance(recipe, list):
        recipe.append(None)
        data = recipe

    cursor.execute("INSERT INTO 'Recipes' ('RecipeName', 'Servings', 'Ingredients', 'URL') VALUES (?,?,?,?)", data)
    connection.commit()



def listRecipes():
    connection = sqlite3.connect("Database/RecipeBook.db")
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM Recipes")
    recipes = result.fetchall()
    recipe_list = []

    for recipe in recipes:
        #print(str(recipe[0]) + " - ", recipe[1])
        recipe_list.append(str(recipe[0]) + " - " + recipe[1])
    return recipe_list