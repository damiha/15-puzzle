from enum import Enum


class Move(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def get_inverse(self):
        if self == Move.UP:
            return Move.DOWN
        elif self == Move.RIGHT:
            return Move.LEFT
        elif self == Move.DOWN:
            return Move.UP
        elif self == Move.LEFT:
            return Move.RIGHT

