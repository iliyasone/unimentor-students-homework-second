n = int(input("Введите количество приёмов пищи "))
total_calories = 0
for n in range(1, n+1):
    a = str(input("Введите название продукта во множественном числе, с заглавной буквы "))
    p = int(input("Введите количество продукта в килограммах "))
    o = p * 1000
    y = "Яблоки"
    b = "Бананы"
    t = "Помидоры"
    if a == y:
        c = 52
        calories = o * c //100
        total_calories += calories
    elif a == b:
        c = 89
        calories = o * c //100
        total_calories += calories
    elif a == t:
        c = 24
        calories = c * o //100
        total_calories += calories
    else:
        print("Вы выбрали несуществующий продукт")
print(int(total_calories))

