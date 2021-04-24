def read_file():
    with open('input.txt', 'r') as f:
        return f.read().strip().split('\n')

class CustomNum1:
    def __init__(self, num):
        self.num = num

    def __add__(self, x):
        return CustomNum1(self.num + x.num)

    def __sub__(self, x):
        return CustomNum1(self.num * x.num)
    
class CustomNum2:
    def __init__(self, num):
        self.num = num

    def __sub__(self, x):
        return CustomNum2(self.num * x.num)

    def __mul__(self, x):
        return CustomNum2(self.num + x.num)


def my_eval(exp, part1=True):
    s = ""
    in_num = False

    class_name = 'CustomNum1'
    if not part1:
        class_name = 'CustomNum2'

    for ch in exp:
        if ch.isdigit() and not in_num:
            s += f"{class_name}("
            in_num = True
        if in_num and not ch.isdigit():
            s += ')'
            in_num = False
    
        s += ch

    if in_num:
        s += ')'

    return eval(s).num

def part1(expressions):
    res = 0
    for ex in expressions:
        res += my_eval(ex.replace('*', '-'))

    return res

def part2(expressions):
    res = 0
    for ex in expressions:
        res += my_eval(ex.replace('*', '-').replace('+', '*'), part1=False)

    return res

if __name__ == '__main__':
    expressions = read_file()
    print(part1(expressions))
    print(part2(expressions))
