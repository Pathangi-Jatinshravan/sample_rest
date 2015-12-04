from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from models import Foods

# Create your views here.

def index(request):
    data = serializers.serialize('json', Foods.objects.all())
    return JsonResponse(data, safe=False)
