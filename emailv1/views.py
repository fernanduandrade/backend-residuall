import json

from django.http import HttpRequest

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from .serializers import Emailv1Serializer
from .models import Emailv1
from .filters import Emailv1Filter
from .utils.valid_email import is_valid_email


class Emailv1List(ListAPIView):
    queryset = Emailv1.objects.all()
    serializer_class = Emailv1Serializer
    filter_class = Emailv1Filter


@api_view(['POST'])
def validation_v1(request: HttpRequest) -> Response:

    body_data = json.loads(request.body)
    valid_email = is_valid_email(body_data['email_address'])

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
        
    return Response(data_reponse)