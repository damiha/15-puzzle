from properties import Properties
from solvers import DFSSolver
from model.statistics import Statistics


class DepthLimitedDFSSolver(DFSSolver):

    def __init__(self, depth_limit=Properties.DEFAULT_DEPTH_LIMIT):
        super().__init__()
        self.depth_limit = depth_limit

    def limit_exceeded(self, depth):
        return depth > self.depth_limit

    def create_stats(self):
        self.stats = Statistics("depth first search (depth limited)")
