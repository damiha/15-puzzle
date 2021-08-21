from solvers import Solver


class BFSSolver(Solver):

    def solve(self):

        queue = [self.start_node]

        while len(queue) > 0:

            current_node = queue.pop(0)

            if current_node == self.goal_node:
                return self.get_solution(current_node)

            self.seen.add(current_node)

            next_nodes = current_node.get_next_nodes()

            for next_node in next_nodes:
                if next_node not in self.seen:
                    queue.append(next_node)

        return []