def super_name_initals(name: str, *names: str):
    for second_name in names:
        name += ' ' + second_name[0] + '.'
        
    return name    
    
print(super_name_initals(*input().split()))