#PRIVATE MODE

class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Кординаты должны быть числами!')

    def get__cord(self):
        return self.__x, self.__y


pt = Point(1,2)
pt.set_coord(10,20)
print(pt.get__cord())
#print(pt.__x, pt.__y)