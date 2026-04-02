import numpy as np
import random

random.seed(3)

def move(ckb, position, who):
    if who == 'a':
        if position == 7:
            ckb[0][0] = 'X'
        elif position == 8:
            ckb[0][1] = 'X'
        elif position == 9:
            ckb[0][2] = 'X'
        elif position == 4:
            ckb[1][0] = 'X'
        elif position == 5:
            ckb[1][1] = 'X'
        elif position == 6:
            ckb[1][2] = 'X'
        elif position == 1:
            ckb[2][0] = 'X'
        elif position == 2:
            ckb[2][1] = 'X'
        elif position == 3:
            ckb[2][2] = 'X'
    else:
        if position == 7:
            ckb[0][0] = '*'
        elif position == 8:
            ckb[0][1] = '*'
        elif position == 9:
            ckb[0][2] = '*'
        elif position == 4:
            ckb[1][0] = '*'
        elif position == 5:
            ckb[1][1] = '*'
        elif position == 6:
            ckb[1][2] = '*'
        elif position == 1:
            ckb[2][0] = '*'
        elif position == 2:
            ckb[2][1] = '*'
        elif position == 3:
            ckb[2][2] = '*'


def checkrepeat(ckb, pos):
    if pos == 7 and ckb[0][0] == ' ':
        return True
    elif pos == 8 and ckb[0][1] == ' ':
        return True
    elif pos == 9 and ckb[0][2] == ' ':
        return True
    elif pos == 4 and ckb[1][0] == ' ':
        return True
    elif pos == 5 and ckb[1][1] == ' ':
        return True
    elif pos == 6 and ckb[1][2] == ' ':
        return True
    elif pos == 1 and ckb[2][0] == ' ':
        return True
    elif pos == 2 and ckb[2][1] == ' ':
        return True
    elif pos == 3 and ckb[2][2] == ' ':
        return True
    else:
        return False

def checkwin(ckb, player):
    if player == 'a':
        if ckb[0][0] == ckb[0][1] == ckb[0][2] == 'X':
            return 1
        if ckb[1][0] == ckb[1][1] == ckb[1][2] == 'X':
            return 1
        if ckb[2][0] == ckb[2][1] == ckb[2][2] == 'X':
            return 1
        if ckb[0][0] == ckb[1][0] == ckb[2][0] == 'X':
            return 1
        if ckb[0][1] == ckb[1][1] == ckb[2][1] == 'X':
            return 1
        if ckb[0][2] == ckb[1][2] == ckb[2][2] == 'X':
            return 1
        if ckb[0][0] == ckb[1][1] == ckb[2][2] == 'X':
            return 1
        if ckb[0][2] == ckb[1][1] == ckb[2][0] == 'X':
            return 1

    if player == 'b':
        if ckb[0][0] == ckb[0][1] == ckb[0][2] == '*':
            return 0
        if ckb[1][0] == ckb[1][1] == ckb[1][2] == '*':
            return 0
        if ckb[2][0] == ckb[2][1] == ckb[2][2] == '*':
            return 0
        if ckb[0][0] == ckb[1][0] == ckb[2][0] == '*':
            return 0
        if ckb[0][1] == ckb[1][1] == ckb[2][1] == '*':
            return 0
        if ckb[0][2] == ckb[1][2] == ckb[2][2] == '*':
            return 0
        if ckb[0][0] == ckb[1][1] == ckb[2][2] == '*':
            return 0
        if ckb[0][2] == ckb[1][1] == ckb[2][0] == '*':
            return 0

