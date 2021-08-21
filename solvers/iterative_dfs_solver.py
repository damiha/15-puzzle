from solvers import Solver, DepthLimitedDFSSolver
from statistics import Statistics
import sys


class IterativeDFSSolver(Solver):

    def __init__(self, start_node, goal_node):
        super().__init__(start_node, goal_node)
        self.solver = None
        self.depth_limit = 0

    def create_stats(self):
        self.stats = Statistics("depth first search (iterative deepening)")

    def change_stats(self):
        solver_stats = self.solver.get_stats()
        self.stats.max_iterations += solver_stats.max_iterations

        self.stats.max_space = max(solver_stats.max_space, self.stats.max_space)

    def solve(self):
        solution = []

        while True:

            self.set_solver()
            solution = self.solver.solve()

            self.update_stats()

            just_starting = self.depth_limit == 0

            if self.is_solution(solution) or just_starting:
                return solution

            self.depth_limit += 1

    def set_solver(self):
        self.solver = DepthLimitedDFSSolver(self.start_node, self.goal_node, self.depth_limit)

        if self.stats is not None:
            self.solver.create_stats()
