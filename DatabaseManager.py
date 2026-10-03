import sqlite3
import json
import pandas as pd
from pathlib import Path

import IngredientManager as IM

BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR / "Database" / "RecipeBook.db"
#pulls up the list of recipes for the days betweeen the two in the list "dates"
def daysAhead(dates):
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()

    cursor.execute("SELECT date, recipe_id, servings FROM MealPlan WHERE date BETWEEN ? AND ?", dates)
    rows = cursor.fetchall()
    connection.close()
    return rows

"""def change_servings(meal_id, delta):
    with sqlite3.connect(str(db_path), timeout=10) as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE MealPlan SET servings = servings + ? WHERE id = ?", [delta, meal_id])
        connection.commit()
        connection.close()"""

def get_servings(meal_id):
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()

    cursor.execute("SELECT servings FROM MealPlan WHERE id=?", (meal_id,))
    servings = cursor.fetchone()
    connection.close()
    return servings

def change_servings(meal_id, delta):

    try:
        with sqlite3.connect(str(db_path), timeout=10) as connection:

            connection.execute(
                "UPDATE MealPlan SET servings = servings + ? WHERE id = ?",
                (delta, meal_id)
            )

    except sqlite3.OperationalError as e:
        raise

#get the meal plan table to initialize the app and turn it into a pandas database
def getMealPlan():
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()
    
    meal_plan = pd.read_sql_query("SELECT * FROM MealPlan", connection)

    connection.close
    return meal_plan

def removeMeal(db_id):
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM MealPlan WHERE id=?", [db_id])
    connection.commit()
    connection.close()

def removeRecipe(db_id):
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM Recipes WHERE id=?", [db_id])
    connection.commit()
    connection.close()

def todaysMeals(date):
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM MealPlan WHERE date = ?", [date])

    rows = cursor.fetchall()
    connection.close()
    return rows


def idRecipe(db_id):
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()

    cursor.execute("SELECT RecipeName FROM Recipes WHERE ID = ?", [db_id])

    recipeTitle = cursor.fetchall()
    connection.close()
    return recipeTitle[0][0]

def recipeIngredients(db_id):
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()
    
    cursor.execute("SELECT Ingredients FROM Recipes WHERE ID = ?", [db_id])
    
    ingredients = cursor.fetchone()
    connection.close()
    return ingredients# json.loads(ingredients)

def recipeServings(db_id):
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()
    
    cursor.execute("SELECT Servings FROM Recipes WHERE ID = ?", [db_id])
    
    servings = cursor.fetchone()
    connection.close()
    return servings

#print(recipeServings(2)[0])

#add new meal to plan
def addMeal(date, meal, recipe_id):
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()

    data = [date, meal, recipe_id]

    cursor.execute("INSERT INTO 'MealPlan' ('date', 'meal', 'recipe_id') VALUES (?,?,?)", data)
    connection.commit()
    connection.close()
    
#function will recieve either a link to a recipe or a string with the recipe information [recipe title, servings, ingredients] and add the recipe to the database
def addRecipe(recipe: str | list[str]):
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()

    if isinstance(recipe, str):
        json_data = IM.recipe_scraper(recipe)
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
    connection.close()

"""
def loadRecipes(self):
    connection = sqlite3.connect("Database/RecipeBook.db")
    cursor = connection.cursor()

    cursor.execute("SELECT ID, RecipeName FROM Recipes")
    rows = cursor.fetchall()

    return rows"""

def listRecipes():
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM Recipes")
    recipes = result.fetchall()
    recipe_list = {}

    for recipe in recipes:
        #return dictionary {db_id:title}
        recipe_list[recipe[0]] = recipe[1]

    connection.close()
    return recipe_list