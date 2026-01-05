a = int(input('Первое число: ')) 
b = int(input('Второе число: '))
c = input('Тип операции (*, +, -, /): ')

if c == '/' and b == 0:
    print('На ноль делить нельзя!')
elif c == '/':
    print(a/b)
elif c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
else:
    print('Неверная операция')