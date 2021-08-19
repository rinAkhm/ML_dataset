from file_list_of_student import WorkList
from Services.Manage_data import MergeData
from Services.Service2 import ServiceSearchStudentByEmail
from Services.Service1 import ServiceGetStudentGradeByToken

# Получаем список студентов
save_student = WorkList()
manage = MergeData()
service1 = ServiceGetStudentGradeByToken()
service2 = ServiceSearchStudentByEmail()

"""получаем из файла список всех студентов"""
students = save_student.read_file()

"""через 2 сервис собираем все токены"""
tokens = service2.get_data_from_service(students=students)

"""формируем сводную таблицу и записываем в ней оценки"""
pivot = service2.pivot(tokens)
service1.get_grade(pivot)
# service1.clear_grades(pivot)

"""получаем список курсов"""
courses = service1.get_course(pivot)

"""создаем таблицу в exele"""
manage.merge_dict(pivot, set(tokens), courses)
