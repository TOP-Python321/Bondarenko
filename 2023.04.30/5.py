scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}


word = input().upper()
word = word.replace("Ё", "Е")

score = 0
for letter in word:
    for key, value in scores_letters.items():
        if letter.upper() in value:
            score += key
            break
            
print(score)

# явление
# 10

