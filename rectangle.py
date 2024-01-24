class Rectangle:
    def __init__(self, top_left ,bottom_right):
        if top_left.x<0 or top_left.y<0 or bottom_right.x>2240 or bottom_right.y>1080 :
            raise ValueError
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


