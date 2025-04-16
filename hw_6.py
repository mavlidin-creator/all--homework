from random import randint, choice

Arr = [randint(1, 100) for i in range(15)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def binary_search(a, x):
    n = len(a)
    ResultOk = False
    first = 0
    last = n - 1
    pos = -1

    while first <= last:
        middle = (first + last) // 2
        val = a[middle]

        if val == x:
            ResultOk = True
            pos = middle
            break
        elif val > x:
            last = middle - 1
        else:
            first = middle + 1

    if ResultOk:
        print(f"Элемент {x} найден на индексе {pos}")
        return pos
    else:
        print(f'Элемент {x} не найден')
        return -1
print(f'Не отсартированная строка: {Arr}')
sorted_list = bubble_sort(Arr)
print("Отсортированный список: ", sorted_list)
v = choice(sorted_list)
print(f'Искомый элемент: {v}')
binary_search(sorted_list, v)
