def read_file():
    with open("input.txt") as f:
        return f.read().strip().split("\n")


valid_opening = "({[<"
valid_closing = ")}]>"
matching_closing = {"{": "}", "(": ")", "[": "]", "<": ">"}


def get_illegal_chars(line):
    stack = []
    for c in line:
        if len(stack) > 0:
            if c in valid_opening:
                stack.append(c)
            elif c in valid_closing:
                if stack[-1] in valid_closing:
                    continue
                if matching_closing[stack[-1]] != c:
                    return c
                else:
                    stack.pop()
            else:
                raise Exception("Invalid character")
        else:
            stack.append(c)
    return None


def part1(data):
    points_table = {")": 3, "]": 57, "}": 1197, ">": 25137, None: 0}
    return sum([points_table[get_illegal_chars(line)] for line in data])


def get_missing_chars(line):
    stack = []
    missingCharsList = []
    for c in line:
        if len(stack) > 0:
            if c in valid_opening:
                stack.append(c)
            elif c in valid_closing:
                if stack[-1] in valid_closing:
                    continue
                if matching_closing[stack[-1]] != c:
                    return ""
                else:
                    stack.pop()
        else:
            stack.append(c)

    res = ""
    while stack:
        res += matching_closing[stack.pop()]
    return res


def part2(data):
    points_table = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for line in data:
        total = 0
        illegal_chars = get_missing_chars(line)
        for c in illegal_chars:
            total = total * 5 + points_table[c]
        if total != 0:
            scores.append(total)
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
