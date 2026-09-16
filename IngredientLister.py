from fractions import Fraction

units = [
    "lb", "Tbsp", "tsp", "cloves",
    "cup", "cups", "oz", "ounce", "ounces",
    "g", "kg", "ml", "l"
]

def is_number_or_fraction(word):
    try:
        Fraction(word)
        return True
    except ValueError:
        return False

#function recieves a list of ingredients (string), splits it into a dictionary with ingredient(string):amount(string)
def listCleaner(ingredients):
    ingredientDict = {}
    for item in ingredients:
        #remove extra characters and split into words
        item = item.split(" ($")[0]
        item = item.replace("*", "")
        words = item.split()

        #divide based on where the unit is
        for i, word in enumerate(words):
            if is_number_or_fraction(word):
                amount = float(Fraction(word))
            clean_word = word.rstrip(".")
            if clean_word in units:
                unit = words[i]
                ingredient = " ".join(words[i + 1:])
                break

        ingredientDict[ingredient] = dict(amount=amount, unit=unit)

    return ingredientDict