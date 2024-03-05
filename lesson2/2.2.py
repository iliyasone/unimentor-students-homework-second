n = int(input())

# "2 3 1" -- split() -> ['2', '3', '1']
# ['2', '3', '1'] -- map(int, ...) -> [2, 3, 1]

result = []
for _ in range(n):
    x, y, z = map(int, input().split())
    result.append((x, y, z))
    
print(result)