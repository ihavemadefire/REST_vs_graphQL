from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models.models import *
from rest_framework.parsers import JSONParser
from .serializers import *

@csrf_exempt
def dog_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Dog.objects.all()
        serializer = DogSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)