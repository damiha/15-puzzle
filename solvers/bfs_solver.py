from solvers import Solver
from statistics import Statistics
import sys

class BFSSolver(Solver):

    def __init__(self, start_node, goal_node):
        super().__init__(start_node, goal_node)
        self.queue = []

    def create_stats(self):
        self.stats = Statistics("breadth first search")

    def change_stats(self):
        self.stats.max_iterations += 1

        current_space_queue = sys.getsizeof(self.queue)
        current_space_seen = sys.getsizeof(self.seen)
        current_space = current_space_seen + current_space_queue

        self.stats.max_space = max(self.stats.max_space, current_space)

    def solve(self):

        self.queue.append(self.start_node)

        while len(self.queue) > 0:

            self.update_stats()

            current_node = self.queue.pop(0)

            if current_node == self.goal_node:
                return self.get_solution(current_node)

            self.seen.add(current_node)

            next_nodes = current_node.get_next_nodes()

            for next_node in next_nodes:
                if next_node not in self.seen:
                    self.queue.append(next_node)

        return []
