def give_license(student_id):
    """
    Проверяет наличие студента с данным id в базе данных

    :param student_id: индификационный номер студента
    :return: True если студент есть в базе и ему можно выдавать лицензию, иначе False
    """
    global students
    for student in students:
        if student["id"] == student_id:
            return True
    return False

students=[
    {"id": 367673, "full_name": "ЯрцевВалерийРустэмович"},
    {"id": 563234, "full_name": "ШиптенкоВиталийПрограммирович"},
    {"id": 982123, "full_name": "ДатабейзовИванДжетлагович"},
]

student_id = int(input("Введите id студента "))
print(give_license(student_id))