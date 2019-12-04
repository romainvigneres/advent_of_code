def check(pwd):
    result = False
    pwd_str = str(pwd)
    previous_digit = "00"
    for digit in pwd_str:
        if int(previous_digit) > int(digit):
            return False
        elif previous_digit == digit:
            result = True
        previous_digit = digit
    return result


def part_one(inp):
    limits = [int(x) for x in inp.split("-")]
    return sum([1 for x in range(limits[0], limits[1] + 1) if check(x)])


def test_one():
    assert check(111111) == True
    assert check(223450) == False
    assert check(123789) == False


def check_two(pwd):
    result = False
    pwd_str = list(str(pwd))
    x = 1
    previous_digit = pwd_str[0]
    while x < 6:
        digit = pwd_str[x]
        if int(previous_digit) > int(digit):
            return False
        elif previous_digit == digit:
            if x == 5:
                if pwd_str[3] != digit:
                    result = True
            elif x == 1:
                if pwd_str[x + 1] != digit:
                    result = True
            elif pwd_str[x - 2] != digit and pwd_str[x + 1] != digit:
                result = True
        previous_digit = digit
        x += 1
    return result


def part_two(inp):
    limits = [int(x) for x in inp.split("-")]
    return sum([1 for x in range(limits[0], limits[1] + 1) if check_two(x)])


def test_two():
    assert check_two(112233) == True
    assert check_two(123444) == False
    assert check_two(111122) == True


def get_result():
    input_string = "272091-815432"
    test_one()
    print("Part one", part_one(input_string))
    test_two()
    print("Part two", part_two(input_string))
