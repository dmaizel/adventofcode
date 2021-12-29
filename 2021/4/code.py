BOARD_LEN = 5

def read_file():
    boards_res = []
    with open('input.txt') as f:
        nums, *boards = f.read().split('\n\n')
        nums = nums.split(',')
        for board in boards:
            boards_res.append([[x, False] for x in board.split()])
    return nums, boards_res

def has_won(board):
    # Check rows
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            if board[i * BOARD_LEN + j][1] == False:
                break
        else:
            return True

    # Check cols
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            if board[j * BOARD_LEN + i][1] == False:
                break
        else:
            return True
    return False


def part1(data):
    nums, boards = data
    for num in nums:
        for board in boards:
            for x in board:
                if x[0] == num:
                    x[1] = True
                    break
            if has_won(board):
                return int(num) * sum([int(x[0]) for x in board if x[1] == False])
    raise AssersionError('Should not get here')


def part2(data):
    nums, boards = data
    board_wins = {}
    for num in nums:
        for i, board in enumerate(boards):
            for x in board:
                if x[0] == num:
                    x[1] = True
                    break
            if has_won(board):
                if len(board_wins) == len(boards) - 1 and i not in board_wins:
                    return int(num) * sum([int(x[0]) for x in board if x[1] == False])
                else:
                    if i not in board_wins:
                        board_wins[i] = 1

    raise AssersionError('Should not get here')


if __name__ == '__main__':
    data = read_file()
    print(part1(data))
    print(part2(data))

