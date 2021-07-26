import unittest
import datetime
from homework6.tasks.oop_2 import Homework, Teacher, Student, HomeworkResult, Person, DeadlineError, IncorrectObjectError


# не знаю надо тестировать классы наследники исключений или нет, вроде бы как они просто наследую и больше ничего, зачем тогда тесты
class TestPerson(unittest.TestCase):

    person_example = Person('John', 'Petrov')

    def test_teacher_initializer(self):
        self.assertEqual(self.person_example.first_name, 'John')
        self.assertEqual(self.person_example.last_name, 'Petrov')


class TestStudent(unittest.TestCase):
    student_example = Student('Petrov', 'John')
    teacher_example = Teacher('Petrov', 'John')

    homework_active = teacher_example.create_homework('Active homework', 10)
    homework_inactive = teacher_example.create_homework('Active homework', 0)

    def test_do_homework(self):
        assert isinstance(self.student_example.do_homework(self.homework_active, "solution"), HomeworkResult)
        #шото не получилось еще разбираюсь
        # self.assertRaises(DeadlineError("You are late"), self.student_example.do_homework(self.homework_inactive, "another solution"))


class TestTeacher(unittest.TestCase):

    teacher_example = Teacher('Petrov', 'John')

    def test_teacher_create_homework(self):
        assert isinstance(self.teacher_example.create_homework('Active homework', 10), Homework)
        assert isinstance(self.teacher_example.create_homework('Active homework', 0), Homework)

    def test_check_homework(self):
        pass

    def test_reset_results(self):
        pass


class TestHomework(unittest.TestCase):

    teacher_example = Teacher('John', 'Petrov')

    homework_active = teacher_example.create_homework('Active homework', 10)
    homework_inactive = teacher_example.create_homework('Active homework', 0)

    def test_homework_initializer(self):
        self.assertEqual(self.homework_active.text, 'Active homework')
        self.assertEqual(self.homework_active.deadline, datetime.timedelta(days=10))

    def test_homework_is_active(self):
        self.assertEqual(self.homework_active.is_active(), True)
        self.assertEqual(self.homework_inactive.is_active(), False)


class TestHomeworkResult(unittest.TestCase):

    student_example = Student('Petrov', 'John')
    teacher_example = Teacher('Petrov', 'John')

    homework_active = teacher_example.create_homework('Active homework', 10)
    homework_inactive = teacher_example.create_homework('Inactive homework', 0)

    homework_active_result = student_example.do_homework(homework_active, 'solution')
    # homework_inactive_result = student_example.do_homework()

    def test_homework_result_initializer(self):
        self.assertEqual(self.homework_active_result.homework, self.homework_active)
        self.assertEqual(self.homework_active_result.author, self.student_example)
        self.assertEqual(self.homework_active_result.solution, 'solution')
        # self.assertRaises(IncorrectObjectError, HomeworkResult(self.student_example, "fff", "Solution"))


if __name__ == '__main__':
    unittest.main()
