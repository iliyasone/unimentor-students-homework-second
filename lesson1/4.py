n = int(input())
result = 0
for _ in range(n):
    food = input()
    weigth = int(input()) # in put

    if food == 'яблоки':
        result += weigth*52*10
    elif food == 'бананы':
        result += weigth*89*10
    elif food == 'помидоры':
        result += weigth*24*10
print(result)