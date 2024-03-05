full_name = input("Введите своё ФИО ")

def get_initials(full_name):
    parts = full_name.split()
    last_name = parts[0]
    initials = last_name
    for part in parts[1:]:
        initials += ' ' + part[0] + '.'

    return initials

print(get_initials(full_name))
