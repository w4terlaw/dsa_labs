from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Student:
    id: int
    last_name: str
    first_name: str
    middle_name: str
    date: date
    address: str
    telephone: int
    fac: str
    course: int
    group: str

    @classmethod
    def create_students(cls):
        students = list()

        students.append(
            cls(1, 'Иванов', 'Иван', 'Иванович', date(2000, 1, 1), 'ул. Пушкина, д.1', 1234567890, 'Философия', 2,
                'Ф-1-22'))
        students.append(
            cls(2, 'Петров', 'Петр', 'Петрович', date(2001, 2, 2), 'ул. Лермонтова, д.2', 9876543210,
                'Философия', 3, 'Ф-1-22'))
        students.append(
            cls(3, 'Сидоров', 'Сидор', 'Сидорович', date(1999, 3, 3), 'ул. Тургенева, д.3', 1357924680,
                'Прикладная математика', 1, 'М-1-22'))
        students.append(
            cls(4, 'Абкеримов', 'Эльмир', 'Абкеримович', date(2003, 1, 27), 'ул. Симферопольская, д.3', 79780126134,
                'Прикладная информатика', 4, 'И-1-20'))
        return students


class Filter:
    def __init__(self, students: List[Student]):
        self.students = students

    def get_student_by_fac(self, *, fac: str):
        print(
            'a) список студентов заданного факультета:',
            *filter(lambda student: student.fac == fac, self.students),
            sep='\n', end='\n\n'
        )

    def get_student_by_fac_and_course(self, *, fac: str, course: int):
        print(
            'b) списки студентов для каждого факультета и курса',
            *filter(lambda student: student.fac == fac and student.course == course, self.students),
            sep='\n', end='\n\n'
        )

    def get_students_by_year(self, *, year: int):
        current_year = date(year, 1, 1)
        print(
            'c) список студентов, родившихся после заданного года:',
            *filter(lambda student: student.date > current_year, self.students),
            sep='\n', end='\n\n'
        )

    def get_students_by_group(self, *, group: str):
        print(
            'd) список учебной группы.',
            *filter(lambda student: student.group == group, self.students),
            sep='\n', end='\n\n'
        )


students_list = Student.create_students()
student_filter = Filter(students_list)

student_filter.get_student_by_fac(fac='Прикладная математика')
student_filter.get_student_by_fac_and_course(fac='Прикладная информатика', course=4)
student_filter.get_students_by_year(year=2000)
student_filter.get_students_by_group(group='Ф-1-22')
