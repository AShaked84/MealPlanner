#once our meal plan is done we can count the instances of each meal, this way we know how many servings to prepare of each recipe.
#this function recieves the meal plan, then iterates through it to count instances of each recipe. It returns a new dictionary {recipe_id:count}
def mealCounter(meal_plan):
    meal_counts = {}
    
    for day, meals in meal_plan.items():
        for time, recipe in meals.items():
            if recipe in meal_counts:
                meal_counts[recipe] += 1
            else:
                meal_counts[recipe] = 1

    return meal_counts