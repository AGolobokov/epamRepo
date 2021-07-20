import unittest
import datetime
from homework5.tasks.oop_1 import Homework, Teacher, Student


class TestHomework(unittest.TestCase):

    teacher_example = Teacher('John', 'Petrov')
    homework_active = teacher_example.create_homework('Active homework', 10)
    homework_inactive = teacher_example.create_homework('Active homework', 0)

    def test_homework_constructor(self):
        self.assertEqual(self.homework_active.text, 'Active homework')
        self.assertEqual(self.homework_active.deadline, datetime.timedelta(days=10))

    def test_homework_is_active(self):
        self.assertEqual(self.homework_active.is_active(), True)
        self.assertEqual(self.homework_inactive.is_active(), False)


class TestTeacher(unittest.TestCase):

    teacher_example = Teacher('Petrov', 'John')
    homework_active = teacher_example.create_homework('Active homework', 10)
    homework_inactive = teacher_example.create_homework('Active homework', 0)

    def test_teacher_constructor(self):
        self.assertEqual(self.teacher_example.first_name, 'John')
        self.assertEqual(self.teacher_example.last_name, 'Petrov')

    def test_teacher_create_homework(self):
        self.assertEqual(self.teacher_example.create_homework(), Homework)


class TestStudent(unittest.TestCase):

    student_example = Student('Petrov', 'John')
    teacher_example = Teacher('Petrov', 'John')
    homework_active = teacher_example.create_homework('Active homework', 10)
    homework_inactive = teacher_example.create_homework('Active homework', 0)

    def test_student_constructor(self):
        self.assertEqual(self.student_example.first_name, 'John')
        self.assertEqual(self.student_example.last_name, 'Petrov')

    def test_teacher_create_homework(self):
        self.assertEqual(self.student_example.do_homework(self.homework_active), self.homework_active)
        self.assertEqual(self.student_example.do_homework(self.homework_inactive), None)


if __name__ == '__main__':
    unittest.main()
