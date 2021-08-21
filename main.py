import time
from tkinter import *

import solver
import node
import properties as prop

master = Tk()
master.title(prop.WINDOW_TITLE)

w = Canvas(master, width=prop.CANVAS_WIDTH, height=prop.CANVAS_HEIGHT)
w.pack()


def draw(game_node):
    draw_grid()
    draw_entries(game_node.entries)


def draw_entries(entries):

    for i in range(0, prop.CELLS_PER_COLUMN):
        for j in range(0, prop.CELLS_PER_ROW):

            center_x = prop.CELL_HEIGHT * (j + 0.5)
            center_y = prop.CELL_HEIGHT * (i + 0.5)

            top_left_x = prop.CELL_WIDTH * j
            top_left_y = prop.CELL_HEIGHT * i

            bottom_right_x = top_left_x + prop.CELL_WIDTH
            bottom_right_y = top_left_y + prop.CELL_HEIGHT

            if entries[i][j] != prop.CELL_EMPTY:
                w.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y, fill=prop.CELL_BG_COLOR)
                w.create_text(center_x, center_y, fill=prop.TEXT_COLOR, font=prop.TEXT_FONT, text=str(entries[i][j]))


def draw_grid():
    draw_horizontal_lines()
    draw_vertical_lines()


def draw_vertical_lines():
    for i in range(0, prop.CELLS_PER_ROW):
        start_x = i * prop.CELL_WIDTH
        start_y = 0
        end_x = start_x
        end_y = prop.CANVAS_HEIGHT

        w.create_line(start_x, start_y, end_x, end_y)


def draw_horizontal_lines():
    for i in range(0, prop.CELLS_PER_COLUMN):
        start_x = 0
        start_y = i * prop.CELL_HEIGHT
        end_x = prop.CANVAS_WIDTH
        end_y = start_y

        w.create_line(start_x, start_y, end_x, end_y)


start_node = node.Node.create_random_node(5)

draw(start_node)

solution = solver.dfs_depth_limited(start_node, 5)
print(solution)

master.resizable(False, False)
mainloop()
