num1 = input("Введите целую часть ")
num2 = input("Введите дробную часть ")

coef = 1.61
mile = float(f"{num1}.{num2}") 
km = mile * coef

print(f"{mile} миль = {km:.1f} км ")


# 50.5 миль = 81.3 км
