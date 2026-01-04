# Задание 4.1 Напишите код для функций sum
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total
# Рекурсивная функция,
#  где используется срез по строкам время выполнения O(n)
def recurSum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recurSum(arr[1:])
    
# удалены срезы добавлен start = 0 для индексаций,
#   что экономит память время выполнения O(1)

def recurSum(arr,start=0):
    if start >= len(arr):
        return 0
    return arr[start] + recurSum(arr,start + 1)

# Напишите рекурсивную функцию для подсчета элементов в списке.
# Время выполнение O(n)
def sumLen(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + sumLen(arr[1:])

def highNumberInList(arr):
    if not arr :
        return 0
    if len(arr) == 1:
        return arr[0]
    return max(arr[0], highNumberInList(arr[1:]))

print(highNumberInList([1,2,3,4]))




