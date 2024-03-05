n = int(input())
k = int(input())


# split : "1 2 3 4 5" -> ["1", "2", "3", "4", "5"]
# map :           int -> ["1", "2", "3", "4", "5"]
# list                   [1, 2, 3, 4, 5]

chizik = list(map(int, input().split()))
pizik = list(map(int, input().split()))
ksenia = list(map(int, input().split()))

chizik.sort()
pizik.sort()
ksenia.sort()
if chizik[k] > pizik[k] and chizik[k] > ksenia[k]:
    print("Чижик")
elif pizik[k] > chizik[k] and pizik[k] > ksenia[k]:
    print("Пыжик")
elif ksenia[k] > pizik[k] and ksenia[k] > chizik[k]:
    print("Ксюша")
else:
    print("Ничья")

print(chizik, pizik, ksenia)







# chizik = input().split()
# for i in range(n):
#     chizik[i] = int(chizik[i])
    

# chizik = [int(d) for d in input().split()]
# списковые включения, list-comprehensions
