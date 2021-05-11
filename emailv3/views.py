import json
import requests

from django.http import HttpRequest

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from .serializers import Emailv3Serializer
from .models import Emailv3
from .filters import Emailv3Filter

class Emailv3Filter(ListAPIView):
    queryset = Emailv3.objects.all()
    serializer_class = Emailv3Serializer
    filter_class = Emailv3Filter

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