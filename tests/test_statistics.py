import unittest
from statistics import Statistics


class TestStatistics(unittest.TestCase):

    def test_reset_statistics(self):

        stats = Statistics("BFS")
        stats.max_space = 50
        stats.max_iterations = 90
        stats.reset_statistics()

        self.assertEqual(0, stats.max_iterations)
        self.assertEqual(0, stats.max_space)
