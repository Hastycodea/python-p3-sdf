spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [spicy_food["name"] for spicy_food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        name = spicy_food["name"]
        cuisine = spicy_food["cuisine"]
        heat_level = spicy_food["heat_level"] 

        print(f"{name} ({cuisine}) | Heat Level: U+1F336*{heat_level}")

# print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food = [spicy_food for spicy_food in spicy_foods if spicy_food["cuisine"] == cuisine]
    return spicy_food[0]

print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
