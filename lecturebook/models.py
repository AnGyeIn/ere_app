from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.TextField()
	sNum = models.TextField()
	pNum = models.TextField()

class LectureBook(models.Model):
	title = models.TextField()
	author = models.TextField()
	lecture = models.TextField()
	owner = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='owningbooks')
	option = models.TextField()
	isAvailable = models.BooleanField()
