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

def removeMeal(db_id):
    connection = sqlite3.connect("Database/RecipeBook.db")
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM MealPlan WHERE id=?", [db_id])
    connection.commit()
    connection.close()

def todaysMeals(date):
    connection = sqlite3.connect("Database/RecipeBook.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM MealPlan WHERE date = ?", [date])

    rows = cursor.fetchall()
    connection.close()
    return rows

def idRecipe(db_id):
    connection = sqlite3.connect("Database/RecipeBook.db")
    cursor = connection.cursor()

    cursor.execute("SELECT RecipeName FROM Recipes WHERE ID = ?", [db_id])

    recipeTitle = cursor.fetchall()
    connection.close()
    return recipeTitle
    
#add new meal to plan
def addMeal(date, meal, recipe_id):
    connection = sqlite3.connect("Database/RecipeBook.db")
    cursor = connection.cursor()

    data = [date, meal, recipe_id]

    cursor.execute("INSERT INTO 'MealPlan' ('date', 'meal', 'recipe_id') VALUES (?,?,?)", data)
    connection.commit()
    connection.close()
    
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

"""
def loadRecipes(self):
    connection = sqlite3.connect("Database/RecipeBook.db")
    cursor = connection.cursor()

    cursor.execute("SELECT ID, RecipeName FROM Recipes")
    rows = cursor.fetchall()

    return rows"""

def listRecipes():
    connection = sqlite3.connect("Database/RecipeBook.db")
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM Recipes")
    recipes = result.fetchall()
    recipe_list = {}

    for recipe in recipes:
        #print(str(recipe[0]) + " - ", recipe[1])
        recipe_list[recipe[0]] = recipe[1]

    connection.close()
    return recipe_list