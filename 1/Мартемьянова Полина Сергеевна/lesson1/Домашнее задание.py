#1
name = 'Valerii'
lastname = ' Yartsev'
a = name + lastname
print("Добро пожаловать в Полиннос," + a +"!")
#2
name = "SashaSashaSashaSasha"
name2 = "Sasha"
if name == name2 * 4:
    print("True")
else:
    print("False")
    
#3
apples = 52
bananas = 89
tomatoes = 24
product = input("Введите название продукта: ").lower()
weight = int(input("Введите вес в кг: "))
if product == 'яблоки':
    n = apples * 10 * weight
elif product == 'бананы':
    n = bananas * 10 * weight
else:
    n = tomatoes * 10 * weight
print(n)


    
    










    