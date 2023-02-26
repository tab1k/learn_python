class Point:
    color = 'Red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point()
pt.set_coords(1, 2)  # вызываем функцию которая стоит в классе Point as pt
print(pt.__dict__)  # функция __dict__ выводит координаты в словаре
