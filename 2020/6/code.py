from collections import defaultdict # Gets rid of if, else blocks

def readFile():
    result = []
    with open(f"input.txt", "r") as f:
        for data in f.read().split("\n\n"):
            result.append(data)
    return result

def part1(groups):
    return sum(len(''.join(set(group.strip().replace('\n', '')))) for group in groups)

def part2(groups):
    count = 0
    for group in [group.strip() for group in groups]:
        dic = defaultdict(int)
        for i in group:
            dic[i] += 1
        for v in dic.values():
            if v == len(group.splitlines()):
                count += 1
    return count

if __name__ == "__main__":
    groups = readFile()
    print(part1(groups))
    print(part2(groups))
