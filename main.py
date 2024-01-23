from point import Point
from rectangle import Rectangle
from cube import Cube
from square import Square
from box import Box

class ShapeManager:
    @staticmethod
    def move_shape(shape, shift_top_left, shift_bottom_right):
        new_top_left_x = shape.top_left.x + shift_top_left.x
        new_top_left_y = shape.top_left.y + shift_top_left.y
        new_bottom_right_x = shape.bottom_right.x + shift_bottom_right.x
        new_bottom_right_y = shape.bottom_right.y + shift_bottom_right.y

        shape.top_left.x = max(0, min(new_top_left_x, 2240))
        shape.top_left.y = max(0, min(new_top_left_y, 1080))
        shape.bottom_right.x = max(0, min(new_bottom_right_x, 2240))
        shape.bottom_right.y = max(0, min(new_bottom_right_y, 1080))

def main():
    point = Point(3, 5)
    print(point)

    rectangle = Rectangle(Point(1, 2), Point(4, 6))
    print(rectangle.get_width())
    print(rectangle.get_height())
    print(rectangle.get_area())

    square = Square(Point(1, 2), Point(4, 5))
    print(square)

    box = Box(Point(1, 2), Point(4, 6))
    print(box)

    cube = Cube(Point(1, 2), Point(4, 6))
    print(cube)

if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
