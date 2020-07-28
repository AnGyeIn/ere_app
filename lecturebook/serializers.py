from rest_framework import serializers
from .models import Student, LectureBook

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('name', 'sNum', 'pNum')

class LectureBookSerializer(serializers.ModelSerializer):
	class Meta:
		model = LectureBook
		fields = ('id', 'title', 'author', 'lecture', 'owner', 'option', 'isAvailable')
