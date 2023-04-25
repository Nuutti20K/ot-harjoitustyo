import unittest
from level import Level

grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
        self.level = Level(grid)

    def test_move_head_right(self):
        head = self.level.head

        self.assertEqual(head.rect.x, 5*50)
        self.assertEqual(head.rect.y, 3*50)

        self.level.head_movement()
        self.assertEqual(head.rect.x, 6*50)
        self.assertEqual(head.rect.y, 3*50)

        self.level.head_movement()
        self.assertEqual(head.rect.x, 7*50)
        self.assertEqual(head.rect.y, 3*50)

    def test_move_head_left(self):
        head = self.level.head
        head.heading = "left"

        self.assertEqual(head.rect.x, 5*50)
        self.assertEqual(head.rect.y, 3*50)

        self.level.head_movement()
        self.assertEqual(head.rect.x, 4*50)
        self.assertEqual(head.rect.y, 3*50)

        self.level.head_movement()
        self.assertEqual(head.rect.x, 3*50)
        self.assertEqual(head.rect.y, 3*50)

    def test_move_head_up(self):
        head = self.level.head
        head.heading = "up"

        self.assertEqual(head.rect.x, 5*50)
        self.assertEqual(head.rect.y, 3*50)

        self.level.head_movement()
        self.assertEqual(head.rect.x, 5*50)
        self.assertEqual(head.rect.y, 2*50)

        self.level.head_movement()
        self.assertEqual(head.rect.x, 5*50)
        self.assertEqual(head.rect.y, 1*50)

    def test_move_head_down(self):
        head = self.level.head
        head.heading = "down"

        self.assertEqual(head.rect.x, 5*50)
        self.assertEqual(head.rect.y, 3*50)

        self.level.head_movement()
        self.assertEqual(head.rect.x, 5*50)
        self.assertEqual(head.rect.y, 4*50)

        self.level.head_movement()
        self.assertEqual(head.rect.x, 5*50)
        self.assertEqual(head.rect.y, 5*50)
