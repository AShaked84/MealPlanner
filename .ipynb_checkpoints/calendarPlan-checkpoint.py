from datetime import datetime, timedelta, date

def calendarMaker():
    start_date = date.today()

    meal_plan = {}
    
    for i in range(7):
        day = start_date + timedelta(days=i)
    
        meal_plan[day] = {
            "breakfast": None,
            "lunch": None,
            "dinner": None
    }

    return meal_plan

def addMeal(meal_plan, date, meal, recipe_id):
    connection = sqlite3.connect("database/movies.db")
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM RecipeBook WHERE ID = ?", [recipe_id])
    recipe = result.fetchall()
    
    print(recipe[1])
    
    #how many servings do we have of each 
    