class Point:
    def __init__(self, x,y):
        if x<0 or y<0:
            raise Exception
        self.x=x
        self.y=y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

