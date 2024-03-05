def fibonacci(k):
    if k == 1:
        return 0
    elif k == 2:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)

# Считываем количество чисел Фибоначчи, которые нужно вычислить
n = int(input())

# Считываем порядковые номера чисел Фибоначчи и выводим соответствующие значения
for _ in range(n):
    k = int(input())
    print(fibonacci(k))