def checklose(ckb):
    space = np.where(ckb == ' ')
    if space[0] == 0 and space[1] == 0:
        if (ckb[0][1] != ckb[0][2]) and (ckb[1][1] != ckb[2][2]) and (ckb[1][0] != ckb[2][0]):
            return 0
    elif space[0] == 0 and space[1] == 1:
        if (ckb[1][1] != ckb[2][1]) and (ckb[0][0] != ckb[0][2]) :
            return 0
    elif space[0] == 0 and space[1] == 2:
        if (ckb[0][0] != ckb[0][1]) and (ckb[1][2] != ckb[2][2]) and (ckb[1][1] != ckb[2][0]):
            return 0
    elif space[0] == 1 and space[1] == 0:
        if (ckb[1][1] != ckb[1][2]) and (ckb[0][0] != ckb[2][0]):
            return 0
    elif space[0] ==1  and space[1] == 1:
        if (ckb[1][0] != ckb[1][2]) and (ckb[0][1] != ckb[2][1]) and (ckb[0][0] != ckb[2][2]) and (ckb[0][2]!= ckb[2][0]):
            return 0
    elif space[0] == 1 and space[1] == 2:
        if (ckb[1][0] != ckb[1][1]) and (ckb[2][0] != ckb[2][2]):
            return 0
    elif space[0] == 2 and space[1] == 0:
        if (ckb[0][0] != ckb[1][0]) and (ckb[2][0] != ckb[1][1]) and (ckb[2][1] != ckb[2][2]):
            return 0
    elif space[0] == 2 and space[1] == 1:
        if (ckb[0][1] != ckb[0][2]) and (ckb[2][0] != ckb[2][2]):
            return 0
    elif space[0] == 2 and space[1] == 2:
        if (ckb[2][0] != ckb[2][1]) and (ckb[0][0] != ckb[1][1]) and (ckb[0][2] != ckb[1][2]):
            return 0
    else:
        return 1
    return 1

def finds_win(ckb):
    if ckb[0][0] == ckb[0][1] == '*' and ckb[0][2] == ' ':
        return 9
    if ckb[0][0] == ckb[0][2] == "*" and ckb[0][1] == ' ':
        return 8
    if ckb[0][1] == ckb[0][2] == "*" and ckb[0][0] == ' ':
        return 7
    if ckb[1][0] == ckb[1][1] == "*" and ckb[1][2] == ' ':
        return 6
    if ckb[1][0] == ckb[1][2] == "*" and ckb[1][1] == ' ':
        return 5
    if ckb[1][1] == ckb[1][2] == "*" and ckb[1][0] == ' ':
        return 4
    if ckb[2][0] == ckb[2][1] == "*" and ckb[2][2] == ' ':
        return 3
    if ckb[2][0] == ckb[2][2] == "*" and ckb[2][1] == ' ':
        return 2
    if ckb[2][1] == ckb[2][2] == "*" and ckb[2][0] == ' ':
        return 1
    # up = horizontal
    if ckb[0][0] == ckb[1][0] == "*" and ckb[2][0] == ' ':
        return 1
    if ckb[0][0] == ckb[2][0] == "*" and ckb[1][0] == ' ':
        return 4
    if ckb[1][0] == ckb[2][0] == "*" and ckb[0][0] == ' ':
        return 7
    if ckb[0][1] == ckb[1][1] == "*" and ckb[2][1] == ' ':
        return 2
    if ckb[0][1] == ckb[2][1] == "*" and ckb[1][1] == ' ':
        return 5
    if ckb[1][1] == ckb[2][1] == "*" and ckb[0][1] == ' ':
        return 8
    if ckb[0][2] == ckb[1][2] == "*" and ckb[2][2] == ' ':
        return 3
    if ckb[0][2] == ckb[2][2] == "*" and ckb[1][2] == ' ':
        return 6
    if ckb[1][2] == ckb[2][2] == "*" and ckb[0][2] == ' ':
        return 9
    # up = vertical
    if ckb[0][0] == ckb[1][1] == "*" and ckb[2][2] == ' ':
        return 3
    if ckb[0][0] == ckb[2][2] == "*" and ckb[1][1] == ' ':
        return 5
    if ckb[1][1] == ckb[2][2] == "*" and ckb[0][0] == ' ':
        return 7
    if ckb[0][2] == ckb[1][1] == "*" and ckb[2][0] == ' ':
        return 1
    if ckb[0][2] == ckb[2][0] == "*" and ckb[1][1] == ' ':
        return 5
    if ckb[1][1] == ckb[2][0] == "*" and ckb[0][2] == ' ':
        return 9
    # up = diagonal
    return 0


