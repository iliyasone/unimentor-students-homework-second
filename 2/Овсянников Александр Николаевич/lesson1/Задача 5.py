max_weight = 50
total_weight = 0
purchases = 0

while True:
    weight = int(input("Введите вес продукта в килограммах (для завершения программы введите 0): "))
            
    if weight == 0:
        break

    if total_weight + weight > max_weight:
        print("Превышена максимальная масса покупки.")
        continue

    total_weight += weight
    purchases += 1

    print("Общий вес продуктов, кг:", total_weight)
    print("Количество сделанных покупок:", purchases)
