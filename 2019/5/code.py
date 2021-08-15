def read_file():
    with open('input.txt') as f:
        return list(map(int, f.read().strip().split(',')))

def run(prog, input_value):
    pc = 0
    lastout = None

    while prog[pc] != 99:
        op = prog[pc]
        modes = ((op // 100) % 10, (op // 1000) % 10)
        op = op % 10

        if op == 1: #add
            a, b, c = prog[pc + 1:pc + 4]
            if modes[0] == 0: a = prog[a]
            if modes[1] == 0: b = prog[b]
            prog[c] = a + b
            pc += 4
        elif op == 2: # mul
            a, b, c = prog[pc + 1:pc + 4]
            if modes[0] == 0: a = prog[a]
            if modes[1] == 0: b = prog[b]
            prog[c] = a * b
            pc += 4
        elif op == 3: #in
            a = prog[pc + 1]
            prog[a] = input_value
            pc += 2
        elif op == 4: #out
            a = prog[pc + 1]
            if modes[0] == 0: a = prog[a]
            lastout = a
            pc += 2
        elif op == 5: #jnz
            a, b = prog[pc + 1:pc + 3]
            if modes[0] == 0: a = prog[a]
            if modes[1] == 0: b = prog[b]
            pc = b if a != 0 else pc + 3
        elif op == 6: #jz
            a, b = prog[pc + 1:pc + 3]
            if modes[0] == 0: a = prog[a]
            if modes[1] == 0: b = prog[b]
            pc = b if a == 0 else pc + 3
        elif op == 7: #lt
            a, b, c = prog[pc + 1:pc + 4]
            if modes[0] == 0: a = prog[a]
            if modes[1] == 0: b = prog[b]
            prog[c] = 1 if a < b else 0
            pc += 4
        elif op == 8: #eq
            a, b, c = prog[pc + 1:pc + 4]
            if modes[0] == 0: a = prog[a]
            if modes[1] == 0: b = prog[b]
            prog[c] = 1 if a == b else 0
            pc += 4

    return lastout


data = read_file()
print(run(data[:], 1))
print(run(data[:], 5))
