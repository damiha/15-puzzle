from solvers import Solver, DepthLimitedDFSSolver


class IterativeDFSSolver(Solver):

    def solve(self):
        depth_limit = 0
        solution = []

        while True:
            solver = DepthLimitedDFSSolver(self.start_node, self.goal_node, depth_limit)
            solution = solver.solve()

            if self.is_solution(solution):
                return solution

            depth_limit += 1
