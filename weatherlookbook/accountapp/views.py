from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User
from .serializers import UserCreateSerializer

@api_view(['POST'])
@permission_classes((AllowAny, ))
def join(request):
    serializer = UserCreateSerializer(data = request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        context = {'msg':'Join Success'}
        return JsonResponse(context)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def edit_username(request):
    print(request.POST['newname'])
    user = User.objects.get(username = request.user.username)
    print(user)
    user.username = request.POST['newname']
    user.save()
    
    context = {'msg':'Username Changed Success'}
    return JsonResponse(context)

def myboard(request):
    context = {'msg':'good'}
    return JsonResponse(context)


def mylike(request):
    context = {'msg':'good'}
    return JsonResponse(context)


def deleteaccount(request):
    context = {'msg':'good'}
    return JsonResponse(context)


    