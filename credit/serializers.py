from rest_framework import serializers
from credit.models import CreditData


class CreditDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditData
        fields = ('data',)
