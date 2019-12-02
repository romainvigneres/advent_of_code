from common import input_list_integer


def mass_to_fuel(mass):
    return mass // 3 - 2


def part_one(list_integer):
    return sum([mass_to_fuel(x) for x in list_integer])


def test_one():
    assert mass_to_fuel(12) == 2
    assert mass_to_fuel(14) == 2
    assert mass_to_fuel(1969) == 654
    assert mass_to_fuel(100756) == 33583


def mass_to_fuel_full(mass):
    result = 0
    fuel_mass = mass_to_fuel(mass)
    while fuel_mass > 0:
        result += fuel_mass
        fuel_mass = mass_to_fuel(fuel_mass)
    return result


def part_two(list_integer):
    return sum([mass_to_fuel_full(x) for x in list_integer])


def test_two():
    assert mass_to_fuel_full(14) == 2
    assert mass_to_fuel_full(1969) == 966
    assert mass_to_fuel_full(100756) == 50346


def get_result():
    inp = input_list_integer("year2019/day01/input.txt")
    # part one
    test_one()
    print("Part one", part_one(inp))
    # part two
    test_two()
    print("Part two", part_two(inp))
