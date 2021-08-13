import time
from tkinter import *
import random

master = Tk()
master.title("15-Puzzle-Solver")

canvas_width = 600
canvas_height = 600
cellsize = canvas_width / 4

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

def draw_grid():
    global cellsize

    # vertical lines
    for i in range(0, int(canvas_width / cellsize)):
        w.create_line(i*cellsize, 0, i*cellsize, canvas_height)

    # vertical lines
    for i in range(0, int(canvas_height / cellsize)):
        w.create_line(0,i * cellsize, canvas_width, i * cellsize)


def draw_entries(entries):

    for i in range(0, len(entries)):
        for j in range(0, len(entries[0])):
            center_y = cellsize * (i + 0.5)
            center_x = cellsize * (j + 0.5)

            if(entries[i][j] != -1):
                w.create_rectangle(j * cellsize, i * cellsize, (j + 1) * cellsize, (i + 1) *cellsize, fill="#fff")
                w.create_text(center_x, center_y, fill="darkblue", font="Times 20 bold", text=str(entries[i][j]))

# direction = { 1 = UP, 2 = RIGHT, 3 = BOTTOM, 4 = LEFT}
# gap = position [0..3, 0...3]
def check_move(entries, gap, direction):

    tile = [-1,-1]

    if(direction == 1 and gap[0] > 0):
        tile = [gap[0] - 1, gap[1]]

    elif (direction == 2 and gap[1] < 3):
        tile =  [gap[0], gap[1] + 1]

    elif (direction == 3 and gap[0] < 3):
       tile = [gap[0] + 1, gap[1]]

    elif (direction == 4 and gap[1] > 0):
        tile = [gap[0], gap[1] - 1]

    else:
        # invalid new title since illegal operation
        return []

    return tile

def get_next_moves(entries, gap):
    next_moves = []

    for i in range(1,5):
        next_gap = check_move(entries, gap, i)
        if(next_gap != []):
            next_moves.append(i)
    return next_moves


def swap(entries, pos1, pos2):
    temp = entries[pos1[0]][pos1[1]]
    entries[pos1[0]][pos1[1]] = entries[pos2[0]][pos2[1]]
    entries[pos2[0]][pos2[1]] = temp

def slide(entries, gap, direction):
    tile = check_move(entries, gap, direction)

    if(len(tile) != 0):
        swap(entries, gap, tile)
        return tile
    else:
        print("ILLEGAL MOVE DETECTED!")
        return []

def create_random_entries(n_shuffles):
    entries = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,-1]]
    gap = [3,3]

    for i in range(0, n_shuffles):
        next_moves = get_next_moves(entries, gap)
        next_move = random.choice(next_moves)
        gap = slide(entries, gap, next_move)

    return entries

draw_grid()
draw_entries(create_random_entries(100))
mainloop()
