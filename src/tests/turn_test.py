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
        self.level1 = Level(grid)
        self.level2 = Level(grid)

    def test_turn_up(self):
        head1 = self.level1.head
        head2 = self.level2.head

        self.assertEqual(head1.queued_heading, "right")
        self.level1.turn_head("up")
        self.assertEqual(head1.queued_heading, "up")

        head2.queued_heading = "left"
        head2.heading = "left"
        self.assertEqual(head2.queued_heading, "left")
        self.level2.turn_head("up")
        self.assertEqual(head2.queued_heading, "up")

    def test_illegal_up_turn(self):
        head = self.level1.head

        head.queued_heading = "down"
        head.heading = "down"
        self.assertEqual(head.queued_heading, "down")
        self.level1.turn_head("up")
        self.assertEqual(head.queued_heading, "down")

    def test_turn_down(self):
        head1 = self.level1.head
        head2 = self.level2.head

        self.assertEqual(head1.queued_heading, "right")
        self.level1.turn_head("down")
        self.assertEqual(head1.queued_heading, "down")

        head2.queued_heading = "left"
        head2.heading = "left"
        self.assertEqual(head2.queued_heading, "left")
        self.level2.turn_head("down")
        self.assertEqual(head2.queued_heading, "down")

    def test_illegal_down_turn(self):
        head = self.level1.head

        head.queued_heading = "up"
        head.heading = "up"
        self.assertEqual(head.queued_heading, "up")
        self.level1.turn_head("down")
        self.assertEqual(head.queued_heading, "up")

    def test_turn_right(self):
        head1 = self.level1.head
        head2 = self.level2.head

        head1.queued_heading = "down"
        head1.heading = "down"
        self.assertEqual(head1.queued_heading, "down")
        self.level1.turn_head("right")
        self.assertEqual(head1.queued_heading, "right")

        head2.queued_heading = "up"
        head2.heading = "up"
        self.assertEqual(head2.queued_heading, "up")
        self.level2.turn_head("right")
        self.assertEqual(head2.queued_heading, "right")

    def test_illegal_right_turn(self):
        head = self.level1.head

        head.queued_heading = "left"
        head.heading = "left"
        self.assertEqual(head.queued_heading, "left")
        self.level1.turn_head("right")
        self.assertEqual(head.queued_heading, "left")

    def test_turn_left(self):
        head1 = self.level1.head
        head2 = self.level2.head

        head1.queued_heading = "down"
        head1.heading = "down"
        self.assertEqual(head1.queued_heading, "down")
        self.level1.turn_head("left")
        self.assertEqual(head1.queued_heading, "left")

        head2.queued_heading = "up"
        head2.heading = "up"
        self.assertEqual(head2.queued_heading, "up")
        self.level2.turn_head("left")
        self.assertEqual(head2.queued_heading, "left")

    def test_illegal_left_turn(self):
        head = self.level1.head

        self.assertEqual(head.queued_heading, "right")
        self.level1.turn_head("left")
        self.assertEqual(head.queued_heading, "right")

    def test_invalid_turn(self):
        head = self.level1.head

        self.assertEqual(head.queued_heading, "right")
        self.level1.turn_head("dow")
        self.assertEqual(head.queued_heading, "right")
