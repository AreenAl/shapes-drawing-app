from box import Box
class Cube(Box):
    def __repr__(self):
        return f"Cube({self.top_left}, {self.bottom_right})"
