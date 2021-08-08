import unittest
import datetime

from homework6.tasks.oop_2 import (
    Homework,
    Teacher,
    Student,
    HomeworkResult,
    Person,
    DeadlineError,
)


class TestPerson(unittest.TestCase):

    person_example = Person("John", "Petrov")

    def test_teacher_initializer(self):
        self.assertEqual(self.person_example.first_name, "John")
        self.assertEqual(self.person_example.last_name, "Petrov")


class TestStudent(unittest.TestCase):

    student_example = Student("Petrov", "John")
    teacher_example = Teacher("Petrov", "John")

    homework_active = teacher_example.create_homework("Active homework", 10)
    homework_inactive = teacher_example.create_homework("Active homework", 0)

    def test_do_homework(self):
        assert isinstance(
            self.student_example.do_homework(self.homework_active, "solution"),
            HomeworkResult,
        )
        self.assertRaises(
            DeadlineError,
            self.student_example.do_homework,
            self.homework_inactive,
            "another solution",
        )


class TestTeacher(unittest.TestCase):

    teacher_example = Teacher("Petrov", "John")
    student_example = Student("Lev", "Sokolov")

    assert len(Teacher.homework_done) == 0

    homework_active = teacher_example.create_homework("Active homework", 10)
    homework_inactive = teacher_example.create_homework("Active homework", 1)

    result_active_homework = student_example.do_homework(
        homework_active, "I have done this hw"
    )
    another_result_active_homework = student_example.do_homework(
        homework_active, "I have this homework"
    )

    result_inactive_homework = student_example.do_homework(homework_inactive, "Done")
    another_result_inactive_homework = student_example.do_homework(
        homework_inactive, "I done too"
    )

    def test_teacher_create_homework(self):
        assert isinstance(
            self.teacher_example.create_homework("Active homework", 10), Homework
        )
        assert isinstance(
            self.teacher_example.create_homework("Inactive homework", 0), Homework
        )

    def test_check_homework(self):
        self.assertEqual(
            self.teacher_example.check_homework(self.result_active_homework), True
        )
        self.assertEqual(
            self.teacher_example.check_homework(self.another_result_active_homework),
            True,
        )
        self.assertEqual(
            self.teacher_example.check_homework(self.another_result_inactive_homework),
            True,
        )
        self.assertEqual(
            self.teacher_example.check_homework(self.result_inactive_homework), False
        )
        assert self.teacher_example.homework_done[self.homework_active] == [
            "I have done this hw",
            "I have this homework",
        ]
        assert self.teacher_example.homework_done[self.homework_inactive] == [
            "I done too"
        ]

    def test_reset_results(self):
        self.assertEqual(
            self.teacher_example.check_homework(self.result_active_homework), True
        )
        self.assertEqual(
            self.teacher_example.check_homework(self.another_result_active_homework),
            True,
        )
        self.assertEqual(
            self.teacher_example.check_homework(self.another_result_inactive_homework),
            True,
        )
        assert len(Teacher.homework_done) == 2

        self.teacher_example.reset_results(self.homework_active)
        assert len(Teacher.homework_done) == 1

        self.teacher_example.reset_results()
        assert len(Teacher.homework_done) == 0


class TestHomework(unittest.TestCase):

    teacher_example = Teacher("John", "Petrov")

    homework_active = teacher_example.create_homework("Active homework", 10)
    homework_inactive = teacher_example.create_homework("Active homework", 0)

    def test_homework_initializer(self):
        self.assertEqual(self.homework_active.text, "Active homework")
        self.assertEqual(self.homework_active.deadline, datetime.timedelta(days=10))

    def test_homework_is_active(self):
        self.assertEqual(self.homework_active.is_active(), True)
        self.assertEqual(self.homework_inactive.is_active(), False)


class TestHomeworkResult(unittest.TestCase):

    student_example = Student("Petrov", "John")
    teacher_example = Teacher("Petrov", "John")

    homework_active = teacher_example.create_homework("Active homework", 10)
    homework_active_result = student_example.do_homework(homework_active, "solution")

    def test_homework_result_initializer(self):
        self.assertEqual(self.homework_active_result.homework, self.homework_active)
        self.assertEqual(self.homework_active_result.author, self.student_example)
        self.assertEqual(self.homework_active_result.solution, "solution")
        self.assertRaises(
            TypeError,
            HomeworkResult,
            self.student_example,
            "fff",
            "Solution",
        )


if __name__ == "__main__":
    unittest.main()