def finds_space(ckb):
    if ckb[0][0] == ckb[0][1] == 'X' and ckb[0][2] == ' ':
        return 9
    if ckb[0][0] == ckb[0][2] == "X" and ckb[0][1] == ' ':
        return 8
    if ckb[0][1] == ckb[0][2] == "X" and ckb[0][0] == ' ':
        return 7
    if ckb[1][0] == ckb[1][1] == "X" and ckb[1][2] == ' ':
        return 6
    if ckb[1][0] == ckb[1][2] == "X" and ckb[1][1] == ' ':
        return 5
    if ckb[1][1] == ckb[1][2] == "X" and ckb[1][0] == ' ':
        return 4
    if ckb[2][0] == ckb[2][1] == "X" and ckb[2][2] == ' ':
        return 3
    if ckb[2][0] == ckb[2][2] == "X" and ckb[2][1] == ' ':
        return 2
    if ckb[2][1] == ckb[2][2] == "X" and ckb[2][0] == ' ':
        return 1
    # up = horizontal
    if ckb[0][0] == ckb[1][0] == "X" and ckb[2][0] == ' ':
        return 1
    if ckb[0][0] == ckb[2][0] == "X" and ckb[1][0] == ' ':
        return 4
    if ckb[1][0] == ckb[2][0] == "X" and ckb[0][0] == ' ':
        return 7
    if ckb[0][1] == ckb[1][1] == "X" and ckb[2][1] == ' ':
        return 2
    if ckb[0][1] == ckb[2][1] == "X" and ckb[1][1] == ' ':
        return 5
    if ckb[1][1] == ckb[2][1] == "X" and ckb[0][1] == ' ':
        return 8
    if ckb[0][2] == ckb[1][2] == "X" and ckb[2][2] == ' ':
        return 3
    if ckb[0][2] == ckb[2][2] == "X" and ckb[1][2] == ' ':
        return 6
    if ckb[1][2] == ckb[2][2] == "X" and ckb[0][2] == ' ':
        return 9
    # up = vertical
    if ckb[0][0] == ckb[1][1] == "X" and ckb[2][2] == ' ':
        return 3
    if ckb[0][0] == ckb[2][2] == "X" and ckb[1][1] == ' ':
        return 5
    if ckb[1][1] == ckb[2][2] == "X" and ckb[0][0] == ' ':
        return 7
    if ckb[0][2] == ckb[1][1] == "X" and ckb[2][0] == ' ':
        return 1
    if ckb[0][2] == ckb[2][0] == "X" and ckb[1][1] == ' ':
        return 5
    if ckb[1][1] == ckb[2][0] == "X" and ckb[0][2] == ' ':
        return 9
    # up = diagonal
    return 0

def cpu_1st_move(ckb):
    if ckb[0][0] == "X" or ckb[2][0] == "X" or ckb[0][2] == "X" or ckb[2][2] == "X":
        return 5
    elif ckb[1][1] == "X":
        first_center = random.randint(1,4)
        if (first_center == 1):
            return 7
        if (first_center == 2):
            return 9
        if (first_center == 3):
            return 1
        if (first_center == 4):
            return 3
    return 0


checkerboard = np.array([[' ', ' ', ' '],
                         [' ', ' ', ' '],
                         [' ', ' ', ' ']])
p1 = input("are you nanwew:")
x1 = 0
x = 0
y1 = 0
y = 0
legal_input = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
whowin = 'computer'
n = 0
cpu_move = 0
first_turn = True
while True:
    while True:
        movea = input("{} you first x :".format(p1))
        if movea not in legal_input:
            print("jfkdsl;a")
            continue
        movea = int(movea)
        if checkrepeat(ckb=checkerboard, pos=movea):
            break
        print("i really don't have nothing")
    move(checkerboard, movea, "a")
    if checkwin(ckb=checkerboard, player='a') == 1:
        whowin = 'a'
        break
    n += 1
    if n >= 9:
        break

    if first_turn and cpu_1st_move(ckb=checkerboard) != 0:
        # first_turn = False
        moveb = cpu_1st_move(ckb=checkerboard)
    elif finds_space(ckb=checkerboard) == 0 and finds_win(ckb=checkerboard) == 0:
         while True:
            cpu_move = random.randint(1,9)
            if checkrepeat(ckb=checkerboard, pos=cpu_move):
                moveb = cpu_move
                break

    elif finds_win(ckb=checkerboard) == 0:
        moveb = finds_space(ckb=checkerboard)

    else:
        moveb = finds_win(ckb=checkerboard)

    move(checkerboard, moveb, "b")
    first_turn = False
    print(checkerboard)
    if checkwin(ckb=checkerboard, player='b') == 0:
        whowin = 'b'
        break
    n += 1
    if n == 8:
        if not (checklose(ckb=checkerboard)):
            break
    if n >= 9:
        break
if whowin == 'a':
    print("a ((((((((((((((((((((((((({}))))))))))))))))))))))))) die".format("computer"))
if whowin == 'b':
    print("a ((((((((((((((((((((((((({}))))))))))))))))))))))))) die".format(p1))
if whowin == 'computer':
    print("a (((((((((((((((((((((((((y'all))))))))))))))))))))))))) die")