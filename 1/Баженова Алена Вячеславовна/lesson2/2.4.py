n = int(input("Введите количество студентов"))
k = int(input("Введите количество сочинений"))
essay_counts = {}
for _ in range(n):
    essays = input().split()
    for essay in essays:
        essay_counts[essay] = essay_counts.get(essay, 0) + 1

duplicate_essays = [essay for essay, count in essay_counts.items() if count == n]
print(" ".join(duplicate_essays))
