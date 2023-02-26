a = int(input('Введите число: '))
b = int(input('Введите число: '))
try:
    x = a / b
    print(x)

except ZeroDivisionError:
    print('На ноль делить нельзя!')