n = int(input("Введите количество грибов "))
if n < 0:
    print("ERROR")
k = int(input("Введите номер гриба "))
if k < 0 or k > n:
    print("ERROR")
chi = list(map(int, input("Введите вес грибов собранный чижиком ").split()))
pyzhik = list(map(int, input("Введите вес грибов собранный пыжиком ").split()))
kseniya = list(map(int, input("Введите вес грибов собранный Ксенией ").split()))
chi_k = chi[k-1]
pyzhik_k = pyzhik[k-1]
ksusha_k = kseniya[k-1]
if chi_k > pyzhik_k and chi_k > ksusha_k:
    print("Чижик")
elif pyzhik_k > chi_k and pyzhik_k > ksusha_k:
    print("Пыжик")
elif ksusha_k > chi_k and ksusha_k > pyzhik_k:
    print("Ксения")
else:
    print("Ничья")