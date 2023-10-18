year = int(input("Введите год: "))

if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print("Да")
else:
    print("Нет")


# Введите год: 2016
# Да


# ИТОГ: отлично — 3/3
