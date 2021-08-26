import unittest
from model.solution_iterator import SolutionIterator
from model.node import Node
from model.node_factory import NodeFactory
from solvers import BFSSolver
from model.move import Move


class TestSolutionIterator(unittest.TestCase):


    def test_has_next(self):

        test_entries = [[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [-1, 10, 11, 12],
                        [9, 13, 14, 15]
                        ]

        start_node, solution = self.get_current_node_and_solution(test_entries)
        iterator = SolutionIterator(start_node, solution)

        self.assertTrue(iterator.has_next())

    def test_has_prev_fail(self):

        test_entries = [[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [-1, 10, 11, 12],
                        [9, 13, 14, 15]
                        ]

        start_node, solution = self.get_current_node_and_solution(test_entries)
        iterator = SolutionIterator(start_node, solution)

        self.assertFalse(iterator.has_prev())

    def test_has_next_fail(self):
        test_entries = [[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [-1, 10, 11, 12],
                        [9, 13, 14, 15]
                        ]

        start_node, solution = self.get_current_node_and_solution(test_entries)
        iterator = SolutionIterator(start_node, solution)

        iterator.next()
        iterator.next()
        iterator.next()
        iterator.next()
        self.assertFalse(iterator.has_next())

    def test_next(self):
        test_entries = [[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [-1, 10, 11, 12],
                        [9, 13, 14, 15]
                        ]

        start_node, solution = self.get_current_node_and_solution(test_entries)
        iterator = SolutionIterator(start_node, solution)

        self.assertEqual(start_node.get_node_after_move(Move.DOWN), iterator.next())
        self.assertEqual(start_node.get_node_after_move(Move.DOWN), iterator.current_node)
        self.assertEqual(1, iterator.index)

    def test_next_multiple_times(self):
        test_entries = [[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [-1, 10, 11, 12],
                        [9, 13, 14, 15]
                        ]

        start_node, solution = self.get_current_node_and_solution(test_entries)
        iterator = SolutionIterator(start_node, solution)

        iterator.next()
        iterator.next()
        iterator.next()
        self.assertEqual(3, iterator.index)

    def test_next_throw(self):
        test_entries = [[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [-1, 10, 11, 12],
                        [9, 13, 14, 15]
                        ]

        start_node, solution = self.get_current_node_and_solution(test_entries)
        iterator = SolutionIterator(start_node, solution)

        iterator.next()
        iterator.next()
        iterator.next()
        iterator.next()
        self.assertRaises(Exception, iterator.next)

    def get_current_node_and_solution(self, entries):

        gap = NodeFactory.find_gap(entries)
        current_node = Node(entries, gap, None)
        solver = BFSSolver()
        solver.load_context(current_node, NodeFactory.create_goal_node())
        solution = solver.solve()

        return current_node, solution
