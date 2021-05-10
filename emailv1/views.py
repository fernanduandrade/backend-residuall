from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import Emailv1Serializer
from common.utils.valid_email import is_valid_email
from common.utils.find_domain import find_domain

@api_view(['POST'])
def validation_v1(request):

    email = request.POST['email_adress']
    domain = find_domain(email)
    valid_email = is_valid_email(email)
    
    if valid_email:
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