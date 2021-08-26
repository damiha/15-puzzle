import copy

from properties import Properties
from model import Move


class Node:
    parent = None
    entries = None
    gap = None

    # which instruction was applied to parent to reach this state
    instruction = None

    def __init__(self, entries, gap, parent):
        self.entries = entries
        self.parent = parent
        self.gap = gap

    def __eq__(self, other):
        return type(other) == Node and hash(self) == hash(other)

    def __hash__(self):
        return hash(str(self.entries))

    def get_next_nodes(self):
        next_nodes = []

        for move in Move:
            if self.check_move(move):
                next_nodes.append(self.get_node_after_move(move))

        return next_nodes

    def check_move(self, direction):

        row_index_last_cell = Properties.CELLS_PER_ROW - 1
        column_index_last_cell = Properties.CELLS_PER_COLUMN - 1

        up_valid = self.gap[0] > 0
        right_valid = self.gap[1] < row_index_last_cell
        bottom_valid = self.gap[0] < column_index_last_cell
        left_valid = self.gap[1] > 0

        if direction == Move.UP and up_valid:
            return True
        elif direction == Move.RIGHT and right_valid:
            return True
        elif direction == Move.DOWN and bottom_valid:
            return True
        elif direction == Move.LEFT and left_valid:
            return True
        else:
            return False

    def get_node_after_move(self, move):
        copied_node = self.copy()
        self.apply_move_to_node(copied_node, move)

        # after move, old node is parent of new (copied) one; overwrite copy
        copied_node.parent = self
        return copied_node

    def copy(self):
        # copied node gets same reference to parent
        return Node(copy.deepcopy(self.entries), copy.deepcopy(self.gap), self.parent)

    def apply_move_to_node(self, node, move):

        old_gap = node.gap
        new_gap = None

        if move == Move.UP:
            new_gap = [self.gap[0] - 1, self.gap[1]]
        elif move == Move.RIGHT:
            new_gap = [self.gap[0], self.gap[1] + 1]
        elif move == Move.DOWN:
            new_gap = [self.gap[0] + 1, self.gap[1]]
        elif move == Move.LEFT:
            new_gap = [self.gap[0], self.gap[1] - 1]

        node.swap(new_gap, old_gap)
        node.gap = new_gap
        node.instruction = move
        return node

    def swap(self, pos1, pos2):
        temp = self.entries[pos1[0]][pos1[1]]
        self.entries[pos1[0]][pos1[1]] = self.entries[pos2[0]][pos2[1]]
        self.entries[pos2[0]][pos2[1]] = temp

    def print(self):
        for i in range(0, Properties.CELLS_PER_COLUMN):
            for j in range(0, Properties.CELLS_PER_ROW):
                print(str(self.entries[i][j]) + "\t", end = "")
            print("")
        print("")
