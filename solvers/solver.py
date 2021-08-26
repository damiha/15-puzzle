from abc import ABC, abstractmethod

from model.node_factory import NodeFactory


class Solver(ABC):

    def __init__(self):
        self.seen = set()

        self.start_node = NodeFactory.empty_node()
        self.goal_node = NodeFactory.empty_node()
        self.stats = None

    # TODO: prevent NullPointerException
    def load_context(self, start_node, goal_node):
        self.start_node = start_node
        self.goal_node = goal_node

    @abstractmethod
    def create_stats(self):
        pass

    @abstractmethod
    def change_stats(self):
        pass

    def update_stats(self):
        if self.stats is not None:
            self.change_stats()

    def get_stats(self):
        return self.stats

    @abstractmethod
    def solve(self):
        pass

    def is_solution(self, solution):
        return len(solution) > 0

    def get_solution(self, end_node):

        solution = []
        current_node = end_node

        while current_node.parent is not None:
            solution.append(current_node.instruction)
            next_node = current_node.parent
            current_node = next_node

        solution.reverse()
        return solution


