from django.urls import path
from lecturebook import views

urlpatterns = [
	path("students/", views.StudentViewSet.as_view()),
	path("lecturebooks/", views.LectureBookViewSet.as_view()),
	path("signup/", views.Signup.as_view()),
	path("activate/<int:id>/", views.ActivateLectureBook.as_view()),
	path("deactivate/<int:id>/", views.DeactivateLectureBook.as_view())
]