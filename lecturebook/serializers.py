from rest_framework import serializers
from .models import Student, LectureBook, LectureBookRequest


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('name', 'sNum')

class LectureBookSerializer(serializers.ModelSerializer):
	class Meta:
		model = LectureBook
		fields = ('id', 'title', 'author', 'lecture', 'owner', 'option', 'isAvailable')

class LectureBookRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = LectureBookRequest
		fields = ('lecturebook', 'lecturebookTitle', 'owner', 'ownerName', 'receiver', 'receiverName', 'option', 'requestTime', 'isAccepted')
