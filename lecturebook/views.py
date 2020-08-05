from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
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

        sNum = request.data['sNum']
        name = request.data['name']
        pNum = request.data['pNum']
        password = request.data['password']
        Student.objects.create_user(sNum=sNum, name=name, pNum=pNum, password=password)
        return Response('Signed up.')

class ActivateLectureBook(APIView):
    def post(self, request, id, format=None):
        lecturebook = LectureBook.objects.get(id=id)
        lecturebook.isAvailable = True
        lecturebook.save()
        return Response('Activated the LectureBook.')

class DeactivateLectureBook(APIView):
    def post(self, request, id, format=None):
        lecturebook = LectureBook.objects.get(id=id)
        lecturebook.isAvailable = False
        lecturebook.save()
        return Response('Deactivated the LectureBook.')

class RequestLectureBook(APIView):
    def post(self, request, id, format=None):
        now = datetime.now()
        opentime = datetime(2020, 9, 1, 18, 0, 0)  # todo: change to opening time

        if (request.data['owner'] == '0000-00001') and (now < opentime):   #todo: change to sNum of student council
            return Response(-2)

        lecturebook = LectureBook.objects.get(id=id)
        if not lecturebook.isAvailable:
            return Response(-3)

        owner = Student.objects.get(sNum=request.data['owner'])
        receiver = Student.objects.get(sNum=request.data['receiver'])
        if LectureBookRequest.objects.filter(lecturebook=lecturebook, owner=owner, receiver=receiver).count() > 0:
            return Response(-1)

        LectureBookRequest.objects.create(
            lecturebook=lecturebook,
            lecturebookTitle=lecturebook.title,
            owner=owner, ownerName=owner.name,
            receiver=receiver,
            option=lecturebook.option,
            receiverName=receiver.name
        )
        return Response('Requested the LectureBook.')

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
        return Response('Canceled the LectureBookRequest.')

class AcceptRequest(APIView):
    def post(self, request, id, format=None):
        lecturebook = LectureBook.objects.get(id=id)
        owner = Student.objects.get(sNum=request.data['owner'])
        receiver = Student.objects.get(sNum=request.data['receiver'])
        try:
            lecturebookrequest = LectureBookRequest.objects.get(lecturebook=lecturebook, owner=owner, receiver=receiver)
            lecturebookrequest.isAccepted = True
            lecturebookrequest.save()
            lecturebook.isAvailable = False
            lecturebook.save()
            return Response(True)
        except ObjectDoesNotExist:
            return Response(False)

class GetPhoneNum(APIView):
    def post(self, request, format=None):
        owner = Student.objects.get(sNum=request.data['owner'])
        return Response(owner.pNum)

class AddLectureBook(APIView):
    def post(self, request, format=None):
        id = LectureBook.objects.all().count() + 1
        title = request.data['title']
        author = request.data['author']
        lecture = request.data['lecture']
        owner = Student.objects.get(sNum=request.data['owner'])
        option = request.data['option']
        LectureBook.objects.create(
            id=id,
            title=title,
            author=author,
            lecture=lecture,
            owner=owner,
            option=option,
            isAvailable=True
        )
        return Response('Added the LectureBook.')
