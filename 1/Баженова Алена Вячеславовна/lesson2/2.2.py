n = int(input("Введите количество ежей "))
my_list = []
for _ in range(n):
    x, y, z = map(int, input("Введите координаты ежа ").split())
    my_list.append((x, y, z))

print(my_list)