def read_file():
    with open('input.txt') as f:
        return f.read().splitlines()

data = read_file()
rl = len(data)
cl = len(data[0])

dd = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if (i != 0 or j != 0):
            dd.append((i, j))

def has_xmas(i, j, d):
    dx, dy = d
    for k, v in enumerate("XMAS"):
        ii = i + k * dx
        jj = j + k * dy
        if not (0 <= ii < rl and 0 <= jj < cl):
            return False
        if data[ii][jj] != v:
            return False
        
    return True

def part1():
    ans = 0

    for i in range(rl):
        for j in range(rl):
            for d in dd:
                ans += has_xmas(i, j, d)
    return ans

def has_xmas2(i, j):
    if not (1 <= i < rl - 1 and 1 <= j < cl - 1):
        return False
    if data[i][j] != 'A':
        return False

    diag1 = f'{data[i-1][j-1]}{data[i+1][j+1]}'
    diag2 = f'{data[i-1][j+1]}{data[i+1][j-1]}'

    return diag1 in ["MS", "SM"] and diag2 in ["MS", "SM"]

def part2():
    ans = 0

    for i in range(rl):
        for j in range(rl):
            ans += has_xmas2(i, j)

    return ans

if __name__ == '__main__':
    print(part1())
    print(part2())
