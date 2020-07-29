import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.
from django.utils import timezone


class StudentManager(BaseUserManager):
	def create_user(self, sNum, name, pNum, password=None):
		user = self.model(sNum=sNum, name=name, pNum=pNum)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, sNum, name, pNum, password):
		user = self.create_user(sNum, name, pNum, password)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save()
		return user

class Student(AbstractBaseUser, PermissionsMixin):
	uuid = models.UUIDField(
		primary_key=True,
		unique=True,
		editable=False,
		default=uuid.uuid4,
		verbose_name='PK'
	)

	name = models.TextField()
	sNum = models.TextField(unique=True)
	pNum = models.TextField()

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'sNum'
	REQUIRED_FIELDS = ['name', 'pNum']

	objects = StudentManager()

	def __str__(self):
		return self.name

class LectureBook(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.TextField()
	author = models.TextField()
	lecture = models.TextField()
	owner = models.ForeignKey('Student', on_delete=models.CASCADE, to_field='sNum')
	option = models.TextField()
	isAvailable = models.BooleanField()

	def __str__(self):
		return self.title

class LectureBookRequest(models.Model):
	lecturebook = models.ForeignKey('LectureBook', on_delete=models.CASCADE, to_field='id')
	lecturebookTitle = models.TextField()
	owner = models.ForeignKey('Student', on_delete=models.CASCADE, to_field='sNum', related_name='owning')
	ownerName = models.TextField()
	receiver = models.ForeignKey('Student', on_delete=models.CASCADE, to_field='sNum', related_name='receiving')
	receiverName = models.TextField()
	requestTime = models.DateTimeField(default=timezone.now)
	isAccepted = models.BooleanField(default=False)

	def __str__(self):
		return '{0} : {1}({2}) -> {3}({4})'.format(self.lecturebook, self.owner, self.owner.sNum, self.receiver, self.receiver.sNum)
