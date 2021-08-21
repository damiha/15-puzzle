from abc import ABC, abstractmethod


class Solver(ABC):

    def __init__(self, start_node, goal_node):
        self.start_node = start_node
        self.goal_node = goal_node

        self.seen = set()

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
            current_node = current_node.parent

        solution.reverse()
        return solution


