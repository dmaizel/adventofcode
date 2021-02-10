def readFile():
    return [list(row) for row in open('input.txt').read().split()]

def check_num_imm_adj_occ(seats, i, j, part1=False):
    count = 0
    for row_inc, col_inc in [(0, -1), (0, 1), (1, -1), (1, 1), (1, 0), (-1, 1), (-1, -1), (-1, 0)]:
        new_i = i
        new_j = j
        while True:
            new_i += row_inc
            new_j += col_inc
            if ((0>new_i or new_i>=len(seats)) or (0>new_j or new_j>=len(seats[new_i])) or seats[new_i][new_j] == 'L'):
                break
            if seats[new_i][new_j] == '#':
                count += 1
                break
            if part1:
                break
    return count

def solve(seats, part1=False):
    while True:
        new_seats = [row[:] for row in seats]
        for i in range(len(seats)):
            for j in range(len(seats[i])): 
                num_adj = check_num_imm_adj_occ(seats, i, j, part1)
                if seats[i][j] == 'L' and num_adj == 0:
                    new_seats[i][j] = "#"
                if num_adj >= (4 if part1 else 5) and seats[i][j] == '#':
                    new_seats[i][j] = 'L'
        
        if new_seats == seats:
            return sum([row.count('#') for row in seats])
        seats = new_seats
               
def part1(seats):
    return solve(seats, part1=True) 


def part2(seats):
    return solve(seats) 
    

if __name__ == '__main__':
    seats = readFile()
    print(part1(seats))
    print(part2(seats))
