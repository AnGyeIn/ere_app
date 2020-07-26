from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(User):
	name = models.TextField()
	username = models.TextField()
	pNum = models.TextField()
	password = models.TextField()

class LectureBook(models.Model):
	title = models.TextField()
	author = models.TextField()
	lecture = models.TextField()
	owner = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='owningbooks')
	option = models.TextField()
	isAvailable = models.BooleanField()
