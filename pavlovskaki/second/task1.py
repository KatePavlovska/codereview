"""
Користувач вводить рядок, що містить римський запис числа. Напишіть функцію, що повертає це число у арабському записі. Виведіть результат.
У випадку помилкового вводу виведіть повідомлення про помилку.
(Римські позначення цифр: M=1000, D=500, C=100, L=50, X=10, V=5, I=1. Жоден символ не може повторюватися понад 3 рази підряд.)
"""
def function(a):
    number = input("Input number")
    try:
        number=int(number) and number < 4000
    except ValueError:
        print("Вводьте лише цифри")
#Перевірка через Try except  на коректність введених даних
#Пробігаємо for
    number = list(number)
    for i in range(number):
        if i==1:
            i.__init__("I")
        if i==2:
            i.__init__("II")
        if i == 3:
            i.__init__("III")
        if i == 4:
            i.__init__("IV")
        if i == 5:
            i.__init__("V")
        if i == 6:
            i.__init__("VI")
        if i == 7:
            i.__init__("VII")
        if i == 8:
            i.__init__("IIX")
        if i == 9:
            i.__init__("IX")
        if i == 10:
            i.__init__("X")
    print(number)
#Заміна відповідно 1 на І і тд


#Другий варіант, адже 1 працює лише в деяких випадках
def function_1(b):
    number = input("Input number")
    try:
        number=int(number) and number < 4000
    except ValueError:
        print("Вводьте лише цифри")
#Перевіряємо на коректність
    k=number/10
    s=number%10
    k1=k*"X"
    if k>3:
        print("Один символ тільки повторюється 3 рази")
    s1=s*"I"
    if s>3:
        print("Один символ тільки повторюється 3 рази")
    k1=str(k1)
    s2=str(s1)
    number1=k1+s2
# для змінної к знаходиться кількісмть десятків(сотень.тисяч), для s кількість одиниць. Потім перетворюємо в string і додаємо.