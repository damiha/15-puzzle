from solvers import DFSSolver
from statistics import Statistics
from properties import Properties as prop


class DepthLimitedDFSSolver(DFSSolver):

    def __init__(self, depth_limit=prop.DEFAULT_DEPTH_LIMIT):
        super().__init__()
        self.depth_limit = depth_limit

    def limit_exceeded(self, depth):
        return depth > self.depth_limit

    def create_stats(self):
        self.stats = Statistics("depth first search (depth limited)")
