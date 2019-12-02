def input_list_string(filepath):
    with open(filepath, 'r') as f:
        return f.read().splitlines()


def input_list_integer(filepath):
    with open(filepath, 'r') as f:
        return [int(x) for x in f.read().splitlines()]
