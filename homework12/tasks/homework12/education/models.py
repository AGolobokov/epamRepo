from django.db import models

# Create your models here.


class Teacher(models.Model):

    first_name = models.CharField(max_length=128, blank=False,  verbose_name='Имя')
    last_name = models.CharField(max_length=128, blank=False,  verbose_name='Фамилия')


class Student(models.Model):

    first_name = models.CharField(max_length=128, blank=False,  verbose_name='Имя')
    last_name = models.CharField(max_length=128, blank=False,  verbose_name='Фамилия')


class Homework(models.Model):

    text_of_homework = models.TextField(blank=False, verbose_name='Текст')  # required to field
    deadline = models.DateField(auto_now_add=True, blank=False, verbose_name='Дата окончания') # required to field
    created = models.DateField(auto_now_add=True, blank=False, verbose_name='Дата создания') # required to field
    is_active = models.BooleanField(default=True)


class HomeworkResult(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, verbose_name='Автор')
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, blank=False, verbose_name='Домашнее задание')
    solution = models.TextField(blank=False, verbose_name='Решение')  # required to field
