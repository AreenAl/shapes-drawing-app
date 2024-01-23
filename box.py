from rectangle import Rectangle
class Box(Rectangle):

    def get_volume(self):
        return self.get_area() * (self.bottom_right.y - self.top_left.y)

    def __repr__(self):
        return f"Box({self.top_left}, {self.bottom_right})"

