# # Task 1
# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# number = int(input("Input size of array: "))
# list = []
# result_list = []

# for i in range(number):
#     n = int(input(f"input element {i + 1}: "))
#     list.append(n)
    
# for num in list:
#     if num not in result_list:
#         result_list.append(num) 

# print(f'your list: {list}')
# print(f'result list: {result_list}, \ncount elements = {len(result_list)}')

# # print(f'result list: {result_list}, \ncount elements = {set(len(result_list))}

#Task 2
# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# number = int(input("Input size of array: "))
# list = []
# result_list = []

# for i in range(number):
#     n = int(input(f"input element {i + 1}: "))
#     list.append(n)
# print(f"your list: {list}")

# k = int(input('\nInput number for shift: '))

# if k < 0 or k > number:
#     print("wrong value :(")
# else:
#     k = k % number
#     result_list = list[k:] + list[:k]

# print(f'\nresult list: {result_list}')

#Task 3
# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# list = [
#     {"V": "S001"},
#     {"V": "S002"},
#     {"VI": "S001"},
#     {"VI": "S005"},
#     {"VII": " S005 "},
#     {" V ":" S009 "},
#     {" VIII ":" S007 "}
# ]

# result_value = set()

# for dic in list:
#     for value in dic.values():
#         result_value.add(value.strip())

# print(result_value)

#Task 4
# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# number = int(input("input size of array: "))
# arr = []
# for i in range(number):
#     n = int(input(f"input element {i + 1}: "))
#     arr.append(n)
# print(f"\nyour list: {arr}")

# count = 0
# result_arr = []
# for i in range(1, len(arr)):
#     if arr[i - 1] < arr[i]:
#         count += 1
#         result_arr.append(f'{arr[i - 1]} < {arr[i]}')

# print(f'{count} -> ({", ".join(map(str, result_arr))})')