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



