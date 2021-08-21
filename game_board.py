from tkinter import *
from solvers import BFSSolver, DFSSolver, DepthLimitedDFSSolver, IterativeDFSSolver
from statistics import Statistics

from node import Node
from move import Move
import properties as prop


class GameBoard:

    def __init__(self):
        self.solution = []
        self.move_pointer = -1
        self.shuffled_without_solution = False

        self.root = Tk()
        self.root.title(prop.WINDOW_TITLE)

        self.current_node = Node.create_goal_node()
        self.goal_node = Node.create_goal_node()

        self.add_top_bar()

        self.w = Canvas(self.root, width=prop.CANVAS_WIDTH, height=prop.CANVAS_HEIGHT)
        self.w.grid(row=1, column=0, rowspan=4, columnspan=4)

    def add_top_bar(self):
        self.shuffle_btn = Button(self.root, text="Shuffle", command=self.shuffle_game_board)
        self.shuffle_btn.grid(row=0, column=0)

        self.solve_btn = Button(self.root, text="Solve", command=self.solve)
        self.solve_btn.grid(row=0, column=1)

        self.forward_btn = Button(self.root, text="=>", command=self.move_forward)
        self.forward_btn.grid(row=0, column=2)

        self.backward_btn = Button(self.root, text="<=", command=self.move_backward)
        self.backward_btn.grid(row=0, column=3)

    def shuffle_game_board(self):
        self.current_node = Node.create_random_node()
        self.shuffled_without_solution = True
        self.draw()

    def solve(self):

        if self.shuffled_without_solution:
            solver = BFSSolver(self.current_node, self.goal_node)
            self.solution = solver.solve()
            self.move_pointer = -1
            self.shuffled_without_solution = False

            print(self.solution)

    def move_forward(self):
        print(self.move_pointer)

        next_move_pointer = self.move_pointer + 1

        if next_move_pointer < len(self.solution):
            self.move_pointer = next_move_pointer
            forward_move = self.solution[self.move_pointer]

            self.current_node = self.current_node.get_node_after_move(forward_move)
            self.draw()

        else:
            self.move_pointer = len(self.solution)

    def move_backward(self):
        print(self.move_pointer)

        if self.move_pointer >= 0:
            if self.move_pointer == len(self.solution):
                self.move_pointer = len(self.solution) - 1

            backward_move = self.solution[self.move_pointer].get_inverse()
            self.move_pointer -= 1

            self.current_node = self.current_node.get_node_after_move(backward_move)
            self.draw()

        else:
            self.move_pointer = -1

    def draw(self):
        self.draw_background()
        self.draw_grid()
        self.draw_entries(self.current_node.entries)

        self.root.resizable(False, False)
        mainloop()

    def draw_background(self):
        self.w.create_rectangle(0, 0, prop.CANVAS_WIDTH, prop.CANVAS_HEIGHT, fill=prop.CANVAS_BG_COLOR)

    def draw_grid(self):
        self.draw_horizontal_lines()
        self.draw_vertical_lines()

    def draw_vertical_lines(self):
        for i in range(0, prop.CELLS_PER_ROW):
            start_x = i * prop.CELL_WIDTH
            start_y = 0
            end_x = start_x
            end_y = prop.CANVAS_HEIGHT

            self.w.create_line(start_x, start_y, end_x, end_y)

    def draw_horizontal_lines(self):
        for i in range(0, prop.CELLS_PER_COLUMN):
            start_x = 0
            start_y = i * prop.CELL_HEIGHT
            end_x = prop.CANVAS_WIDTH
            end_y = start_y

            self.w.create_line(start_x, start_y, end_x, end_y)

    def draw_entries(self, entries):

        for i in range(0, prop.CELLS_PER_COLUMN):
            for j in range(0, prop.CELLS_PER_ROW):

                center_x = prop.CELL_HEIGHT * (j + 0.5)
                center_y = prop.CELL_HEIGHT * (i + 0.5)

                top_left_x = prop.CELL_WIDTH * j
                top_left_y = prop.CELL_HEIGHT * i

                bottom_right_x = top_left_x + prop.CELL_WIDTH
                bottom_right_y = top_left_y + prop.CELL_HEIGHT

                if entries[i][j] != prop.CELL_EMPTY:
                    self.w.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y,
                                            fill=prop.CELL_BG_COLOR)
                    self.w.create_text(center_x, center_y,
                                       fill=prop.TEXT_COLOR, font=prop.TEXT_FONT, text=str(entries[i][j]))
