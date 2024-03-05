alphabet = {
    'к': 'т',
    'р': 'а',
    'и': 'к',
    'в': 'л',
    'о': 'у',
    'я': 'ч',
    'з': 'ш',
    'ы': 'е'}

old_text = input()
new_text = ''

for letter in old_text:
    if letter in alphabet:
        new_text += alphabet[letter]
    else:
        new_text += letter

print(new_text)
