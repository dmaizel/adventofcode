def readFile():
    with open("input.txt", "r") as file:
        return [int(num) for num in file.read().split(',')]

def solve(numbers, stop_num):
    turn_spoken = {num: i + 1 for i, num in enumerate(numbers[:-1])}
    last_num = numbers[-1]

    for turn_num in range(len(numbers) + 1, stop_num + 1):
        last_turn_num = turn_num - 1

        if last_num in turn_spoken:
            spoken_num = last_turn_num - turn_spoken[last_num]
        else:
            spoken_num = 0

        turn_spoken[last_num] = last_turn_num
        last_num = spoken_num

    return spoken_num

def part1(numbers):
    return solve(numbers, 2020)

def part2(numbers):
    return solve(numbers, 30000000)

if __name__ == '__main__':
    numbers = readFile()
    print(part1(numbers))
    print(part2(numbers))
