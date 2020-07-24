from django.urls import path, include
from .views import helloAPI, student_list, lecturebook_list

urlpatterns = [
	path("hello/", helloAPI),
	path("students/", student_list),
	path("lecturebooks/", lecturebook_list),
]