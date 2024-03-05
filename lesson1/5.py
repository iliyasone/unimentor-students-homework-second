weight = 0
count = 0
new_item = int(input())

while weight + new_item <= 50:
    weight += new_item
    count += 1
    new_item = int(input())
    
print(weight)
print(count)
    
    