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

    def test_snake_growth(self):
        head = self.level.head

        self.assertEqual(head.growth, False)
        self.level.snake_growth()
        self.assertEqual(head.growth, True)

    def test_add_body(self):
        head = self.level.head
        head.heading = "down"
        headings = []
        coordinates = []
        for part in iter(self.level.bodies.sprites()):
            headings.append(part.heading)
            coordinates.append((part.rect.x, part.rect.y))
        self.assertEqual(headings[-1], "right")
        self.assertEqual(coordinates[-1][0], 200)
        self.assertEqual(coordinates[-1][1], 150)
        
        self.level.add_body()
        headings = []
        coordinates = []
        for part in iter(self.level.bodies.sprites()):
            headings.append(part.heading)
            coordinates.append((part.rect.x, part.rect.y))
        self.assertEqual(headings[-1], "down")
        self.assertEqual(coordinates[-1][0], 250)
        self.assertEqual(coordinates[-1][1], 150)
