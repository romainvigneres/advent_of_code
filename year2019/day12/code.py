import math


def least_common_mul(x, y):
    return (x * y) // math.gcd(x, y)


class Moon:
    def __init__(self, position):
        self.pos = position
        self.vel = [0, 0, 0]

    def pot(self):
        return sum([abs(x) for x in self.pos])

    def kin(self):
        return sum([abs(x) for x in self.vel])

    def energy(self):
        return self.pot() * self.kin()

    def update(self):
        for x in range(3):
            self.pos[x] += self.vel[x]


def part_one(lst, steps):
    list_moon = [Moon(x) for x in lst]
    for _ in range(steps):
        for a in range(4):
            moon_a = list_moon[a]
            for b in range(4):
                if a == b:
                    continue
                moon_b = list_moon[b]
                for c in range(3):
                    if moon_a.pos[c] < moon_b.pos[c]:
                        moon_a.vel[c] += 1
                    elif moon_a.pos[c] > moon_b.pos[c]:
                        moon_a.vel[c] -= 1
        for moon in list_moon:
            moon.update()
    return sum([x.energy() for x in list_moon])


def test_one():
    inp_test = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
    assert part_one(inp_test, 10) == 179
    inp_test2 = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]
    assert part_one(inp_test2, 100) == 1940


def one_d_orbits(positions):
    velocities = [0] * 4

    first_state = hash(tuple(velocities) + tuple(positions))
    steps = 0
    while True:
        for idx1 in range(4):
            for idx2 in range(idx1 + 1, 4):
                if positions[idx1] < positions[idx2]:
                    velocities[idx1] += 1
                    velocities[idx2] -= 1
                elif positions[idx1] > positions[idx2]:
                    velocities[idx1] -= 1
                    velocities[idx2] += 1
        for x in range(4):
            positions[x] += velocities[x]

        steps += 1
        if first_state == (hash(tuple(velocities) + tuple(positions))):
            return steps


def part_two(input_lst):
    cycle0 = one_d_orbits([m[0] for m in input_lst])
    cycle1 = one_d_orbits([m[1] for m in input_lst])
    cycle2 = one_d_orbits([m[2] for m in input_lst])
    return least_common_mul(cycle0, least_common_mul(cycle1, cycle2))


def test_two():
    inp_test2 = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]
    assert part_two(inp_test2) == 4686774924

def get_result():
    input_list = [[14, 4, 5], [12, 10, 8], [1, 7, -10], [16, -5, 3]]
    test_one()
    print("Part one", part_one(input_list, 1000))
    test_two()
    print("Part two", part_two(input_list))

