from fractions import Fraction

units = [
    "lb", "lb.", "Tbsp", "tsp", "cloves",
    "cup", "cups", "oz", "ounce", "ounces",
    "g", "kg", "ml", "l"
]

#function recieves a string, returns a boolean on whether it is a number, includes fractions ("1/4") and decimals ("3.14")
def is_number_or_fraction(word):
    try:
        Fraction(word)
        return True
    except ValueError:
        return False

#function recieves a list of ingredients (string), splits it into a dictionary with ingredient(string):{amount: float, unit: string}
def listCleaner(ingredients):
    ingredientDict = {}
    for item in ingredients:
        #remove extra characters and split into words
        item = item.split(" ($")[0]
        item = item.replace("*", "")
        words = item.split()

        unit = ""
        amount = 1

        #divide based on where the number is
        #default empty string for unit in case ingredient doesn't have one
        for i, word in enumerate(words):
            if is_number_or_fraction(word):
                amount = float(Fraction(word))
            elif word.rstrip(".") in units:
                unit = word
            else:
                ingredient = " ".join(words[i:])
                break

        ingredientDict[ingredient] = dict(amount=amount, unit=unit)

    return ingredientDict

def groceryList(ingredients, default_servings, required_servings):
    ingredient_dict = listCleaner(ingredients)
    serving_factor = required_servings/default_servings

    for ingredient in ingredient_dict.values():
        ingredient["amount"] = ingredient["amount"] * serving_factor

    return ingredient_dict