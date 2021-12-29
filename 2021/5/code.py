def read_file():
    res = []
    with open("input.txt") as f:
        for line in f.read().strip().split("\n"):
            coord1, coord2 = line.split(" -> ")
            res.append(
                [
                    tuple([int(x) for x in "".join(coord1).split(",")]),
                    tuple([int(x) for x in "".join(coord2).split(",")]),
                ]
            )
    return res


def part1(data):
    field = {}
    for coords in data:
        coord1, coord2 = coords
        x1, y1 = coord1
        x2, y2 = coord2
        if x1 == x2 or y1 == y2:
            mark_in_range(field, *coords)

    return count_overlap(field, 2)


def part2(data):
    field = {}
    for coords in data:
        mark_in_range(field, *coords)

    return count_overlap(field, 2)


def mark_in_range(field, coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    while x1 != x2 or y1 != y2:
        if (x1, y1) in field:
            field[(x1, y1)] += 1
        else:
            field[(x1, y1)] = 1
        x1 += 0 if x1 == x2 else -1 if x1 > x2 else 1
        y1 += 0 if y1 == y2 else -1 if y1 > y2 else 1
    if (x2, y2) in field:
        field[(x2, y2)] += 1
    else:
        field[(x2, y2)] = 1


def count_overlap(field, min_num):
    return len([x for x in field if field[x] >= min_num])


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
