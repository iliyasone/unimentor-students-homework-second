n = int(input())
k = int(input())
chizhik = list(map(int, input().split()))
pyzhik = list(map(int, input().split()))
ksenia = list(map(int, input().split()))

chizhik.sort(reverse=True)
pyzhik.sort(reverse=True)
ksenia.sort(reverse=True)

chizhik_k = chizhik[k - 1]
pyzhik_k = pyzhik[k - 1]
ksenia_k = ksenia[k - 1]

if chizhik_k > pyzhik_k and chizhik_k > ksenia_k:
    winner = "Чижик"
elif pyzhik_k > chizhik_k and pyzhik_k > ksenia_k:
    winner = "Пыжик"
elif ksenia_k > chizhik_k and ksenia_k > pyzhik_k:
    winner = "Ксюша"
else:
    winner = "Ничья"

print(winner)