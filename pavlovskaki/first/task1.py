"""
Користувач вводить дані. Завдання: вивести усі слова цього тексту, що містять велику букву, у вигляді списку.
"""

story = input()
r = []
y = []
for i in range(len(story)):

    if story[i] != " ":
        r.append(story[i])
    else:
        for j in range(len(r)):
            if r[j] in "QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ":
                y.append(r)
                r = []
                break
        r = []
print(y)
