count = 0
bought = 0
while True:
    try:
        a = int(input())
        if count + a > 50:
            break
        count+=a
        bought += 1
    except:
        break
print(count)
print(bought)

