in_stock = {"coffee": 0, "milk": 0, "cream": 0}

recipes = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1}
}

def order(*preferences):
    global in_stock
    has_ingredients = lambda drink: all(in_stock[ingredient] >= amount for ingredient, amount in recipes[drink].items())
    for drink in preferences:
        if drink in recipes and has_ingredients(drink):
            for ingredient, amount in recipes[drink].items():
                in_stock[ingredient] -= amount
            return drink
            continue
        return "К сожалению, не можем предложить Вам напиток"
        continue

in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
