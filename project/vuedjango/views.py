# from django.shortcuts import render

# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser 
# from rest_framework import status
 
# from vuedjango.models import Tutorial
# from vuedjango.serializers import TutorialSerializer
# from rest_framework.decorators import api_view

# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
# from .models import *
# from vuedjango import views
# from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from .models import *
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from vuedjango.forms import CustomUserCreationForm

pusher = Pusher(
  app_id='1219030',
  key='e61c72228a22ae50a400',
  secret='8f9d442985722579f783',
  cluster='ap1',
  ssl=False
)
# pusher = Pusher(app_id=u'1219030', key=u'e61c72228a22ae50a400', secret=u'8f9d442985722579f783', cluster=u'ap1')
@login_required(login_url='login/')
def index(request):
    return render(request,"vuedjango/chat.html");

@csrf_exempt
def broadcast(request):
    message = Conversation(message=request.POST.get('message', ''), status='', user=request.user);
    message.save();
    message = {'name': message.user.username, 'status': message.status, 'message': message.message, 'id': message.id}
    pusher.trigger(u'a_channel', u'an_event', message)
    return JsonResponse(message, safe=False)
    
#return all conversations in the database
def conversations(request):
    data = Conversation.objects.all()
    data = [{'name': person.user.username, 'status': person.status, 'message': person.message, 'id': person.id} for person in data]
    return JsonResponse(data, safe=False)
    
@csrf_exempt
def delivered(request, id):
    message = Conversation.objects.get(pk=id);
    if request.user.id != message.user.id:
        socket_id = request.POST.get('socket_id', '')
        message.status = 'Delivered';
        message.save();
        message = {'name': message.user.username, 'status': message.status, 'message': message.message, 'id': message.id}
        pusher.trigger(u'a_channel', u'delivered_message', message, socket_id)
        return HttpResponse('ok');
    else:
        return HttpResponse('Awaiting Delivery');

def dashboard(request):
    return render(request,"vuedjango/chat.html");

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            user = form.save()
            login(request, user)
            # return redirect(reverse("dashboard"))
        return render(request, 'users/register.html', {'form': form})
            
    # Create your views here.
def vue_test(request):
    return render(request, 'vuedjango/vuedjango.templates.vuedjango.ind.html')

    # @api_view(['GET', 'POST', 'DELETE'])
    # def tutorial_list(request):
    #     # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    #     if request.method == 'POST':
    #         tutorial_data = JSONParser().parse(request)
    #         tutorial_serializer = TutorialSerializer(data=tutorial_data)
    #         if tutorial_serializer.is_valid():
    #             tutorial_serializer.save()
    #             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
    #             return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #         if request.method == 'GET':
    #             tutorials = Tutorial.objects.all()
            
    #         title = request.GET.get('title', None)
    #         if title is not None:
    #             tutorials = tutorials.filter(title__icontains=title)
            
    #         tutorials_serializer = TutorialSerializer(tutorials, many=True)
    #         return JsonResponse(tutorials_serializer.data, safe=False)
    #         # 'safe=False' for objects serialization

    # @api_view(['GET', 'PUT', 'DELETE'])
    # def tutorial_detail(request, pk):
    #     # find tutorial by pk (id)
    #     try: 
    #         tutorial = Tutorial.objects.get(pk=pk)
    #         if request.method == 'PUT': 
    #             tutorial_serializer = TutorialSerializer(tutorial) 
    #             return JsonResponse(tutorial_serializer.data) 

    #         if request.method == 'GET': 
    #             tutorial_serializer = TutorialSerializer(tutorial) 
    #             return JsonResponse(tutorial_serializer.data) 

    #         if request.method == 'PUT': 
    #             tutorial_data = JSONParser().parse(request) 
    #             tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 

    #         elif request.method == 'DELETE': 
    #             tutorial.delete() 
    #             return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    #         elif request.method == 'DELETE':
    #             count = Tutorial.objects.all().delete()
    #             return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

    #         if tutorial_serializer.is_valid(): 
    #             tutorial_serializer.save() 
    #             return JsonResponse(tutorial_serializer.data) 
    #             return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
                
    #     except Tutorial.DoesNotExist: 
    #         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
    # @api_view(['GET'])
    # def tutorial_list_published(request):
    #     # GET all published tutorials
    #     if request.method == 'GET': 
    #         tutorials_serializer = TutorialSerializer(tutorials, many=True)
    #         return JsonResponse(tutorials_serializer.data, safe=False)
