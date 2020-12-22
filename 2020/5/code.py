def readFile():
    with open(f"input.txt", "r") as f:
        return[int(line.strip().replace("F", "0").replace("B", "1")
            .replace("L", "0").replace("R", "1"), 2) for line in f.readlines()]

def part1(seat_ids):
   return max(seat_ids)            

def part2(seat_ids):
    for i in range(min(seat_ids), max(seat_ids)):
        if i not in seat_ids and i+1 in seat_ids and i-1 in seat_ids:
            return i

if __name__ == '__main__':
    seat_ids = readFile()
    print(part1(seat_ids))
    print(part2(seat_ids))
