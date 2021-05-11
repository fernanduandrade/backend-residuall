from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Emailv3Serializer
from .models import Emailv3
import json
import requests

@api_view(['GET'])
def get_emailv3(request: HttpRequest) -> Response:

    emails = Emailv3.objects.all()
    serializer = Emailv3Serializer(emails, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def validation_v3(request: HttpRequest) -> Response:

    body_data = json.loads(request.body)
    email_address = body_data['email_address']
    request = requests.get(f'https://api.eva.pingutil.com/email?email={email_address}')
    result = request.json()
    
    serializer = Emailv3Serializer(data=result['data'])

    if serializer.is_valid():
        serializer.save()

    data_reponse = {
        'status': 'ok',
        'code': 200,
        'results': [
            {'data' : result['data']}
        ]
    }
    
    return Response(data_reponse)