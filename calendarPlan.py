from datetime import datetime, timedelta, date
import numpy as np
import pandas as pd

#add new meal component
def addMeal(meal_plan, date, meal, recipe_id):
    meal_plan = pd.concat([meal_plan, pd.DataFrame([{"date" : date, "meal" : meal, "recipe_id" : recipe_id}])], ignore_index = True)
    return meal_plan