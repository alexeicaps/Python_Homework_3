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

# k = 'ящерица'
# our_dict = {'A, E, I, O, U, L, N, S, T, R, А, В, Е, Ё, И, Й, Н, О, Р, С, Т': 1,
#             'D, G, Д, К, Л, М, П, У': 2,
#             'B, C, M, P, Б, Г, Ё, Ь, Я': 3,
#             'F, H, V, W, Y, Й, Ы': 4,
#             'K, Ж, З, Х, Ц, Ч': 5,
#             'J, X, Ш, Э, Ю': 8,
#             'Q, Z, Ф, Щ, Ъ': 10}
#
# a = k.upper()
# # print(a)
# # word = input("Type a word: ").upper()
# result = 0
# for char in a:
#     for key in our_dict:
#         if char in key:
#             result += our_dict[key]
# print(result)


# два словаря

eng = 'qwertyuiopasdfghjklzxcvbnm'

rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

list_English = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP',
                4: 'FHVWY', 5: "K", 8: 'JX', 10: 'QZ'}
list_Russian = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ',
                4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}

word = input('Введите слово на русском или английском языке: ')

if word[0].lower() in eng:
    summa_1 = 0
    for letter in word:
        for key, value in list_English.items():
            if letter.upper() in value:
                summa_1 += key
    print(f'стоимость введенного английского слова = {summa_1}')
else:
    if word[0].lower() in rus:
        summa_2 = 0
        for letter in word:

            for key, value in list_Russian.items():
                if letter.upper() in value:
                    summa_2 += key
    print(f'стоимость введенного русского слова = {summa_2}')






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