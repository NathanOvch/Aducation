#3

tyu = int(input("Введіть число"))
if tyu == 0:
    print("число дорівнює нулю")
elif tyu >= 0:
    print("число більше нуля")
elif tyu <= 0:
    print("число меньше нуля")

#1

day = int(input('Введіть номер дня тижня'))
if day == 1:
    print("Понеділок")
elif day == 2:
    print("Вівторок")
elif day == 3:
    print("Середа")
elif day == 4:
    print("Четвер")
elif day == 5:
    print("П'ятниця")
elif day == 6:
    print("Субота")
elif day == 7:
    print("Неділя")

#3

moon = int(input('Введіть номер місяця року'))
if moon == 1:
    print("Січень")
elif moon == 2:
    print("Лютий")
elif moon == 3:
    print("Березень")
elif moon == 4:
    print("Квітень")
elif moon == 5:
    print("Травень")
elif moon == 6:
    print("Червень")
elif moon == 7:
    print("Липень")
if moon == 8:
    print("Серпень")
elif moon == 9:
    print("Вересень")
elif moon == 10:
    print("Жовтень")
elif moon == 11:
    print("Листопад")
elif moon == 12:
    print("Грудень")

#4

a = int(input('Введіть число'))
b = int(input('Введіть число'))
if a == b:
    print("Вони рівні")
elif a >= b:
    print(a > b)
elif a <= b:
    print(a < b)
