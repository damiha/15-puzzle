from tkinter import *
from properties import Properties

from model import GameBoard


class GameBoardUI:

    def __init__(self):
        self.gameboard = GameBoard()

        self.root = Tk()
        self.root.title(Properties.WINDOW_TITLE)

        self.clicked = StringVar()
        self.clicked.set(Properties.DEFAULT_SOLVER)

        disable_shuffle_and_draw = lambda: [
            self.change_button_states_on_shuffle(),
            self.gameboard.shuffle_game_board(),
            self.draw()
        ]
        solve_and_enable = lambda: [
            self.read_and_set_solver(),
            self.gameboard.solve(),
            self.enable_buttons_if_solution_exists()
        ]
        move_forward_and_draw = lambda: [
            self.gameboard.move_forward(),
            self.draw()
        ]
        move_backward_and_draw = lambda: [
            self.gameboard.move_backward(),
            self.draw()
        ]

        self.shuffle_btn = Button(self.root, text="Shuffle", command=disable_shuffle_and_draw)
        self.solve_btn = Button(self.root, text="Solve", state="disable", command=solve_and_enable)
        self.forward_btn = Button(self.root, text="=>", state="disabled", command=move_forward_and_draw)
        self.backward_btn = Button(self.root, text="<=", state="disabled", command=move_backward_and_draw)
        self.position_buttons_at_top()

        self.solver_drop_down = OptionMenu(self.root, self.clicked, *Properties.SOLVER_OPTIONS)
        self.solver_drop_down.grid(row=0, column=1)

        self.w = Canvas(self.root, width=Properties.CANVAS_WIDTH, height=Properties.CANVAS_HEIGHT)
        self.w.grid(row=1, column=0, rowspan=5, columnspan=5)

        self.root.resizable(False, False)

    def change_button_states_on_shuffle(self):
        self.solve_btn.config(state="active")
        self.forward_btn.config(state="disabled")
        self.backward_btn.config(state="disabled")

    def enable_buttons_if_solution_exists(self):
        if len(self.gameboard.solution) > 0:
            self.forward_btn.config(state="active")
            self.backward_btn.config(state="active")

    def read_and_set_solver(self):
        solver_name = self.clicked.get()
        self.gameboard.set_solver(solver_name)
        self.solve_btn.config(state="disabled")

    def start_main_loop(self):
        self.root.mainloop()

    def position_buttons_at_top(self):
        self.shuffle_btn.grid(row=0, column=0)
        self.solve_btn.grid(row=0, column=2)
        self.forward_btn.grid(row=0, column=3)
        self.backward_btn.grid(row=0, column=4)

    def draw(self):
        self.draw_background()
        self.draw_grid()
        self.draw_board_from_node(self.gameboard.current_node)

    def draw_background(self):
        self.w.create_rectangle(0, 0, Properties.CANVAS_WIDTH, Properties.CANVAS_HEIGHT, fill=Properties.CANVAS_BG_COLOR)

    def draw_grid(self):
        self.draw_horizontal_lines()
        self.draw_vertical_lines()

    def draw_vertical_lines(self):
        for i in range(0, Properties.CELLS_PER_ROW):
            start_x = i * Properties.CELL_WIDTH
            start_y = 0
            end_x = start_x
            end_y = Properties.CANVAS_HEIGHT

            self.w.create_line(start_x, start_y, end_x, end_y)

    def draw_horizontal_lines(self):
        for i in range(0, Properties.CELLS_PER_COLUMN):
            start_x = 0
            start_y = i * Properties.CELL_HEIGHT
            end_x = Properties.CANVAS_WIDTH
            end_y = start_y

            self.w.create_line(start_x, start_y, end_x, end_y)

    def draw_board_from_node(self, node):

        entries = node.entries

        for i in range(0, Properties.CELLS_PER_COLUMN):
            for j in range(0, Properties.CELLS_PER_ROW):

                center_x = Properties.CELL_HEIGHT * (j + 0.5)
                center_y = Properties.CELL_HEIGHT * (i + 0.5)

                top_left_x = Properties.CELL_WIDTH * j
                top_left_y = Properties.CELL_HEIGHT * i

                bottom_right_x = top_left_x + Properties.CELL_WIDTH
                bottom_right_y = top_left_y + Properties.CELL_HEIGHT

                if entries[i][j] != Properties.CELL_EMPTY:
                    self.w.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y,
                                            fill=Properties.CELL_BG_COLOR)
                    self.w.create_text(center_x, center_y,
                                       fill=Properties.TEXT_COLOR, font=Properties.TEXT_FONT, text=str(entries[i][j]))