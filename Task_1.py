# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1

import random

# n = int(input("Введите начальное число диапазона: "))
# # m = int(input("Введите конечное число диапазона: "))
# list_1 = [1, 2, 3, 4, 5]
# k = int(input("Type a number: "))
# count = 0
# for i in list_1:
#     if k == list_1[i]:
#         count += 1
#     else:
#         print("Числа {k} в списке нет.")
# print(f"Число {k} встречается {count} раз)




# data = {}
# data_second = dict()
#
# data["John"] = 23
# data["Kate"] = 20
# print(data["John"])
# print(list(data.keys()))
# print(list(data.values()))
#
# for i in data.keys():   # <-> data:
#     print(i)
#
# for i in data.values():
#     print(i, end=' ')


# Task 21

data = [{"V": "S001"}, {"V": "S002"},
         {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {"V":"S009"},
             {"VIII":"S007"}]
set_values = set()
print(data[5])

for i in data:
    print(i)
    set_values.add(i.values()[0])
print(set_values)