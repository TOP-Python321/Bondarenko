numbers = []

while True:
    num = int(input("Введите число, кратное 7: "))
    if num % 7 != 0:
        break
    numbers.append(num)
    
    
result = " ".join(str(num) for num in reversed(numbers))
print(result)


# Введите число, кратное 7: 7
# Введите число, кратное 7: 14
# Введите число, кратное 7: 21
# Введите число, кратное 7: 57
# 21 14 7

