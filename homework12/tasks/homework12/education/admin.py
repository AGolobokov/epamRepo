from django.contrib import admin

from education.models import Teacher, Student, Homework, HomeworkResult

# Register your models here.


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Homework)
admin.site.register(HomeworkResult)
