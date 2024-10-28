in_stock = {"coffee": 1, "milk": 2, "cream": 3}
def order(*preferences):
    recipes = {
        "Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
        "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
        "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
        "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1}
    }
    result = []
    for drink in preferences:
        ingredients = recipes.get(drink)
        if ingredients:
            can_make = lambda x: in_stock[x] >= ingredients[x]
            if all(can_make(ing) for ing in ingredients):
                for ing in ingredients:
                    in_stock[ing] -= ingredients[ing]
                result.append(drink)
                print(result)
                result = []
                continue
            else:
                break
           
    return "К сожалению, не можем предложить Вам напиток"

in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
in_stock = {"coffee": 2, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
