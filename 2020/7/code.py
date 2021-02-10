import re

def readFile():
    return open('input.txt').read().splitlines()

def describe_bags(data):
    bags = {}
    for line in data:
        colour = re.match(r"(.+?) bags contain", line)[1]  
        bags[colour] = re.findall(r"(\d+?) (.*?) bags?", line)
    
    return bags

def has_shiny_gold(colour):
    if colour == "shiny gold": 
        return True
    else:
        return any(has_shiny_gold(c) for _, c in bags[colour] )

def count_bags(bag_type):
    return 1 + sum(int(number)*count_bags(colour) for number, colour in bags[bag_type])

def part1(bags):
    bag_count = 0
    for bag in bags:
        if has_shiny_gold(bag):
            bag_count += 1
    return bag_count - 1

def part2(bags):
    return count_bags("shiny gold") - 1

if __name__ == '__main__':
    bags = describe_bags(readFile())
    print(part1(bags))
    print(part2(bags))
