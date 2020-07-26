from django.urls import path
from lecturebook import views

urlpatterns = [
	path("students/", views.StudentViewSet.as_view()),
	path("lecturebooks/", views.LectureBookViewSet.as_view()),
]