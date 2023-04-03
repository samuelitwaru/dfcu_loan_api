from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Loan, Customer
from .serializers import AccountNumberSerializer, LoanSerializer


@api_view(['POST'])
def loan_status(request):
    """
    Validate the account number passed in the request,
    If account number is valid: return customer's loan status
    Else, return an error message
    """

    if request.method == 'POST':
        serializer = AccountNumberSerializer(data=request.data)
        if serializer.is_valid():
            # get loan status
            account_number = request.data['account_number']
            customer = Customer.objects.filter(account_number=account_number).first()
            if customer:
                loan_query = Loan.objects.filter(customer=account_number)
                loan_count = loan_query.count()
                if loan_count:
                    loan_serializer = LoanSerializer(loan_query.all(), many=True)
                    return Response(loan_serializer.data)
                else:
                    return Response({"message":"no loan found"}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'account number not found'}, status=status.HTTP_400_BAD_REQUEST)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)