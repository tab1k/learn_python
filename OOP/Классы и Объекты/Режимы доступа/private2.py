# PRIVATE MODE 2
import private as private


class Point:

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Кординаты должны быть числами!')

    def get__cord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get__cord())
print(dir(pt))
print(pt.__dict__.items())

for k,v in pt.__dict__.items():
    print(f'Класс {k}, и ответ его {v}')
# print(pt.__x, pt.__y)
