word = input()

valid_chars = {"0", "1"}

if (word.startswith("0b") and all(char in valid_chars for char in word[2:]) or
    word.startswith("b") and all(char in valid_chars for char in word[1:]) or 
    all(char in valid_chars for char in word)):
    print("да")
else:
    print("нет")
    


# 0b10110
# да

# 1b11010
# нет

