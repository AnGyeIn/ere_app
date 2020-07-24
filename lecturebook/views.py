from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student, LectureBook
from .serializers import StudentSerializer, LectureBookSerializer

# Create your views here.
@api_view(['GET'])
def helloAPI(response):
	return Response("hello world!")

@api_view(['GET'])
def student_list(request):
	totalStudents = Student.objects.all()
	serializer = StudentSerializer(totalStudents, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def lecturebook_list(request):
	totalLectureBooks = LectureBook.objects.all()
	serializer = LectureBookSerializer(totalLectureBooks, many=True)
	return Response(serializer.data)