n = int(input("Количество приемов пищи: "))
total_cal = 0
for i in range(n):
    fruit = input("Название продукта (яблоки, бананы или помидоры): ")
    weight = int(input("Масса продукта в килограммах: "))
    
    if fruit == "яблоки":
                cal = 520
    elif fruit == "бананы":
                cal = 890
    elif fruit == "помидоры":
                cal = 240

    total_cal += weight * cal
print("Общее количество калорий:", total_cal)
input("Для выхода нажмите Enter")
