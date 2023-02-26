# @classmethod - метод который помогает получить доступ к встроенным аттрибутам класса, в нашем случае нашим классом является Vector

class Vector:

    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):  # or Vector
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y


v = Vector(1, 101)
res = v.get_coord()
print(res)
print(v.validate(5))
