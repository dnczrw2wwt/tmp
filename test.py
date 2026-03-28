import numpy as np


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


#
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

checkerboard = np.array([[' ', ' ', ' '],
                         [' ', ' ', ' '],
                         [' ', ' ', ' ']])
p1 = input("are you nanwew:")
p2 = input("are you sdft:")
x1 = 0
x = 0
y1 = 0
y = 0
legal_input = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
whowin = 'computer'
n = 0
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
    print(checkerboard)
    if checkwin(ckb=checkerboard, player='a') == 1:
        whowin = 'a'
        break
    n += 1
    if n >= 9:
        break

    while True:
        moveb = input("{} dan u shekonde 8 :".format(p2))
        if moveb not in legal_input:
            print("a;sldkjf")
            continue
        moveb = int(moveb)
        if checkrepeat(ckb=checkerboard, pos=moveb):
            break
        print("you sr")
    move(checkerboard, moveb, "b")
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
    print("a ((((((((((((((((((((((((({}))))))))))))))))))))))))) die".format(p2))
if whowin == 'b':
    print("a ((((((((((((((((((((((((({}))))))))))))))))))))))))) die".format(p1))
if whowin == 'computer':
    print("a (((((((((((((((((((((((((y'all))))))))))))))))))))))))) die")
