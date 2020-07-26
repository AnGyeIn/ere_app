from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student, LectureBook
from .serializers import StudentSerializer, LectureBookSerializer
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
@api_view(['GET'])
def student_list(request):
    total_students = Student.objects.all()
    serializer = StudentSerializer(total_students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lecturebook_list(request):
    total_lecturebooks = LectureBook.objects.all().ordered_by('title')
    serializer = LectureBookSerializer(total_lecturebooks, many=True)
    return Response(serializer.data)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return Response('로그인 성공')   # todo: 내용

        else:
            try:
                user = User.objects.get(username=username)
                return Response('비밀번호가 다릅니다. 가입한 적이 없다면 학생회로 연락하시기 바랍니다.')  # todo: 내용
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['id'], request.POST['password'])
                auth.login(request, user)
                return Response('가입 및 로그인 되었습니다.')   # todo: 내용
    else:
        return Response('로그인/회원가입 요청 오류')   # todo: 내용

def logout(request):
    auth.logout(request)
    return Response('로그아웃되었습니다.')   # todo: 내용