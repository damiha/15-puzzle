from solvers import Solver, DepthLimitedDFSSolver
from model.statistics import Statistics


class IterativeDFSSolver(Solver):

    def __init__(self):
        super().__init__()
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

            if self.is_solution(solution):
                return solution

            self.depth_limit += 1

    def set_solver(self):
        self.solver = DepthLimitedDFSSolver(self.depth_limit)
        self.solver.load_context(self.start_node, self.goal_node)

        if self.stats is not None:
            self.solver.create_stats()
