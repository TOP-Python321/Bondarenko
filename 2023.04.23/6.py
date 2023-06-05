ticket_number = input("Введите номер билета: ")

if (sum(int(digit) for digit in (ticket_number[:3])) == 
    sum(int(digit) for digit in(ticket_number[3:]))):
    print("Да")
else:
    print("Нет")


# Введите номер билета: 561822
# Да

# Введите номер билета: 341511
# Нет

