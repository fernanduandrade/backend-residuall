from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import Emailv1Serializer
import re

@api_view(['POST'])
def validation_v1(request):

    email = request.POST['email_adress']
    domain= re.findall('(?<=@)[^.]+(?=\.)',email)[0]
    
    valid_emails = ['.com.br', '.com', '.gov.br', '.org']

    is_valided = (re.findall(r"(?=("+'|'.join(valid_emails)+r"))", email))
    
    if len(is_valided) >= 1:
        data = {'email_adress': email, 'domain': domain, 'valid_syntax': True}
        serializer = Emailv1Serializer(data=data)

        if serializer.is_valid():
            serializer.save()

        data_reponse = {
            'status': 'ok',
            'code': 200,
            'results': [{
                'email_adress': email,
                'domain': domain,
                'valid_syntax': True
            }]
        }

    else:
        data = {'email_adress': email, 'domain': domain}
        serializer = Emailv1Serializer(data=data)

        if serializer.is_valid():
            serializer.save()

        data_reponse = {
            'status': 'ok',
            'code': 200,
            'results': [{
                'email_adress': email,
                'domain': domain,
                'valid_syntax': False
            }]
        }
        


    
    return JsonResponse(data_reponse)