# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
#
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;

k = 'Ноутбук'
our_dict = {'A, E, I, O, U, L, N, S, T, R, А, В, Е, Ё, И, Й, Н, О, Р, С, Т': 1,
            'D, G, Д, К, Л, М, П, У': 2,
            'B, C, M, P, Б, Г, Ё, Ь, Ъ, Я': 3,
            'F, H, V, W, Y, Й, Ш, Щ, Ы': 4,
            'K, Ж, З, Х, Ц, Ч, Э, Ю': 5,
            'J, X, Ф': 8,
            'Q, Z': 10}

a = k.upper()
# print(a)
# word = input("Type a word: ").upper()
result = 0
for char in a:
    for key in our_dict:
        if char in key:
            result += our_dict[key]
print(result)









# dictionary = {1: 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т',
#               2: 'D, G, Д, К, Л, М, П, У',
#               3: 'B, C, M, P, Б, Г, Ё, Ь, Я',
#               4: 'F, H, V, W, Y, Й, Ы',
#               5: 'K, Ж, З, Х, Ц, Ч',
#               8: 'J, X',
#               10: 'Q, Z, Ф, Щ, Ъ'}
# word = str(input('Enter a word: ').upper())
#
# score = 0
# for char in word:
#     for key in dictionary:
#         if char in list(dictionary[key]):
#             score += key
#
# print(score)

# d = {
#     1 : 'one',
#     2 : 'two',
#     3 : 'three'
# }
# d[4] = 'four'
# print(d)
# d[5] = 'five'
# print(d)
# d[3] = 'три'
# print(d)

# person = {}
# s = 'john alen york sgu 1 2 3 4 5 6'
# s = s.split()
# person['lastname'] = s[0]
# print(person)

# d = {
#     1 : 'one',
#     2 : 'two',
#     3 : 'three'
# }
# d[4] = 'four'
# # print(d)
# for key in d:
#     print(key,':', d[key])