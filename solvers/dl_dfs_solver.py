from solvers import DFSSolver
from statistics import Statistics


class DepthLimitedDFSSolver(DFSSolver):

    def __init__(self, start_node, goal_node, depth_limit):
        super().__init__(start_node, goal_node)
        self.depth_limit = depth_limit

    def limit_exceeded(self, depth):
        return depth > self.depth_limit

    def create_stats(self):
        self.stats = Statistics("depth first search (depth limited)")
