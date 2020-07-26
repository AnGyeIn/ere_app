from django.urls import path, include
from .views import student_list, lecturebook_list, login

urlpatterns = [
	path("students/", student_list),
	path("lecturebooks/", lecturebook_list),
	path("login/", login),
]