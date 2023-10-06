class Student:
    def __init__(self, LF, group_number, grade, number_on_the_list, arithmetic_mean_mark):
        self.LF = LF
        self.group_number = group_number
        self.grade = grade
        self.number_on_the_list = number_on_the_list
        self.arithmetic_mean_mark = arithmetic_mean_mark
    def print_info(self):
        print(f'Фамилия Имя: {self.LF}\nНомер группы: {self.group_number}\nУспеваемость: {self.grade}\nНомер в списке: {self.number_on_the_list}\nСредняя арифметическая отметка: {self.arithmetic_mean_mark}')
students = []
for i in range(10):
    print(f'\nВведите данные о студенте: {i+1}')
    LF = input("Фамилия Имя: ")
    group_number = input("Номер группы: ")
    grade = input("Успеваемость: ")
    number_on_the_list = input("Номер в списке: ")
    arithmetic_mean_mark = input("Средняя арифметическая отметка: ")
student_1 = Student('Mariya Luzhinskaya', 'PO-21', 'very good', '13', '8,8')
students.append(student_1)
for student in students:
    student_1.print_info()
