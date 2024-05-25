from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
import requests

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@api_view(['GET'])
def get_destinations(request, account_id):
    account = get_object_or_404(Account, account_id=account_id)
    destinations = Destination.objects.filter(account=account)
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def incoming_data(request):
    token = request.headers.get('CL-X-TOKEN')
    if not token:
        return Response({"message": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        account = Account.objects.get(app_secret_token=token)
    except Account.DoesNotExist:
        return Response({"message": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    data = request.data
    destinations = Destination.objects.filter(account=account)
    
    for destination in destinations:
        headers = destination.headers
        response = requests.post(destination.url, headers=headers, json=data)
        if response.status_code != 200:
            return Response({"message": "Failed to send data to one or more destinations"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({"message": "Data successfully sent to all destinations"})
