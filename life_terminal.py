import random as r
from time import sleep
import os
import keyboard

def random_state(width, height):
    state = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            state[i][j] = r.randint(0, 1)
    
    return state

def render(state):
    
    height, width = len(state), len(state[0])
    show = ['' for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if state[i][j] == 0:
                show[i] += "  "
            else:
                show[i] += "O "

    for i in show:
        print(i)
    for i in range(height):
        print('\033[F', end='')

def next_board_state(state):
    height, width = len(state), len(state[0])
    next = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            neighbors = check_neighbors(state, j, i)
            if state[i][j] == 1:
                if 1 < neighbors <= 3:
                    next[i][j] = 1
                else:
                    next[i][j] = 0
            else:
                if neighbors == 3:
                    next[i][j] = 1
                else:
                    next[i][j] = 0
    
    return next

def check_neighbors(state, x, y):
    neighbors = 0
    xedge, yedge = False, False
    if x == 0 or x == len(state[0]) - 1:
        xedge = True
    if y == 0 or y == len(state) - 1:
        yedge = True
    

    if not xedge and not yedge:
        neighbors += state[y - 1][x - 1] + state[y - 1][x] + state[y - 1][x + 1]
        neighbors += state[y][x - 1] + state[y][x + 1]
        neighbors += state[y + 1][x - 1] + state[y + 1][x] + state[y + 1][x + 1]
    
    elif not yedge and xedge:
        if x == 0:
            neighbors += state[y - 1][x] + state[y - 1][x + 1]
            neighbors += state[y][x + 1]
            neighbors += state[y + 1][x] + state[y + 1][x + 1]
        else:
            neighbors += state[y - 1][x - 1] + state[y - 1][x]
            neighbors += state[y][x - 1]
            neighbors += state[y + 1][x - 1] + state[y + 1][x]

    elif (not xedge) and yedge:
        if y == 0:
            neighbors += state[y][x - 1] + state[y][x + 1]
            neighbors += state[y + 1][x - 1] + state[y + 1][x] + state[y + 1][x + 1]
        else:
            neighbors += state[y - 1][x - 1] + state[y - 1][x] + state[y - 1][x + 1]
            neighbors += state[y][x - 1] + state[y][x + 1]
    
    else:
        if x == 0:
            if y == 0:
                neighbors += state[y][x + 1] + state[y + 1][x] + state[y + 1][x + 1]
            else:
                neighbors += state[y][x + 1] + state[y - 1][x] + state[y - 1][x + 1]
        else:
            if y == 0:
                neighbors += state[y][x - 1] + state[y + 1][x - 1] + state[y + 1][x]
            else:
                neighbors += state[y][x - 1] + state[y - 1][x - 1] + state[y - 1][x]
    
    return neighbors
            

def main():
    
    initial = [[]]

    with open('state.txt', 'r') as f:
        for line in f:
            for num in line:
                if num == '\n':
                    initial.append([])
                else:
                    initial[-1].append(int(num))
    render(initial)
    next = next_board_state(initial)
    while True:
        sleep(0.1)
        render(next)
        next = next_board_state(next)

        if keyboard.is_pressed('a'):
            os.system('cls')
            break

main()