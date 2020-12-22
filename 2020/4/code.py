import re

def readFile():
    result = []
    with open(f"input.txt", "r") as f:
        for data in f.read().split("\n\n"):
            result.append(dict(d.split(':') for d in data.strip().replace('\n', ' ').split(' ')))
    return result

def assert_all_required_fields(data):
    return all((k in data for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")))

def part1(passports):
    return len(passports)

def part2(passports):
    patterns = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "20(1[0-9]|20)",
        "eyr": "20(2[0-9]|30)",
        "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
        "hcl": "#[0-9a-f]{6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}",
        "cid": ".*"
    }
    return sum((all((re.fullmatch(patterns[k], passport[k]) for k in passport)) for passport in passports))

if __name__ == "__main__":
    passports = readFile()
    valid_passports = [passport for passport in passports if assert_all_required_fields(passport)]
    print(f"Part 1: {part1(valid_passports)}")
    print(f"Part 2: {part2(valid_passports)}")
