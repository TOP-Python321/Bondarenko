num = int(input("Введите число"))

num1 = num // 100
num2 = (num // 10) % 10
num3 = (num // 100) %10

summary = num1 + num2 + num3
multiply = num1 * num2 * num3

print(f"Сумма цифр = {summary} \n"
f"Произведение цифр = {multiply}")

#Сумма цифр = 15
#Произведение цифр = 125
