class Point:
    color = 'Red'
    circle = 2


    def __init__(self, x, y):
        print('Вызов __init__')
        self.x = x
        self.y = y



pt = Point(1,2)
print(pt.__dict__)


a = pt.__dict__
for k, v in  a.items():
    print(k,v)





