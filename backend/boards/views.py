from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BoardSerializer, LikeSerializer
from .models import Board, Like
from users.models import User
from boards.models import Board


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


@api_view(['POST'])
def board_like_post(request):
    return Response({"message" : "data input!","data":request.data})

@api_view(['DELETE'])
def board_like_delete(request, username, boardno):
    user = get_object_or_404(User ,username=username)
    board = get_object_or_404(Board ,id=boardno)
    like = Like.objects.filter(user=user).filter(board=board)
    like.delete()
    return Response({'message':'like has been deleted!'})
    
