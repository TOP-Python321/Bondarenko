message = input()  


cost = len(message.replace(' ', '')) * 0.3

print(f"{int(cost // 1)} руб. {int(cost % 1 * 100)} коп.")

# код работает исправно
# 5 руб. 70 коп.

