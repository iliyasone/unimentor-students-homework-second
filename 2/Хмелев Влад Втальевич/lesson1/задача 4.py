n = int(input())
f = 0
for i in range(n):
    a = input()
    b = int(input())
    c = {"яблоки": 52, "бананы": 89, }
    if a in c:
        x = c [a] * b * 10
        f += x
print(f)
