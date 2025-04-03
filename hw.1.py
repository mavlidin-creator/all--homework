class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'ФИО: {self.full_name}\nВозраст: {self.age}\nСемейное положение: {self.is_married}')


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_mark(self):
        return sum(self.marks.values()) / len(self.marks)

    def introduce_myself(self):
        super().introduce_myself()
        for subject, mark in self.marks.items():
            print(f'{subject}: {mark}')
        print(f"Средний балл: {self.average_mark()}")


class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        salary = self.base_salary
        if self.experience > 3:
            for _ in range(self.experience - 3):
                salary += salary * 0.05
        return salary

    def introduce_myself(self):
        super().introduce_myself()
        print(f'Опыт работы: {self.experience}')
        print(f'Зарплата: {self.calculate_salary()}')

def create_students():
    student_1 = Student('Асан уулу Мавлидин', 19, 'not', {'Математика': 5})
    student_2 = Student('Жапарбеков Доолотбек ', 17, 'not', {'История': 4, 'Физика': 3})
    student_3 = Student('Баланчаев Тукунчу ', 20, 'yes', {'Английский': 5, 'Литература': 4, 'Химия': 5})
    return [student_1, student_2, student_3]

students = create_students()
for student in students:
    student.introduce_myself()
    print('---')

teacher = Teacher('Добрыня Никитич', 45, 'yes', 8)
teacher.introduce_myself()
