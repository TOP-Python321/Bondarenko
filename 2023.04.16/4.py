cell1 = input("Введите координаты первой клетки: ")
cell2 = input("Введите координаты второй клетки: ")

if (ord(cell1[0]) + int(cell1[1])) % 2 == (ord(cell2[0]) + int(cell2[1])) % 2:
    print("да")
else:
    print("нет")


# Введите координаты первой клетки: g1
# Введите координаты второй клетки: e6
# нет

# Введите координаты первой клетки: f1
# Введите координаты второй клетки: b5
# да


# ИТОГ: отлично — 5/5
