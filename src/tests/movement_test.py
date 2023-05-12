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

    def test_move_body_right(self):
        bodies_x = []
        bodies_y = []
        for body in self.level.bodies:
            bodies_x.append(body.rect.x)
            bodies_y.append(body.rect.y)
        self.level.body_movement()
        i = 1
        for body in self.level.bodies:
            if i <=3:
                self.assertEqual(body.rect.x, bodies_x[i])
                self.assertEqual(body.rect.y, bodies_y[i])
            else:
                self.assertEqual(body.rect.x, 5*50)
                self.assertEqual(body.rect.y, 3*50)
            i += 1

    def test_move_body_left(self):
        i = 0
        for body in self.level.bodies:
            if i == 3:
                body.heading = "left"
            i += 1
        bodies_x = []
        bodies_y = []
        for body in self.level.bodies:
            bodies_x.append(body.rect.x)
            bodies_y.append(body.rect.y)
        self.level.body_movement()
        i = 1
        for body in self.level.bodies:
            if i <=3:
                self.assertEqual(body.rect.x, bodies_x[i])
                self.assertEqual(body.rect.y, bodies_y[i])
            else:
                self.assertEqual(body.rect.x, 3*50)
                self.assertEqual(body.rect.y, 3*50)
            i += 1

    def test_move_body_up(self):
        i = 0
        for body in self.level.bodies:
            if i == 3:
                body.heading = "up"
            i += 1
        bodies_x = []
        bodies_y = []
        for body in self.level.bodies:
            bodies_x.append(body.rect.x)
            bodies_y.append(body.rect.y)
        self.level.body_movement()
        i = 1
        for body in self.level.bodies:
            if i <=3:
                self.assertEqual(body.rect.x, bodies_x[i])
                self.assertEqual(body.rect.y, bodies_y[i])
            else:
                self.assertEqual(body.rect.x, 4*50)
                self.assertEqual(body.rect.y, 2*50)
            i += 1
    
    def test_move_body_down(self):
        i = 0
        for body in self.level.bodies:
            if i == 3:
                body.heading = "down"
            i += 1
        bodies_x = []
        bodies_y = []
        for body in self.level.bodies:
            bodies_x.append(body.rect.x)
            bodies_y.append(body.rect.y)
        self.level.body_movement()
        i = 1
        for body in self.level.bodies:
            if i <=3:
                self.assertEqual(body.rect.x, bodies_x[i])
                self.assertEqual(body.rect.y, bodies_y[i])
            else:
                self.assertEqual(body.rect.x, 4*50)
                self.assertEqual(body.rect.y, 4*50)
            i += 1