from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, LectureBook
from .serializers import StudentSerializer, LectureBookSerializer

# Create your views here.
class StudentViewSet(APIView):
    authentication_classes = []
    permission_classes = []

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

class Signup(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        if Student.objects.filter(sNum=request.data['sNum']).count() > 0:
            return Response(-1)
        else:
            sNum = request.data['sNum']
            name = request.data['name']
            pNum = request.data['pNum']
            password = request.data['password']
            Student.objects.create_user(sNum=sNum, name=name, pNum=pNum, password=password)
            return Response(sNum)
