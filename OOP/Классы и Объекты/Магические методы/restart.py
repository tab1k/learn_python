class Point:
    MIN_COORD = 0
    MAX_COORD = 100


    def __init__(self, x, y):
        self.x = x
        self.y = y


    def set_coords(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
        else:
            print('OUPS...')

    def get_coords(self):
        return self.x, self.y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left


pt = Point(101,2)
pt.set_bound(-100)
print(pt.MAX_COORD)
print(pt.__dict__)
print(Point.__dict__)