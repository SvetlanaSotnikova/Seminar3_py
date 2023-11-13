# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1

size = int(input("Input size of array: "))
list = []

for el in range(size):
    number = int(input(f"Input element {el + 1}: "))
    list.append(number)
print(f"list = [{', '.join(map(str, list))}]")

number = int(input("Enter the number you want to know the quantity of: "))

count = list.count(number)

print(f"\nCount of number {number}: {count}")


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# result = 5

size = int(input("Input size of array: "))
list = []

for el in range(size):
    number = int(input(f"Input element {el + 1}: "))
    list.append(number)
print(f"list = [{', '.join(map(str, list))}]")

number = int(input("Input number: "))

result_number = min(list, key=lambda X: abs(X - number))

# # closest_difference = abs(list[0] - number)
# # closest_element = list[0]

# # for el in list:
# #     diffrence = abs(el - number)
# #     if diffrence < closest_difference:
# #         closest_difference = diffrence
# #         closest_element = el
        
# # print(closest_element)

print(result_number)

# Задача 20 В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

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
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Пример:
# k = 'ноутбук'
# # 12

russion_points = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10
}
english_points = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

word = input("input word: ")

word = word.upper()

score = 0

if word[0] in english_points:
    scores = english_points
else:
    scores = russion_points

for letter in word:
    if letter in scores:
        score += scores[letter]

print(f'point: {score}')