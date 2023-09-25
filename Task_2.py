# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

# data = [int(input(f'Enter {i + 1} element: ')) for i in range(int(input('Enter array size: ')))]
# x = int(input('Enter comparison value '))
list_1 = [2, 16, 9, 32, 25]
k = 12
number = list_1[0]
diff = k - number
for i in list_1:
    if abs(k - i) < diff:
        diff = k - i
        if diff < 0:
            diff = diff * (-1)
        number = i
print(number)