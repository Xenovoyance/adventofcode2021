import time


def part_one():
    input = "adventofcode_2021_d4_input.txt"
    board_numbers = []
    drawn_numbers = []
    boards = []
    _tmp_board = []

    with open(input, "r") as f:
        for id, line in enumerate(f.readlines()):
            if id == 0:
                for number in line.strip().split(','):
                    drawn_numbers.append(number)
            else:
                if line.strip() != '':
                    board_numbers.append(line.strip().split())

    i = 0
    for board_row in board_numbers:
        for num in board_row:
            _tmp_board.append(num)
            if i == 24:
                boards.append(_tmp_board)
                _tmp_board = []
                i = 0
            else:
                i += 1
    play_bingo(drawn_numbers, boards)


def check_for_bingo(board):
    bingo = False
    for i in range(5):
        if (board[i+1].startswith("*")):
            if (board[i+5].startswith("*")):
                if (board[i+10].startswith("*")):
                    if (board[i+15].startswith("*")):
                        if (board[i+20].startswith("*")):
                            bingo = True
    if (board[0].startswith("*")):
        if (board[1].startswith("*")):
            if (board[2].startswith("*")):
                if (board[3].startswith("*")):
                    if (board[4].startswith("*")):
                        bingo = True
        if (board[5].startswith("*")):
            if (board[10].startswith("*")):
                if (board[15].startswith("*")):
                    if (board[20].startswith("*")):
                        bingo = True
    if (board[5].startswith("*")):
        if (board[6].startswith("*")):
            if (board[7].startswith("*")):
                if (board[8].startswith("*")):
                    if (board[9].startswith("*")):
                        bingo = True
    if (board[10].startswith("*")):
        if (board[11].startswith("*")):
            if (board[12].startswith("*")):
                if (board[13].startswith("*")):
                    if (board[14].startswith("*")):
                        bingo = True
    if (board[15].startswith("*")):
        if (board[16].startswith("*")):
            if (board[17].startswith("*")):
                if (board[18].startswith("*")):
                    if (board[19].startswith("*")):
                        bingo = True
    if (board[20].startswith("*")):
        if (board[21].startswith("*")):
            if (board[22].startswith("*")):
                if (board[23].startswith("*")):
                    if (board[24].startswith("*")):
                        bingo = True
    return bingo


def draw_a_number(board, number_to_check):
    return ["*"+number_to_check if x == number_to_check else x for x in board]


def play_bingo(bingo_numbers, bingo_boards):
    lowest = lowest_winning = 999
    lowest_board = []
    highest_board = []
    highest = highest_winning = 0
    for bid, board in enumerate(bingo_boards):
        for nid, number in enumerate(bingo_numbers):
            board = draw_a_number(board, number)
            if (check_for_bingo(board)):
                if nid < lowest:
                    lowest = nid
                    lowest_board = board
                    lowest_winning = number
                if nid > highest:
                    highest = nid
                    highest_board = board
                    highest_winning = number
                break

    lowest_answer = 0
    for num in lowest_board:
        if not num.startswith("*"):
            lowest_answer += int(num)
    print("First winner was board " + str(lowest) + " (winning number was " +
          str(lowest_winning) + "). Part 1 answer: " + str(int(lowest_answer) * int(lowest_winning)))

    highest_answer = 0
    for num in highest_board:
        if not num.startswith("*"):
            highest_answer += int(num)
    print("Last winner was board " + str(highest) + " (winning number was " +
          str(highest_winning) + "). Part 2 answer: " + str(int(highest_answer) * int(highest_winning)))


if __name__ == "__main__":
    start_time = time.time()
    part_one()
    print("Executed in " + (str((time.time() - start_time) * 1000)) + " ms")
