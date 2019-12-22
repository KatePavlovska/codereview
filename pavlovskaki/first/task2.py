"""
Задано список. Завдання: вивести кількість порожніх списків, які він містить.
"""
word = input("Введіть кількість елементів списку")
newlist = []
count = 0
for i in range (word):
    newlist[i] = input("Vvedit" + str(i+1) + "element spisky").split("")
    if newlist[i] == []:
        count=+1
print("")