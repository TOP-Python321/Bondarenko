def countable_nouns (num: int, words: tuple):
    last_digit = num % 10

    if last_digit not in [1,2,3,4] or num % 100 in [11,12,13,14]:
        return words[2]
    elif last_digit == 1:
        return words [0]
    else:
        return words[1]


