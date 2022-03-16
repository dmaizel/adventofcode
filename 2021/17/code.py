import re


def read_file():
    with open("input.txt") as f:
        # return [tuple(map(int,x.strip()[2:].split('..'))) for x in
        #         f.read().split(':')[1].strip().split(',')]
        xmin, xmax, ymin, ymax = map(int, re.findall(r"-?\d+", f.read()))
        assert ymin < 0 and ymax < 0
        return [(xmin, xmax), (ymin, ymax)]


def tri(n):
    return n * (n + 1) // 2


def search(xmin, xmax, ymin, ymax):
    total = 0
    yhi = 0

    for v0x in range(1, xmax + 1):
        for v0y in range(ymin, -ymin):
            x, y = 0, 0
            vx, vy = v0x, v0y

            # While we are not past the target (on either axis)
            while x <= xmax and y >= ymin:
                # If we are inside the target, the v0x and vy0 were good
                if x>= xmin and y <= ymax:
                    total += 1
                    break

                #Advance the trajectory following the rules
                x, y = (x + vx, y + vy)
                vy -= 1

                if vx > 0: #vx never goes below 0
                    vx -= 1

                #update the maximum y found so far if needed
                if y > yhi:
                    yhi = y

    return yhi, total

def part1(target_area):
    _, y = target_area
    ymin, _ = y
    return tri(ymin)


def part2(target_area):
    x, y = target_area
    _, total = search(*x, *y)
    return total


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
