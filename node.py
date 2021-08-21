import copy
import random
from enum import Enum
import properties as prop


class Move(Enum):
    UP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4


class Node:
    parent = None
    entries = None
    gap = None

    # which instruction was applied to parent to reach this state
    instruction = None

    def __init__(self, entries,gap, parent):
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

        row_index_last_cell = prop.CELLS_PER_ROW - 1
        column_index_last_cell = prop.CELLS_PER_COLUMN - 1

        up_valid = self.gap[0] > 0
        right_valid = self.gap[1] < row_index_last_cell
        bottom_valid = self.gap[0] < column_index_last_cell
        left_valid = self.gap[1] > 0

        if direction == Move.UP and up_valid:
            return True
        elif direction == Move.RIGHT and right_valid:
            return True
        elif direction == Move.BOTTOM and bottom_valid:
            return True
        elif direction == Move.LEFT and left_valid:
            return True
        else:
            return False

    def get_node_after_move(self, move):
        copied_node = self.copy()
        self.apply_move_to_node(copied_node, move)
        return copied_node

    def copy(self):
        return Node(copy.deepcopy(self.entries), copy.deepcopy(self.gap), self)

    def apply_move_to_node(self, node, move):

        old_gap = node.gap
        new_gap = None

        if move == Move.UP:
            new_gap = [self.gap[0] - 1, self.gap[1]]
        elif move == Move.RIGHT:
            new_gap = [self.gap[0], self.gap[1] + 1]
        elif move == Move.BOTTOM:
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

    @staticmethod
    def create_node_from_entries(entries):

        gap = Node.find_gap(entries)
        return Node(entries, gap, None)

    @staticmethod
    def find_gap(entries):

        for i in range(0, prop.CELLS_PER_COLUMN):
            for j in range(0, prop.CELLS_PER_ROW):
                if entries[i][j] == prop.CELL_EMPTY:
                    return [i, j]
        # THROW AN EXCEPTION

    @staticmethod
    def create_random_node(n_shuffles):

        current_node = Node.create_goal_node()

        for i in range(0,n_shuffles):
            next_nodes = current_node.get_next_nodes()
            current_node = random.choice(next_nodes)

        # cut parent relation so that get_solution() works
        current_node.parent = None
        return current_node

    @staticmethod
    def create_goal_node():

        goal_entries = []

        for i in range(0, prop.CELLS_PER_COLUMN):

            row_entries = []

            for j in range(0, prop.CELLS_PER_ROW):
                cells_in_previous_rows = prop.CELLS_PER_ROW * i
                cell_in_current_row = j + 1
                cell_number = cells_in_previous_rows + cell_in_current_row
                row_entries.append(cell_number)

            goal_entries.append(row_entries)

        gap_row_index = prop.CELLS_PER_ROW - 1
        gap_col_index = prop.CELLS_PER_COLUMN - 1

        goal_entries[gap_col_index][gap_row_index] = prop.CELL_EMPTY
        return Node.create_node_from_entries(goal_entries)

    @staticmethod
    def print(node):

        for i in range(0, prop.CELLS_PER_COLUMN):
            for j in range(0, prop.CELLS_PER_ROW):
                print(str(node.entries[i][j]) + "\t", end = "")
            print("")
        print("")
