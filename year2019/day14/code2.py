import math
with open("input.txt") as f:
    s = f.read().strip()


def parse(kk):
    idx = kk.find(" ")
    return (int(kk[:idx]), kk[idx+1:])


recipes = {}
for line in s.split("\n"):
    ing, out = line.split(" => ")
    ing = ing.split(", ")
    ing = [parse(inga) for inga in ing]
    out = parse(out)
    recipes[out[1]] = (ing, out)


def get_required(fuel_amount):
    required = {}
    required['FUEL'] = fuel_amount

    while any(required[key] > 0 and key != "ORE" for key in required):
        z = [k for k in required if required[k] > 0 and k != "ORE"][0]
        zq = required[z]
        outq = recipes[z][1][0]
        qq = math.ceil(required[z]/outq)
        required[z] -= outq*qq
        for ing in recipes[z][0]:
            if ing[1] in required:
                required[ing[1]] += ing[0]*qq
            else:
                required[ing[1]] = ing[0]*qq
    return required['ORE']


print(get_required(1))

high = 10000000
low = 0
while low < high:
    mid = (low + high) // 2
    req = get_required(mid)
    print(mid, req)
    if req > 1000000000000:
        high = mid - 1
    elif req < 1000000000000:
        low = mid + 1

print('result', low)
