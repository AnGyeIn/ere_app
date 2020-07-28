from django.contrib import admin

from .models import Student, LectureBook, LectureBookRequest

# Register your models here.
admin.site.register(Student)
admin.site.register(LectureBook)
admin.site.register(LectureBookRequest)
