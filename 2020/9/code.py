def readFile():
    return [int(x) for x in open('input.txt').read().strip().split('\n')]

def part1(numbers):
    preamble_len = 25
    i = 0
    while i < len(numbers) - 1:
        preamble = numbers[i:i+preamble_len]
        found = False
        target = numbers[i+preamble_len]
        for num in preamble:
            y = target - num
            if y in preamble and y != num:
                found = True
        if not found:
            return target
        i += 1

def part2(numbers, invalid_num):
    i = 1
    j = 0   
    while i < len(numbers) - 1:
        while invalid_num < sum(numbers[j:i]):
            j += 1
        if sum(numbers[j:i]) == invalid_num:
            return min(numbers[j:i]) + max(numbers[j:i])
        i += 1
            

if __name__ == '__main__':
    numbers = readFile()
    invalid_num = part1(numbers)
    print(invalid_num)
    print(part2(numbers, invalid_num))
