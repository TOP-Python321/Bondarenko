email = input().strip()

if "@" in email and "." in email[email.index("@"):]:
    print("да")
else:
    print("нет")
    
# sjjowfijwij@.ru
# да

# trhuowrgoureg@ru
# нет

