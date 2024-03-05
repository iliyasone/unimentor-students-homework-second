def get_initials(full_name):
    parts = full_name.split()
    last_name = parts[0]
    initials = last_name
    if len(parts) == 3:
        first_name = parts[1]

        patronymic = parts[2]
        initials += ' ' + first_name[0] + '.' + patronymic[0] + '.'
    elif len(parts) == 2:
        first_name = parts[1]
        initials += ' ' + first_name[0] + '.'

    return initials
full_name = input("Введите своё ФИО ")

print(get_initials(full_name))
