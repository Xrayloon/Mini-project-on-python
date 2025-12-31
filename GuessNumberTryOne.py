TrueNumber = ''
while TrueNumber != 7:
    TrueNumber = int(input('Угадай число: '))
    

    if TrueNumber > 7:
        print('Меньше')
    elif TrueNumber < 7:
        print('Больше')
    else:
        print('Угадал')
        break
