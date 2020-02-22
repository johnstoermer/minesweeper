import random

BOARD_SIZE = 5
NUM_MINES = 1
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
explored_board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

#initialize board
###place mines AND numbers
def place_mine():
    x = random.randint(0, BOARD_SIZE - 1)
    y = random.randint(0, BOARD_SIZE - 1)
    board[x][y] = 11
    for i in range(3):
        for j in range(3):
            movx = x + (i - 1)
            movy = y + (j - 1)
            try:
                if movx != -1 and movy != -1 and board[movx][movy] != 11:
                    board[movx][movy] += 1
            except:
                pass

def reset_game():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    explored_board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    for k in range(NUM_MINES):
        place_mine()

#utils
###print board
def print_board_DEBUG():
    for row in board:
        for val in row:
            print(val, end = ' ')
        print('')

def print_board():
    for i in range(BOARD_SIZE):
        print(i, end = ' ')
        for j in range(BOARD_SIZE):
            if explored_board[i][j] != 0:
                print(explored_board[i][j], end = ' ')
            else:
                print('*', end = ' ')
        print('')
    print(' ', end = ' ')
    for i in range(BOARD_SIZE):
        print(i, end = ' ')
    print('')

###click function
def click():
    while True:
        clickx = int(input('Enter X: '))
        clicky = int(input('Enter Y: '))
        flag = input('Flag or Reveal? (f or r): ')
        if flag == 'f':
            explored_board[clicky][clickx] = 2
            break
        elif flag == 'r':
            explored_board[clicky][clickx] = 1
            break
        print('Invalid input!')

###check win
def check_win():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if explored_board[i][j] == 0 and board[i][j] == 11:
                continue
            elif explored_board[i][j] == 1 and board[i][j] == 11:
                print('GAME OVER!')
                reset_game()
                return
            else:
                print('YOU WIN!')
                reset_game()
                return
#start game
reset_game()
while True:
    #print_board_DEBUG()
    print_board()
    click()
    check_win()
