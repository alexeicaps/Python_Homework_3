# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3


# N = abs(int(input('Введите количество элементов списка А: ')))
# print(N)
# A_entered = input("Введите через пробел элементы списка: ").split()
# print(A_entered, type(A_entered))
# A_num = list(map(int, A_entered))
# print(A_num, type(A_num))
# if len(A_num) != N:
#     print('Введенные элементы не соответствуют заявленному количеству!')
# else:
#     X = int(input('Введите число X, которое необходимо найти в списке: '))
#     count = 0
#     for i in range(N):
#         if A_num[i] == X:
#             count += 1
#     print(f'Число {X} встречается в списке A {count} раз')


list_1 = [1, 3, 3, 2, 3, 4, 5, 3, 3]
k = 3
print(list_1.count(k))


