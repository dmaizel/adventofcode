def read_file():
    with open("input.txt") as f:
        dots, folds = f.read().strip().split("\n\n")
        dots = set(tuple(map(int, dot.split(","))) for dot in dots.split("\n"))
        folds = [fold.split()[2].split("=") for fold in folds.split("\n")]
        return dots, folds


def solve(data, part1=False):
    dots, folds = data
    for fold in folds:
        res = set()
        fold_axis, fold_at = fold
        fold_at = int(fold_at)
        for (x, y) in dots:
            if fold_axis == "y" and y > fold_at:
                res.add((x, fold_at - (y - fold_at)))
            elif fold_axis == 'x' and x > fold_at:
                res.add((fold_at - (x - fold_at), y))
            else:
                res.add((x, y))
        if part1:
            break
        dots = res

    return dots


def part1(data):
    return len(solve(data, part1=True))


def part2(data):
    dots = solve(data)
    max_x = max([x for x, _ in dots])
    max_y = max([y for _, y in dots])
    ans = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            ans += "x" if (x, y) in dots else " "
        print(ans)
        ans = ""


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    part2(data)
