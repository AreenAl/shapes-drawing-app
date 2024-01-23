class Rectangle:
    def __init__(self, top_left ,bottom_right):
        self.top_left=top_left
        self.bottom_right=bottom_right

    def get_width(self):
        return self.bottom_right.x-self.top_left.x

    def get_height(self):
        return self.bottom_right.y-self.top_left.y

    def get_area(self):
        return self.get_width()*self.get_height()

    def __repr__(self):
        return f"Rectangle({self.top_left}, {self.bottom_right})"


