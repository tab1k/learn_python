class Point:
    color = 'red' #переменные внутри класса называют аттрибутами класса или его свойствами
    circle = 2


p = Point() # переменная p -> является экземпляром класса Point
t = Point()
print(p) #функция __dict__ вытаскивает все атрибутты класса
print(t)

Point.pt = 'Square'
print(p,t)

Point.pt
print()





