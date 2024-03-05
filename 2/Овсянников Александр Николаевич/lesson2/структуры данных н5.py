n = int(input())
students = {}

for i in range(n):
    x, y, z, k = map(int, input().split())
    coordinates = (x, y, z)

    if coordinates in students:
        students[coordinates].add(k)
    else:
        students[coordinates] = {k}

for coordinates, exams in students.items():
    print(*coordinates, *exams)
