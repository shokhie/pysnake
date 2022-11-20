from time import sleep
ROWS = 25
COLS = 30
snake = [[3, 2], [2, 2]]
def board(snake):
    snakex = [i[0] for i in snake] # extracting x co-ordinates
    snakey = [i[1] for i in snake] # extracting y co-ordinates
    for j in range(ROWS):
        for i in range(COLS):
            if i in snakex and j in snakey:
                print("@", end='')
            elif i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1:
                print("#", end= '')
            else:
                print(" ", end = '')
        print()
while True:
    sleep(0.2)
    board(snake)
    snake = [[(i[0]+1) % ROWS, i[1]] for i in snake]
