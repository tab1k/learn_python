''' OLympiad Solutions '''
def sport():



    dict = {
        'first' : 'первым',
        'second' : 'вторым',
        'third' : 'третий',
        'fourth' : 'четвертый',
        'fifth' : 'пятый',
    }

    list2 = [1,2,3,4,5]

    list = []
    count_sportsmen = int(input('Кол-во участников: '))
    for i in str(count_sportsmen):
        while len(list) != count_sportsmen:
            for key in dict.values():
                a = int(input(f'Введите кто пришел {key}: '))
                list.append(a)
                if len(list) == str(count_sportsmen):
                    continue



    if list == list2:
        print('Все заняли места по их нумерации!')

    elif list != list2:
        total = []
        for ch in list:
            total.append(ch)
        print(total)



    else:
        #for change in list:
            #total = [change]
        print('Список пришедших к финишу: ', list)
        #print(total)




sport()
