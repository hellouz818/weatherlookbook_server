from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets # vieset import
from .serializers import BoardSerializer # 생성한 serializer import
from .models import Board
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BoardViewSet(viewsets.ModelViewSet): # ModelViewSet 활용
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
