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

    def test_next_move(self):
        head = self.level.head
        head.next_move = 3

        self.assertEqual(head.next_move, 3)
        self.level.movement_coordinator()
        self.assertEqual(head.next_move, 2)
        self.level.movement_coordinator()
        self.assertEqual(head.next_move, 1)
        self.level.movement_coordinator()
        self.assertEqual(head.next_move, 0)
        self.level.movement_coordinator()
        self.assertEqual(head.next_move, 10)

    def test_heading_changes(self):
        head = self.level.head
        head.next_move = 1
        head.heading = "up"
        head.queued_heading = "right"

        self.assertEqual(head.heading, "up")
        self.assertEqual(head.queued_heading, "right")
        self.level.movement_coordinator()
        self.assertEqual(head.heading, "up")
        self.assertEqual(head.queued_heading, "right")
        self.level.movement_coordinator()
        self.assertEqual(head.heading, "right")
        self.assertEqual(head.queued_heading, "right")

    def test_growth(self):
        head = self.level.head
        head.next_move = 1

        bodies = []
        for body in self.level.bodies:
            bodies.append(body)

        self.level.snake_growth()
        self.assertEqual(head.growth, True)
        self.assertEqual(len(bodies), 4)
        self.level.movement_coordinator()
        self.assertEqual(head.growth, True)
        self.assertEqual(len(bodies), 4)
        self.level.movement_coordinator()

        bodies = []
        for body in self.level.bodies:
            bodies.append(body)
        self.assertEqual(head.growth, False)
        self.assertEqual(len(bodies), 5)

