from django.urls import path
from credit import views

urlpatterns = [
    path("load/", views.LoadCreditData.as_view()),
    path("save/", views.SaveCreditData.as_view()),
]
