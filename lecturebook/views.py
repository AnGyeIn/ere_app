from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, LectureBook, LectureBookRequest
from .serializers import StudentSerializer, LectureBookSerializer, LectureBookRequestSerializer


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

class ActivateLectureBook(APIView):
    def post(self, request, id, format=None):
        lecturebook = LectureBook.objects.get(id=id)
        lecturebook.isAvailable = True
        lecturebook.save()
        return Response(True)

class DeactivateLectureBook(APIView):
    def post(self, request, id, format=None):
        lecturebook = LectureBook.objects.get(id=id)
        lecturebook.isAvailable = False
        lecturebook.save()
        return Response(True)

class RequestLectureBook(APIView):
    def post(self, request, id, format=None):
        lecturebook = LectureBook.objects.get(id=id)
        owner = Student.objects.get(sNum=request.data['owner'])
        receiver = Student.objects.get(sNum=request.data['receiver'])
        if LectureBookRequest.objects.filter(lecturebook=lecturebook, owner=owner, receiver=receiver).count() > 0:
            return Response(-1)
        else:
            lecturebookrequest = LectureBookRequest.objects.create(
                lecturebook=lecturebook,
                lecturebookTitle=lecturebook.title,
                owner=owner, ownerName=owner.name,
                receiver=receiver,
                option=lecturebook.option,
                receiverName=receiver.name
            )
            return Response(lecturebookrequest)

class RequestListForOwner(APIView):
    def post(self, request, format=None):
        user = Student.objects.get(sNum=request.data['sNum'])
        requests = user.owning.all().order_by('requestTime')
        serializer = LectureBookRequestSerializer(requests, many=True)
        return Response(serializer.data)

class RequestListForReceiver(APIView):
    def post(self, request, format=None):
        user = Student.objects.get(sNum=request.data['sNum'])
        requests = user.receiving.all().order_by('requestTime')
        serializer = LectureBookRequestSerializer(requests, many=True)
        return Response(serializer.data)

class CancelRequest(APIView):
    def post(self, request, id, format=None):
        lecturebook = LectureBook.objects.get(id=id)
        owner = Student.objects.get(sNum=request.data['owner'])
        receiver = Student.objects.get(sNum=request.data['receiver'])
        lecturebookrequest = LectureBookRequest.objects.get(lecturebook=lecturebook, owner=owner, receiver=receiver)
        lecturebookrequest.delete()
        return Response(True)

class AcceptRequest(APIView):
    def post(self, request, id, format=None):
        lecturebook = LectureBook.objects.get(id=id)
        owner = Student.objects.get(sNum=request.data['owner'])
        receiver = Student.objects.get(sNum=request.data['receiver'])
        lecturebookrequest = LectureBookRequest.objects.get(lecturebook=lecturebook, owner=owner, receiver=receiver)
        lecturebookrequest.isAccepted = True
        lecturebookrequest.save()
        lecturebook.isAvailable = False
        lecturebook.save()
        return Response(True)

class GetPhoneNum(APIView):
    def post(self, request, format=None):
        owner = Student.objects.get(sNum=request.data['owner'])
        return Response(owner.pNum)

class AddLectureBook(APIView):
    def post(self, request, format=None):
        title = request.data['title']
        author = request.data['author']
        lecture = request.data['lecture']
        owner = Student.objects.get(sNum=request.data['owner'])
        option = request.data['option']
        lecturebook = LectureBook.objects.create(
            title=title,
            author=author,
            lecture=lecture,
            owner=owner,
            option=option,
            isAvailable=True
        )
        return Response(lecturebook)
