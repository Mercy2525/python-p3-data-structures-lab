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
    selected=list() 
    for food in spicy_foods:
        selected.append(food['name'])
    return selected    

def get_spiciest_foods(spicy_foods):
    heat_levels=[food for food in spicy_foods if food['heat_level']>5]
    return heat_levels

    
def print_spicy_foods(spicy_foods):
    good_food=list()
    for food in spicy_foods:
        heat= "🌶" * food["heat_level"]
        my_food=(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')
        good_food.append(my_food)
    return good_food




def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    choice_food=[ food for food in spicy_foods if food["cuisine"]==cuisine]
    print(choice_food)
    return choice_food
get_spicy_food_by_cuisine(spicy_foods,'Thai')

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
