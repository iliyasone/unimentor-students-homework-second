cal_apples = int(520)
cal_bananas = int(890)
cal_tomatoes = int(240)
cal = 0
fruit = input("Съеденный фрукт: ")
weight = int(input("Масса: "))
if fruit == "яблоки":
    cal = cal_apples * weight
    print(cal)
elif fruit == "бананы":
    cal = cal_bananas * weight
    print(cal)
else:
    cal = cal_tomatoes * weight
    print(cal)
input("Нажмите Enter для выхода")
