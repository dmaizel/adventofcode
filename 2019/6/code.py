def read_file():
    with open('input.txt') as f:
        lines = f.read().strip().split('\n')
    orbits = tuple(line.split(')') for line in lines)
    return orbits


orbits = read_file()
orbits_dict = {child: parent for parent, child in orbits}


def count_orbits(planet):
    total = 0
    while planet in orbits_dict:
        total += 1
        planet = orbits_dict[planet]
    return total


def part1(orbits):
    return sum(map(count_orbits, orbits_dict))


def part2(data):
    pass


print(part1(orbits))
