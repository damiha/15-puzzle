from solvers import BFSSolver, DFSSolver, DepthLimitedDFSSolver, IterativeDFSSolver
from statistics import Statistics

from node import Node
from move import Move
from properties import Properties as prop


class GameBoard:

    def __init__(self):
        self.solution = []
        self.move_pointer = -1
        self.shuffled_without_solution = False

        self.current_node = Node.create_goal_node()
        self.goal_node = Node.create_goal_node()

    def shuffle_game_board(self):
        self.current_node = Node.create_random_node()
        self.shuffled_without_solution = True

    def solve(self):

        if self.shuffled_without_solution:
            solver = BFSSolver(self.current_node, self.goal_node)
            self.solution = solver.solve()
            self.move_pointer = -1
            self.shuffled_without_solution = False

    def move_forward(self):

        next_move_pointer = self.move_pointer + 1

        if next_move_pointer < len(self.solution):
            self.move_pointer = next_move_pointer
            forward_move = self.solution[self.move_pointer]

            self.current_node = self.current_node.get_node_after_move(forward_move)

        else:
            self.move_pointer = len(self.solution)

    def move_backward(self):

        if self.move_pointer >= 0:
            if self.move_pointer == len(self.solution):
                self.move_pointer = len(self.solution) - 1

            backward_move = self.solution[self.move_pointer].get_inverse()
            self.move_pointer -= 1

            self.current_node = self.current_node.get_node_after_move(backward_move)

        else:
            self.move_pointer = -1