TrueNumber = ''
while TrueNumber != 7:
    TrueNumber = input('Угадай число: ')
    TrueNumber = int(TrueNumber)

    if TrueNumber > 7:
        print('Меньше')
    elif TrueNumber < 7:
        print('Больше')
    else:
        print('Угадал')
        break
