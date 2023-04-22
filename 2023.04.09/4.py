num = int(input("Введите число"))

# КОММЕНТАРИЙ: цифра — digit, число — number, num
num1 = num // 100
num2 = (num // 10) % 10
num3 = (num // 100) % 10

# КОММЕНТАРИЙ: избыточные переменные summary и multiply
# КОММЕНТАРИЙ: сумма (матем.) — sum, произведение (матем.) — product
summary = num1 + num2 + num3
multiply = num1 * num2 * num3

print(f"Сумма цифр = {summary} \n"
      f"Произведение цифр = {multiply}")


# Сумма цифр = 15
# Произведение цифр = 125


# ИТОГ: отлично — 4/4
