# @staticmethod - с помощью этого декоратора , мы можем определить методы которые не имеют доступа ни к аттрибутам класса, ни к аттрибутам его экземпляров
# т.е. создается самостоятельная - независимая функция , объявленная внутри класса

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

        print(self.square_norm(self.x, self.y), '@staticmethod')

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def square_norm(x,y): # заметьте что тут нет "self"
        return f"Квадрат нормы равняется - {x*x + y*y}" #уравнение квадрата нормы


v = Vector(1, 101)
res = v.get_coord()
print(res)
print(v.validate(5), '@classmethod')
print(v.square_norm(5,6), '@staticmethod')
