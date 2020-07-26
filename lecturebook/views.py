from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, LectureBook
from .serializers import StudentSerializer, LectureBookSerializer

# Create your views here.
class StudentViewSet(APIView):
    def get(self, request, format=None):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

class LectureBookViewSet(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        queryset = LectureBook.objects.all().order_by('title')
        serializer = LectureBookSerializer(queryset, many=True)
        return Response(serializer.data)
