from properties import Properties as Properties

from model import NodeFactory
from model import SolutionIterator
from solvers import BFSSolver, DFSSolver, DepthLimitedDFSSolver, IterativeDFSSolver


class GameBoard:

    def __init__(self):

        self.shuffled_without_solution = False

        self.current_node = NodeFactory.create_goal_node()
        self.goal_node = NodeFactory.create_goal_node()

        self.set_solver(Properties.DEFAULT_SOLVER)
        self.solution = []
        self.iterator = None

    def set_solver(self, solver_name):
        solvers_by_name = {
                                "breadth first search": BFSSolver(),
                                "depth first search": DFSSolver(),
                                "depth first search (limited)": DepthLimitedDFSSolver(),
                                "depth first search (iterative)": IterativeDFSSolver()
        }
        self.solver = solvers_by_name[solver_name]

    def shuffle_game_board(self):
        self.current_node = NodeFactory.create_random_node()
        self.shuffled_without_solution = True

    def solve(self):

        if self.shuffled_without_solution:
            self.solver.load_context(self.current_node, self.goal_node)
            self.solver.create_stats()
            self.solution = self.solver.solve()
            self.iterator = SolutionIterator(self.current_node, self.solution)
            self.shuffled_without_solution = False

    def move_forward(self):
        if self.iterator is not None and self.iterator.has_next():
            self.current_node = self.iterator.next()

    def move_backward(self):
        if self.iterator is not None and self.iterator.has_prev():
            self.current_node = self.iterator.prev()
