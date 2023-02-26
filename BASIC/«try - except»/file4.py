a = int(input('Введите число: '))
b = int(input('Введите число: '))
try:
    x = a / b


except ZeroDivisionError:
    print('На ноль делить нельзя!')

else:
    print('Ответ', x)

finally:
    print('Программа закончилась!')