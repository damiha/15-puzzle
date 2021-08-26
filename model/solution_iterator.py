class SolutionIterator:

    def __init__(self, current_node, solution):
        self.current_node = current_node
        self.solution = solution
        self.index = 0

    def has_next(self):
        return self.index < len(self.solution)

    def next(self):

        if self.has_next():

            next_move = self.solution[self.index]
            self.index += 1
            self.current_node = self.current_node.get_node_after_move(next_move)
            return self.current_node

        else:
            # TODO: raise a more meaningful exception
            raise Exception

    def has_prev(self):
        return self.index > 0

    def is_last(self):
        return self.index == len(self.solution)

    def prev(self):

        if self.has_prev():

            # moves cant be applied in backwards only, they have to be inverted individually
            self.index -= 1
            next_move = self.solution[self.index].get_inverse()
            self.current_node = self.current_node.get_node_after_move(next_move)
            return self.current_node

        else:
            # TODO: raise a more meaningful exception
            raise Exception