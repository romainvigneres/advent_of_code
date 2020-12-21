from common import input_list_string

fields = set([
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid" optional
])
hexa = "0123456789abcdef"
lst_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def pass_valid(lst_f):
    if len(fields - set(lst_f)) == 0:
        return True
    return False


def part_one(inp_lst):
    valid = 0
    f_pass = []
    for line in inp_lst:
        if line == "":
            if f_pass:
                if pass_valid(f_pass):
                    valid += 1
            f_pass = []
            continue
        sl = line.split(" ")
        for bit in sl:
            f_pass.append(bit.split(":")[0])
    return valid


def pass_valid_2(dict_f):
    if not pass_valid([*dict_f]):
        return False
    
    byr = int(dict_f["byr"])
    if  byr < 1920 or byr > 2002:
        return False
    
    iyr = int(dict_f["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False
    
    eyr = int(dict_f["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False
    
    hgt = dict_f["hgt"]
    type_hgt = hgt[-2:]
    h = int(hgt[:-2])
    if type_hgt == "cm":
        if h < 150 or h > 193:
            return False
    elif type_hgt == "in":
        if h < 59 or h > 76:
            return False
    else:
        return False

    hcl = dict_f["hcl"]
    if hcl[0] != "#":
        return False
    for c in hcl[1:]:
        if c not in hexa:
            return False

    if dict_f["ecl"] not in lst_ecl:
        return False
    
    pid = dict_f["pid"]
    if len(pid) != 9:
        return False
    for c in pid:
        if not c.isdigit():
            return False
    return True


def part_two(inp_lst):
    valid = 0
    f_pass = dict()
    for line in inp_lst:
        if line == "":
            if f_pass:
                if pass_valid_2(f_pass):
                    valid += 1
            f_pass = dict()
            continue
        sl = line.split(" ")
        for bit in sl:
            k, v = bit.split(":")
            f_pass[k] = v
    return valid


def test():
    inp_tst = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013",
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
        "",
        "hcl:#cfa07d eyr:2025 pid:166559648",
        "iyr:2011 ecl:brn hgt:59in",
        ""
    ]
    assert part_one(inp_tst) == 2
    inp_tst = [
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
        "hcl:#623a2f",
        "",
        "eyr:2029 ecl:blu cid:129 byr:1989",
        "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "",
        "hcl:#888785",
        "hgt:164cm byr:2001 iyr:2015 cid:88",
        "pid:545766238 ecl:hzl",
        "eyr:2022",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
        "",
    ]
    assert part_two(inp_tst) == 4

def get_result():
    inp = input_list_string("2020", "04")
    test()
    print(part_one(inp))
    print(part_two(inp))