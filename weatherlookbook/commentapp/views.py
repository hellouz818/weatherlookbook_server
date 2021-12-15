from django.http.response import JsonResponse
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from boardapp.models import Board
from accountapp.models import User
from .models import Comment
# Create your views here.

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def commentcreate(request, bid):
    comment = Comment()
    comment.user = request.user
    comment.board = Board.objects.get(bid = bid)
    comment.text = request.POST['text']
    comment.save()
    return JsonResponse({"msg":"commentcreate success"})
    
