n = int(input())
k = int(input())

all = set()

for i in range(n):
    student = set(input().split())

    if not all:
        all.update(student)
    else:
        all.intersection_update(student)

print(*all)3
