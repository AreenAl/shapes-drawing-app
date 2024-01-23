# test_shapes.py
import unittest
from point import Point
from rectangle import Rectangle
from square import Square
from box import Box
from cube import Cube
from main import ShapeManager

class TestShapes(unittest.TestCase):
    def test_point_creation(self):
        point = Point(3, 5)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 5)

    def test_rectangle_methods(self):
        rectangle = Rectangle(Point(1, 2), Point(4, 6))
        self.assertEqual(rectangle.get_width(), 3)
        self.assertEqual(rectangle.get_height(), 4)
        self.assertEqual(rectangle.get_area(), 12)

    def test_square_creation(self):
        square = Square(Point(1, 2), Point(5, 6))
        self.assertEqual(square.get_width(), 4)
        self.assertEqual(square.get_height(), 4)
        self.assertEqual(square.get_area(), 16)

    def test_box_methods(self):
        box = Box(Point(1, 2), Point(4, 6))
        self.assertEqual(box.get_width(), 3)
        self.assertEqual(box.get_height(), 4)
        self.assertEqual(box.get_area(), 12)
        self.assertEqual(box.get_volume(), 48)

    def test_cube_creation(self):
        cube = Cube(Point(1, 2), Point(4, 6))
        self.assertEqual(cube.get_width(), 3)
        self.assertEqual(cube.get_height(), 4)
        self.assertEqual(cube.get_area(), 12)
        self.assertEqual(cube.get_volume(), 48)

    def test_move_shape(self):
        rectangle = Rectangle(Point(3, 3), Point(100, 100))
        ShapeManager.move_shape(rectangle, Point(1, 1), Point(100, 30))
        self.assertEqual(rectangle.top_left.x, 4)
        self.assertEqual(rectangle.top_left.y, 4)
        self.assertEqual(rectangle.bottom_right.x, 200)
        self.assertEqual(rectangle.bottom_right.y, 130)

    def test_move_shape_not_equal(self):
        rectangle = Rectangle(Point(3, 3), Point(100, 100))
        ShapeManager.move_shape(rectangle, Point(1, 1), Point(100, 30))
        self.assertNotEqual(rectangle.top_left.x, 3)
        self.assertNotEqual(rectangle.top_left.y, 3)
        self.assertNotEqual(rectangle.bottom_right.x, 100)
        self.assertNotEqual(rectangle.bottom_right.y, 100)
