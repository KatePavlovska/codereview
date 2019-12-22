"""
Дано список. Завдання: вивести суму усіх парних і непарних елементів цього списку.
"""
array = []
s1 = 0
s2 = 0
for i in range(1, len(array), 2):
    s1 += array[i-1]
    s2 += array[i]

if len(array) % 2 == 1:
    s1 += array[-1]

print(array)
