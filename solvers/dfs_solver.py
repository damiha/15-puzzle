from solvers import Solver
from model.statistics import Statistics
import sys


class DFSSolver(Solver):

    def solve(self):

        return self.dfs(self.start_node, 0)

    def dfs(self, current_node, depth):
        self.update_stats()

        if self.limit_exceeded(depth):
            return []

        if current_node == self.goal_node:
            return self.get_solution(current_node)

        self.seen.add(current_node)

        for next_node in current_node.get_next_nodes():
            if next_node not in self.seen:
                solution = self.dfs(next_node, depth + 1)

                if self.is_solution(solution):
                    return solution

        return []

    def limit_exceeded(self, depth):
        return False

    def create_stats(self):
        self.stats = Statistics("depth first search")

    def change_stats(self):
        self.stats.max_iterations += 1
        current_space = sys.getsizeof(self.seen)

        self.stats.max_space = max(self.stats.max_space, current_space)
