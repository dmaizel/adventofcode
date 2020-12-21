inp = "input2.txt"

lines = open(inp).read().strip().split('\n')

def part_one():
    valid = 0
    for line in lines:
        rule_str, password = line.split(':') 
        letter = rule_str[-1]
        minn, maxx = rule_str[0:-2].split('-')
        letters_in_password = password.count(letter) 
        if letters_in_password >= int(minn) and letters_in_password <= int(maxx):
            valid += 1

    return valid


def part_two():
    valid = 0
    for line in lines:
        rule_str, password = line.split(':') 
        letter = rule_str[-1]
        first, second = rule_str[0:-2].split('-')
        if (password[int(first)] + password[int(second)]).count(letter) == 1:
            valid += 1

    return valid

print(part_one())
print(part_two())
