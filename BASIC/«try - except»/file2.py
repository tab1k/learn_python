x = 0
while x == 0:
    try:
        x = int(input('Введите число: '))
        x += 5
        print(x)
    except ValueError:
        print('Введите число!')