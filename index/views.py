from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    
    return JsonResponse({
        'status': 'OK',
        'code': 200,
        'results': []
    })

@api_view(['GET'])
def health(request):

    return JsonResponse({
        'status': 'OK',
        'code': 200,
        'results': [{
            'message': 'Servidor executando na porta 8080'
        }]
    })