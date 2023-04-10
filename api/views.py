import os

from django.http import HttpResponse
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Customer, Loan
from .serializers import AccountNumberSerializer, LoanSerializer
from utils import get_host_name


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
    

@api_view(['POST'])
def download_response(request):
    content = request.data['content']
    # Replace 'file.txt' with the name of your file
    filename = 'response.txt'
    # Replace 'path/to/file/' with the path to your file
    filepath = os.path.join(getattr(settings, 'MEDIA_ROOT'), filename)

    with open(filepath, 'w') as f:
        f.write(content)
        # response = HttpResponse(f.read(), content_type='text/plain')
        # response['Content-Disposition'] = f'attachment; filename={filename}'
        # return response
    
    host = get_host_name(request)
    file_url = f'{host}/media/{filename}'
    print(file_url)
    return Response({'file_url': file_url})