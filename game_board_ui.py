from tkinter import *
from game_board import GameBoard
from properties import Properties as prop


class GameBoardUI:

    def __init__(self):

        self.gameboard = GameBoard()

        self.root = Tk()
        self.root.title(prop.WINDOW_TITLE)

        shuffle_and_draw = lambda: [self.gameboard.shuffle_game_board(), self.draw()]
        move_forward_and_draw = lambda: [self.gameboard.move_forward(), self.draw()]
        move_backward_and_draw = lambda: [self.gameboard.move_backward(), self.draw()]

        self.shuffle_btn = Button(self.root, text="Shuffle", command=shuffle_and_draw)
        self.solve_btn = Button(self.root, text="Solve", command=self.gameboard.solve)
        self.forward_btn = Button(self.root, text="=>", command=move_forward_and_draw)
        self.backward_btn = Button(self.root, text="<=", command=move_backward_and_draw)

        self.position_buttons_at_top()

        self.w = Canvas(self.root, width=prop.CANVAS_WIDTH, height=prop.CANVAS_HEIGHT)
        self.w.grid(row=1, column=0, rowspan=4, columnspan=4)

        self.root.resizable(False, False)

    def start_main_loop(self):
        self.root.mainloop()

    def position_buttons_at_top(self):
        self.shuffle_btn.grid(row=0, column=0)
        self.solve_btn.grid(row=0, column=1)
        self.forward_btn.grid(row=0, column=2)
        self.backward_btn.grid(row=0, column=3)

    def draw(self):
        self.draw_background()
        self.draw_grid()
        self.draw_board_from_node(self.gameboard.current_node)


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

    def draw_board_from_node(self, node):

        entries = node.entries

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