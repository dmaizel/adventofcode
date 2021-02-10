def readFile():
    return sorted([int(x) for x in open('input.txt').read().strip().split('\n')])

def diff_count(numbers, n):
    curr_num = 0
    count = 0
    for num in numbers:
        if num - n == curr_num:
            count += 1
        curr_num  = num
    return count

def part1(numbers):
    return diff_count(numbers, 1) * diff_count(numbers, 3)

def part2(numbers):
    return num_ways(numbers, 0)

def num_ways(numbers, i, memo = {}):    
    if i in memo:
        return memo[i]

    if i == len(numbers) - 1:
        return 1

    total = 0
    
    if i+1 < len(numbers) and (numbers[i+1] - numbers[i]) <=3:
        total += num_ways(numbers, i+1, memo)

    if i+2 < len(numbers) and (numbers[i+2] - numbers[i]) <=3:
        total += num_ways(numbers, i+2, memo)

    if i+3 < len(numbers) and (numbers[i+3] - numbers[i]) <=3:
        total += num_ways(numbers, i+3, memo)

    memo[i] = total
    return total

if __name__ == '__main__':
    numbers = readFile()
    numbers = [0, *numbers, max(numbers)+3]
    print(part1(numbers))
    print(part2(numbers))
