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

    def __getattribute__(self, item): #item -> аттрибут к которому идет обращение
        if item == 'x':
            raise  ValueError('Доступ запрещен')
        else:
            print('__getattribute__')
            return object.__getattribute__(self,item)


pt = Point(101,2)
a = pt.y
print(a)