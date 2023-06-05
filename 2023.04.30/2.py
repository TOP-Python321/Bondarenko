fruits = []

while True:
    fruit = input()
    if not fruit:
        break
    fruits.append(fruit)
    

if len(fruits) == 1:
    print(fruits[0])
else:
    joined_fruits = ", ".join(fruits[:-1])
    result = f'{joined_fruits} и {fruits[-1]}'
    print(result)
    
    
# лимон

# лимон

# лимон
# груша
# яблоко

# лимон, груша и яблоко

