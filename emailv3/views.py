from django.http import HttpRequest,JsonResponse
from rest_framework.decorators import api_view
from .serializers import Emailv3Serializer
import json
import requests

@api_view(['POST'])
def validation_v3(request: HttpRequest) -> JsonResponse:

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
    
    return JsonResponse(data_reponse)