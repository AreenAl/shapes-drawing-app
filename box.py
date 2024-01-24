from rectangle import Rectangle
class Box(Rectangle):
    def __init__(self,top_left,bottom_right,length):
        super().__init__(top_left ,bottom_right)
        self.length=length
    def get_volume(self):
        return self.get_area() * self.length

    def __repr__(self):
        return f"Box({self.top_left}, {self.bottom_right})"

