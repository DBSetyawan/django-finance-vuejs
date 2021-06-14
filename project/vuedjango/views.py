from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from vuedjango.models import Tutorial
from vuedjango.serializers import TutorialSerializer
from rest_framework.decorators import api_view

# Create your views here.
def vue_test(request):
    return render(request, 'vuedjango/vuedjango.templates.vuedjango.ind.html')

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    # GET all published tutorials
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 