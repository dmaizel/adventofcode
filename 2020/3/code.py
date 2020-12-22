lines = open('input.txt').read().split('\n')

def solve(down, right):
    ans = 0
    j = right
    for i in range(down, len(lines)-1, down):
        line = lines[i]
        if line[j%len(line)] == '#':
            ans += 1
        j += right
    return ans


def part_one():
    return solve(1,3)

def part_two():
    res = 1
    slopes = [(1,1), (3,1), (5,1), (7, 1), (1, 2)]
    for slope in slopes:
        right, down = slope
        res *= solve(down, right)
    return res


print('Part 1:')
print(part_one())
print('Part 2:')
print(part_two())
