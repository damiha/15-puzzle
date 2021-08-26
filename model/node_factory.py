import random

from properties import Properties
from model import Node


class NodeFactory:

    @staticmethod
    def create_node_from_entries(entries):
        gap = NodeFactory.find_gap(entries)
        return Node(entries, gap, None)

    @staticmethod
    def find_gap(entries):

        for y in range(0, Properties.CELLS_PER_COLUMN):
            for x in range(0, Properties.CELLS_PER_ROW):
                if entries[y][x] == Properties.CELL_EMPTY:
                    return [y, x]
        # TODO: raise meaningful exception
        raise Exception

    @staticmethod
    def create_random_node():

        goal_node = NodeFactory.create_goal_node()
        current_node = NodeFactory.create_goal_node()

        for i in range(0, Properties.AMOUNT_SHUFFLES):
            next_nodes = current_node.get_next_nodes()
            current_node = random.choice(next_nodes)

        # cut parent relation so that get_solution() works
        current_node.parent = None

        if current_node != goal_node:
            return current_node
        else:
            return NodeFactory.create_random_node()

    @staticmethod
    def create_goal_node():

        goal_entries = []

        for i in range(0, Properties.CELLS_PER_COLUMN):

            row_entries = []

            for j in range(0, Properties.CELLS_PER_ROW):
                cells_in_previous_rows = Properties.CELLS_PER_ROW * i
                cell_in_current_row = j + 1
                cell_number = cells_in_previous_rows + cell_in_current_row
                row_entries.append(cell_number)

            goal_entries.append(row_entries)

        gap_row_index = Properties.CELLS_PER_ROW - 1
        gap_col_index = Properties.CELLS_PER_COLUMN - 1

        goal_entries[gap_col_index][gap_row_index] = Properties.CELL_EMPTY
        return NodeFactory.create_node_from_entries(goal_entries)

    @staticmethod
    def empty_node():
        return Node(None, None, None)