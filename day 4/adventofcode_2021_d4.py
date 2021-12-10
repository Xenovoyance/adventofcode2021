import time

def part_one():
    input = "adventofcode_2021_d4_input.txt"
    board_numbers = []
    drawn_numbers = []
    boards = []
    _tmp_board = []
    
    # get all the drawn numbers
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
                i+=1
    
    print(boards[0])

    boards[0] = draw_a_number(boards[0],'22')
    boards[0] = draw_a_number(boards[0],'13')
    boards[0] = draw_a_number(boards[0],'17')
    boards[0] = draw_a_number(boards[0],'11')
    boards[0] = draw_a_number(boards[0],'0')

    if check_for_bingo(boards[0]):
        print("Bingo!")

def check_for_bingo(board):
    bingo = False

    # check both for horizintal and vertical bingo
    if (board[0].startswith("*")):
        if (board[5].startswith("*")):
            if (board[10].startswith("*")):
                if (board[15].startswith("*")):
                    if (board[20].startswith("*")):
                        bingo = True
    if (board[0].startswith("*")):
        if (board[1].startswith("*")):
            if (board[2].startswith("*")):
                if (board[3].startswith("*")):
                    if (board[4].startswith("*")):
                        bingo = True
    if (board[1].startswith("*")):
        if (board[6].startswith("*")):
            if (board[11].startswith("*")):
                if (board[16].startswith("*")):
                    if (board[21].startswith("*")):
                        bingo = True
    if (board[2].startswith("*")):
        if (board[7].startswith("*")):
            if (board[12].startswith("*")):
                if (board[17].startswith("*")):
                    if (board[22].startswith("*")):
                        bingo = True
    if (board[3].startswith("*")):
        if (board[8].startswith("*")):
            if (board[13].startswith("*")):
                if (board[18].startswith("*")):
                    if (board[23].startswith("*")):
                        bingo = True
    if (board[4].startswith("*")):
        if (board[9].startswith("*")):
            if (board[14].startswith("*")):
                if (board[19].startswith("*")):
                    if (board[24].startswith("*")):
                        bingo = True
    # horizontal
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

# draw a single number from a specific board
def draw_a_number(board,number_to_check):
    board = ["*"+number_to_check if x==number_to_check else x for x in board]
    return board


if __name__ == "__main__":
    #start_time = time.time()
    #print("Part 1: " + part_one() + " executed in " + (str((time.time() - start_time)* 1000)) + " ms")
    part_one()