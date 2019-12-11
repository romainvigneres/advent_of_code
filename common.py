def fpath(y, d):
    return f"year{y}/day{d}/input.txt"


def input_list_string(year, day):
    with open(fpath(year, day), "r") as f:
        return f.read().splitlines()


def input_list_integer(year, day):
    with open(fpath(year, day), "r") as f:
        return [int(x) for x in f.read().splitlines()]


def input_integer_sep(year, day, sep=","):
    with open(fpath(year, day), "r") as f:
        return [int(x) for x in f.read().splitlines()[0].split(sep)]


def input_string_sep(year, day, sep=","):
    with open(fpath(year, day), "r") as f:
        return [x for x in f.read().splitlines()[0].split(sep)]
