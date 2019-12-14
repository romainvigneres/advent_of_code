from common import input_list_string


class Recipe():
    def __init__(self, quantity, ingredients, basic):
        self.quantity = quantity
        self.ingredients = ingredients
        self.basic = basic


def get_recipe_book(inp_list):
    recipe_book = dict()
    for line in inp_list:
        rec = line.split(" => ")
        ings = rec[0].split(", ")
        ing_dict = dict()
        bas = False
        for ing in ings:
            ing_quant, ing_name = ing.split(" ")
            ing_dict[ing_name] = int(ing_quant)
            if ing_name == "ORE":
                bas = True
        rec_quant, rec_name = rec[1].split(" ")
        recipe_book[rec_name] = Recipe(int(rec_quant), ing_dict, bas)
    return recipe_book


def get_basic_ingredients(recipe, quant, book, ing_list=None):
    if ing_list is None:
        ing_list = dict()
    rec = book[recipe]
    if rec.basic:
        if recipe in ing_list:
            ing_list[recipe] += quant
        else:
            ing_list[recipe] = quant
        return ing_list
    for k, v in rec.ingredients.items():
        get_basic_ingredients(k, quant * v, book, ing_list)
    return ing_list


def part_one(inp_list):
    recipes = get_recipe_book(inp_list)
    shopping_list = get_basic_ingredients("FUEL", 1, recipes)
    ore_cost = 0
    for k, v in shopping_list.items():
        r = recipes[k]
        bulk = (v // r.quantity) + (v % r.quantity > 0)
        ore_cost += bulk * r.ingredients["ORE"]
    return ore_cost


def test_one():
    input_test = [
        "10 ORE => 10 A",
        "1 ORE => 1 B",
        "7 A, 1 B => 1 C",
        "7 A, 1 C => 1 D",
        "7 A, 1 D => 1 E",
        "7 A, 1 E => 1 FUEL"
    ]
    assert part_one(input_test) == 31
    input_test = [
        "9 ORE => 2 A",
        "8 ORE => 3 B",
        "7 ORE => 5 C",
        "3 A, 4 B => 1 AB",
        "5 B, 7 C => 1 BC",
        "4 C, 1 A => 1 CA",
        "2 AB, 3 BC, 4 CA => 1 FUEL"
    ]
    assert part_one(input_test) == 165
    input_test = [
        "157 ORE => 5 NZVS",
        "165 ORE => 6 DCFZ",
        "44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL",
        "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ",
        "179 ORE => 7 PSHF",
        "177 ORE => 5 HKGWZ",
        "7 DCFZ, 7 PSHF => 2 XJWVT",
        "165 ORE => 2 GPVTF",
        "3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"
    ]
    assert part_one(input_test) == 13312


def get_result():
    inp = input_list_string("2019", "14")
    test_one()
    print("Part one", part_one(inp))
