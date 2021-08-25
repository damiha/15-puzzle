import unittest
from move import Move


class TestMove(unittest.TestCase):

    def test_get_inverse(self):
        self.assertEqual(Move.DOWN, Move.get_inverse(Move.UP))
        self.assertEqual(Move.LEFT, Move.get_inverse(Move.RIGHT))
        self.assertEqual(Move.UP, Move.get_inverse(Move.DOWN))
        self.assertEqual(Move.RIGHT, Move.get_inverse(Move.LEFT))
