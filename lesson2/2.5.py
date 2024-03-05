n = int(input())
students: dict[tuple[int, int, int], set[int]] = dict()


for _ in range(n):
    x, y, z, k = map(int, input().split())
    coordinates = (x, y, z)
    
    if coordinates not in students.keys():
        students[coordinates] = {k}
    else:
        students[coordinates].add(k)
        
for coordinates, contests in students.items():
    print(*coordinates, *contests)