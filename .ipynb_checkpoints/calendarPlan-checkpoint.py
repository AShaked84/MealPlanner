from datetime import datetime, timedelta, date

#creates a calendar for this week, starting sunday, with a space to add a recipe for each meal
#recipe saved as id number
#output: {datetime.date:{string:int, string:int, string:int}, ...}
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

#function recieves meal_plan created by calendarMaker, a datetime date (eg date(year, month,  date), the meal to fill out as a string, and the id for the chosen recipe. 
#the chosen recipe is saved to the chosen meal as its id number
def addMeal(meal_plan, date, meal, recipe_id):
    connection = sqlite3.connect("database/RecipeBook.db")
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM Recipes WHERE ID = ?", [recipe_id])
    recipe = result.fetchall()
    
    meal_plan[date][meal] = recipe[0]
    
    #how many servings do we have of each 
    