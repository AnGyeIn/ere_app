from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from credit.models import CreditData
from credit.serializers import CreditDataSerializer
from lecturebook.models import Student

# Create your views here.
class LoadCreditData(APIView):
    def post(self, request, format=None):
        user = Student.objects.get(sNum=request.data['sNum'])
        try:
            creditData = CreditData.objects.get(user=user)
            serializer = CreditDataSerializer(creditData)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(-1)

class SaveCreditData(APIView):
    def post(self, request, format=None):
        user = Student.objects.get(sNum=request.data['sNum'])
        data = request.data['data']
        try:
            creditData = CreditData.objects.get(user=user)
            creditData.data = data
            creditData.save()
            return Response(True)
        except ObjectDoesNotExist:
            creditData = CreditData.objects.create(data=data)
            return Response(CreditDataSerializer(creditData).data)
