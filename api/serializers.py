from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework import serializers

from .models import Loan


class AccountNumberSerializer(serializers.Serializer):
    account_number = serializers.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(10)])


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"