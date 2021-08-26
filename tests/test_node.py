import unittest
from model.node import Node
from model.move import Move


class TestNode(unittest.TestCase):

    def test_eq_success(self):
        # entries are the same
        test_entries = [[1, 2, 3, 4],
                        [-1, 5, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]
        x = 0
        y = 1
        first_node = Node(test_entries, [y, x], None)
        second_node = Node(test_entries, [y, x], None)

        self.assertTrue(first_node == second_node)

    def test_eq_fail_different_entries(self):
        # entries are not the same
        test_entries_1 = [[1, 2, 3, 4],
                        [-1, 5, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]

        x_1 = 0
        y_1 = 1

        test_entries_2 = [[2, 1, 3, 4],
                          [-1, 5, 6, 7],
                          [8, 9, 10, 11],
                          [12, 13, 14, 15]
                          ]

        x_2 = 0
        y_2 = 1

        first_node = Node(test_entries_1, [y_1, x_2], None)
        second_node = Node(test_entries_2, [y_1, x_2], None)

        self.assertFalse(first_node == second_node)

    def test_copy(self):
        test_entries = [[1, 2, 3, 4],
                        [-1, 5, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]
        x = 0
        y = 1
        first_node = Node(test_entries, [y, x], test_entries)
        second_node = first_node.copy()
        
        same_memory_address = first_node is second_node
        same_entries = first_node.entries == second_node.entries
        same_gap = first_node.gap == second_node.gap
        same_parent = first_node.parent == second_node.parent

        self.assertFalse(same_memory_address)
        self.assertTrue(same_entries)
        self.assertTrue(same_gap)
        self.assertTrue(same_parent)

    def test_swap(self):
        test_entries = [[1, 2, 3, 4],
                          [-1, 5, 6, 7],
                          [8, 9, 10, 11],
                          [12, 13, 14, 15]
                          ]

        x = 0
        y = 1

        test_entries_swapped = [[2, 1, 3, 4],
                          [-1, 5, 6, 7],
                          [8, 9, 10, 11],
                          [12, 13, 14, 15]
                          ]

        actual_node = Node(test_entries, [y, x], None)
        actual_node.swap([0, 0], [0, 1])
        # entries were swapped INPLACE
        self.assertEqual(test_entries_swapped, actual_node.entries)

    def test_check_move(self):
        test_entries = [[1, 2, 3, 4],
                        [-1, 5, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]
        x = 0
        y = 1
        actual_node = Node(test_entries, [y, x], None)

        self.assertTrue(actual_node.check_move(Move.UP))
        self.assertTrue(actual_node.check_move(Move.RIGHT))
        self.assertTrue(actual_node.check_move(Move.DOWN))
        self.assertFalse(actual_node.check_move(Move.LEFT))

    def test_get_node_after_move(self):
        test_entries = [[1, 2, 3, 4],
                        [-1, 5, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]

        test_up = [[-1, 2, 3, 4],
                        [1, 5, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]

        test_right = [[1, 2, 3, 4],
                        [5, -1, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]

        test_down = [[1, 2, 3, 4],
                        [8, 5, 6, 7],
                        [-1, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]

        node = Node(test_entries, [1, 0], None)

        node_after_up = Node(test_up, [0, 0], node)
        node_after_up.instruction = Move.UP

        node_after_right = Node(test_right, [1, 1], node)
        node_after_right.instruction = Move.RIGHT

        node_after_down = Node(test_down, [2, 0], node)
        node_after_down.instruction = Move.DOWN

        self.assertTrue(TestNode.is_equal_semantically(node_after_up, node.get_node_after_move(Move.UP)))
        self.assertTrue(TestNode.is_equal_semantically(node_after_right, node.get_node_after_move(Move.RIGHT)))
        self.assertTrue(TestNode.is_equal_semantically(node_after_down, node.get_node_after_move(Move.DOWN)))

    @staticmethod
    def is_equal_semantically(first_node, second_node):

        same_entries = first_node.entries == second_node.entries
        same_gap = first_node.gap == second_node.gap
        same_parent = first_node.parent == second_node.parent
        same_instruction = first_node.instruction == second_node.instruction

        return same_entries and same_gap and same_parent and same_instruction

    def test_get_next_nodes_length(self):
        test_entries = [[1, 2, 3, 4],
                       [-1, 5, 6, 7],
                       [8, 9, 10, 11],
                       [12, 13, 14, 15]
                       ]
        x = 0
        y = 1
        actual_node = Node(test_entries, [y, x], None)

        self.assertEqual(3, len(actual_node.get_next_nodes()))
