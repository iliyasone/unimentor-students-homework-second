alphabet = {
    "к" : "т",
    "р" : "а",
    "и" : "к",
    "в" : "л",
    "о" : "у",
    "я" : "ч",
    "з" : "ш",
    "ы" : "е",
}
text = input("Введите текст ")
new_text = ''.join(alphabet.get(char, char) for char in text)
print(new_text)