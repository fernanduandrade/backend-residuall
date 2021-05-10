from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import Emailv1Serializer
from common.utils.valid_email import is_valid_email
import json

@api_view(['POST'])
def validation_v1(request):

    body_data = json.loads(request.body)
    valid_email = is_valid_email(body_data['email_adress'])

    if valid_email:
        data = {**body_data, 'valid_syntax': True}
        serializer = Emailv1Serializer(data=data)

        if serializer.is_valid():
            serializer.save()

        data_reponse = {
            'status': 'ok',
            'code': 200,
            'results': [
                data
            ]
        }

    else:
        data = {**body_data, 'valid_syntax': False}
        serializer = Emailv1Serializer(data=data)

        if serializer.is_valid():
            serializer.save()

        data_reponse = {
            'status': 'ok',
            'code': 200,
            'results': [
                data
            ]
        }
        


    
    return JsonResponse(data_reponse)