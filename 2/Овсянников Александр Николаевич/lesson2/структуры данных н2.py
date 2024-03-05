n = int(input())
hedgehog_coordinates = []

for i in range(n):
    coordinates = tuple(map(int, input().split()))
    hedgehog_coordinates.append(coordinates)

print(hedgehog_coordinates)
