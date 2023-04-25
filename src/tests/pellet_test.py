import unittest
from sprites.pellet import Pellet

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.pellet1 = Pellet(0, 0, 0)
        self.pellet2 = Pellet(0, 0, 5)

    def test_score_up(self):
        self.assertEqual(self.pellet1.score, 0)
        self.pellet1.score_up()
        self.assertEqual(self.pellet1.score, 1)
        self.pellet1.score_up()
        self.pellet1.score_up()
        self.assertEqual(self.pellet1.score, 3)

    def test_get_score(self):
        self.assertEqual(self.pellet2.get_score(), self.pellet2.score)
        self.assertEqual(self.pellet1.get_score(), self.pellet1.score)
