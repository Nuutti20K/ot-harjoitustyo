import unittest
from level import Level

grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 2, 2, 2, 2, 3, 0, 4, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(grid)

    def test_head_collides_with_wall(self):
        head = self.level.head
        head.heading = "up"

        collision = self.level.collision_check(head)
        self.assertEqual(collision, False)
        self.level.head_movement()
        collision = self.level.collision_check(head)
        self.assertEqual(collision, False)
        self.level.head_movement()
        collision = self.level.collision_check(head)
        self.assertEqual(collision, False)
        self.level.head_movement()
        collision = self.level.collision_check(head)
        self.assertEqual(collision, True)
        self.level.head_movement()
        collision = self.level.collision_check(head)
        self.assertEqual(collision, False)

    def test_head_collides_with_body(self):
        head = self.level.head
        head.heading = "down"

        collision = self.level.collision_check(head)
        self.assertEqual(collision, False)
        self.level.head_movement()
        collision = self.level.collision_check(head)
        self.assertEqual(collision, False)
        self.level.head_movement()
        collision = self.level.collision_check(head)
        self.assertEqual(collision, True)
        self.level.head_movement()
        collision = self.level.collision_check(head)
        self.assertEqual(collision, False)

    def test_head_collides_with_pellet(self):
        head = self.level.head

        collision = self.level.pellet_check()
        self.assertEqual(collision, False)
        self.level.head_movement()
        collision = self.level.pellet_check()
        self.assertEqual(collision, False)
        self.level.head_movement()
        collision = self.level.pellet_check()
        self.assertEqual(collision, True)
        self.level.head_movement()
        collision = self.level.pellet_check()
        self.assertEqual(collision, False)
        self.level.head_movement()
