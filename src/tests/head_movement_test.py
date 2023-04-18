import unittest
from level import Level

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 2, 2, 2, 2, 3, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 4, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(map)

    def test_can_move_forwards(self):
        head = self.level.head

        self.assertEqual(head.rect.x, 5*50)
        self.assertEqual(head.rect.y, 3*50)

        self.level.head_movement()
        self.assertEqual(head.rect.x, 6*50)
        self.assertEqual(head.rect.y, 3*50)

        self.level.head_movement()
        self.assertEqual(head.rect.x, 7*50)
        self.assertEqual(head.rect.y, 3*50)
