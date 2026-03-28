import pygame
import time
import numpy as np
import random

random.seed(3)

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

def move(ckb, position, who):
    if who is True:
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


def checkwin(ckb, player):
    if player is True:
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

    if player is False:
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
    elif space[0] ==1 and space[1] == 1:
        if (ckb[1][0] != ckb[1][2]) and (ckb[0][1] != ckb[2][1]) and (ckb[0][0] != ckb[2][2]) and (ckb[0][2] != ckb[2][0]):
            return 0
    elif space[0] == 1 and space[1] == 2:
        if (ckb[1][0] != ckb[1][1]) and (ckb[0][2] != ckb[2][2]):
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

def checkarea (x, y):
    area = 0
    area7 = (0, 0, 163, 163)
    area4 = (0, 169, 163, 330)
    area1 = (0, 336, 163, 499)
    area8 = (169, 0, 330, 163)
    area5 = (169, 169, 330, 330)
    area2 = (169, 336, 330, 499)
    area9 = (336, 0, 499, 330)
    area6 = (336, 169, 499, 163)
    area3 = (336, 336, 499, 499)

    if x <= 163 :
        if y <= 163 :
            area = 7
        elif y <= 330 :
            area = 4
        elif y <= 499 :
            area = 1
    elif x <= 330 :
        if y <= 163 :
            area = 8
        elif y <= 330 :
            area = 5
        elif y <= 499 :
            area = 2
    elif x <= 499 :
        if y <= 163 :
            area = 9
        elif y <= 330 :
            area = 6
        elif y <= 499 :
            area = 3
    return area

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
        first_center = random.randint(1, 4)
        if (first_center == 1):
            return 7
        if (first_center == 2):
            return 9
        if (first_center == 3):
            return 1
        if (first_center == 4):
            return 3
    return 0

def _cpu_move(ckb, first_turn):
    if first_turn and cpu_1st_move(ckb=checkerboard) != 0:
        # first_turn = False
        return cpu_1st_move(ckb=checkerboard)
    elif finds_space(ckb=checkerboard) == 0 and finds_win(ckb=checkerboard) == 0:
         while True:
            cpu_move = random.randint(1,9)
            if checkrepeat(ckb=checkerboard, pos=cpu_move):
                return cpu_move

    elif finds_win(ckb=checkerboard) == 0:
        return finds_space(ckb=checkerboard)

    else:
        return finds_win(ckb=checkerboard)


pygame.init()
pygame.display.set_caption('TICTAC TOE')
icon = pygame.image.load('sources/images/Icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('sources/images/board.png')
screensize = background.get_size()
screen = pygame.display.set_mode((screensize[0], screensize[1]))

X = pygame.image.load('sources/images/X.png')
X_rect = X.get_rect()

Xsound = pygame.mixer.Sound('sources/sounds/player_1_sound.wav')

O = pygame.image.load('sources/images/O.png')
O_rect = O.get_rect()

Osound = pygame.mixer.Sound('sources/sounds/player_2_sound.wav')

BRUH = pygame.mixer.Sound('sources/sounds/bruh.wav')

DIE = pygame.mixer.Sound('sources/sounds/Ydie.mp3')

first_turn = True

cpu_move = 0

turn = True

time1 = pygame.time.get_ticks()
occupy = [False, False, False, False, False, False, False, False, False]


checkerboard = np.array([[' ', ' ', ' '],
                         [' ', ' ', ' '],
                         [' ', ' ', ' ']])

POS = {
    '7': (0, 0),
    '4': (0, 169),
    '1': (0, 336),
    '8': (169, 0),
    '5': (169, 169),
    '2': (169, 336),
    '9': (336, 0),
    '6': (336, 169),
    '3': (336, 336),
}

whowin = None

ifcantplayanymore = None

n = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    area = checkarea(x=pygame.mouse.get_pos()[0], y=pygame.mouse.get_pos()[1])

    if occupy[area - 1] is False:
        if pygame.mouse.get_pressed()[0]:
            screen.blit(X, POS[str(area)])
            Xsound.play()
            move(ckb=checkerboard, position=area, who=True)
            n += 1
            occupy[area - 1] = True
            turn = not turn
            __cpu_move = _cpu_move(ckb=checkerboard, first_turn=first_turn)
            screen.blit(O, POS[str(__cpu_move)])
            first_turn=False
            # Osound.play()
            move(ckb=checkerboard, position=__cpu_move, who=False)
            whowin = checkwin(ckb=checkerboard, player=turn)
            n += 1
            occupy[__cpu_move - 1] = True
            turn = not turn
            time.sleep(0.1)
            # print(n)

        if n == 8:
            ifcantplayanymore = checklose(ckb=checkerboard)
            if ifcantplayanymore == 0:
                DIE.play()
                n = 100

        if occupy == [True, True, True, True, True, True, True, True, True]:
            print('029384751495873498571498571348517034958723049582705193847501')
            time.sleep(3)
            break

        if whowin == 1:
            BRUH.play()
            n = 100
        if whowin == 0:
            print("pass")
            n = 100

    screen.blit(background, (0, 0))
    pygame.display.update()

    if n == 100:
        time.sleep(3)
        break
