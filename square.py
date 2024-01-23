from rectangle import Rectangle
class Square(Rectangle):
    def __repr__(self):
        return f"Square({self.top_left}, {self.bottom_right})"
