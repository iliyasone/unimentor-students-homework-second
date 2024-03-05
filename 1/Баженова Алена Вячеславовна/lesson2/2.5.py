n = int(input("Введите количество отправленных работ"))
students = {}
for _ in range(n):
    x, y, z, k = map(int, input("Введите координаты и номер контрольной").split())
    coordinates = (x, y, z)
    if coordinates not in students:
        students[coordinates] = set()
    students[coordinates].add(k)
for coordinates, works in students.items():
    print(*coordinates, *works)
