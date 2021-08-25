import unittest
from node_factory import NodeFactory
from node import Node
from properties import Properties as prop


class TestNodeFactory(unittest.TestCase):

    def test_find_gap_success(self):
        test_entries = [[1, 2, 3, 4],
                        [-1, 5, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]
        x = 0
        y = 1
        self.assertEqual([y,x], NodeFactory.find_gap(test_entries))

    def test_find_gap_fail(self):
        test_entries = [[1, 2, 3, 4],
                        [4, 5, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]
        # pass arguments to find gap like below
        self.assertRaises(Exception, NodeFactory.find_gap, test_entries)

    def test_create_node_from_entries(self):
        test_entries = [[1, 2, 3, 4],
                        [-1, 5, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15]
                        ]
        x = 0
        y = 1
        actual_node = NodeFactory.create_node_from_entries(test_entries)

        self.assertEqual(test_entries, actual_node.entries)
        self.assertEqual([y,x], actual_node.gap)
        self.assertIsNone(actual_node.instruction)

    def test_create_goal_node_2x2(self):

        prop.CELLS_PER_ROW = 2
        prop.CELLS_PER_COLUMN = 2

        expected_entries = [[1, 2],
                            [3, -1]
                            ]

        actual_node = NodeFactory.create_goal_node()
        self.assertEqual(expected_entries, actual_node.entries)

    def test_create_goal_node_3x3(self):

        prop.CELLS_PER_ROW = 3
        prop.CELLS_PER_COLUMN = 3

        expected_entries = [[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, -1]
                            ]

        actual_node = NodeFactory.create_goal_node()
        self.assertEqual(expected_entries, actual_node.entries)

    def test_create_goal_node_4x4(self):

        prop.CELLS_PER_ROW = 4
        prop.CELLS_PER_COLUMN = 4

        expected_entries = [[1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, -1]
                            ]

        actual_node = NodeFactory.create_goal_node()
        self.assertEqual(expected_entries, actual_node.entries)

    def test_empty_node(self):

        actual_node = NodeFactory.empty_node()
        self.assertIsNone(actual_node.entries)
        self.assertIsNone(actual_node.gap)
        self.assertIsNone(actual_node.instruction)


