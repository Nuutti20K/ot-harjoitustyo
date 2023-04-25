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
    

#def movement_coordinator(self):
#        if self.head.next_move <= 0:
#            self.head.next_move = self.head.speed
#            self.head.heading = self.head.queued_heading
#            if self.head.growth:
#                self.add_body()
#                self.head.growth = False
#            else:
#                self.body_movement()
#            self.head_movement()
#        else:
#            self.head.next_move -= 1