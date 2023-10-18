punctuation = '.,:;!?–—\'\"()*/'   

text = input()
new_text = ''.join([c for c in text if c not in punctuation])
print(new_text)

# Код: работает, исправно.
# Код работает исправно

