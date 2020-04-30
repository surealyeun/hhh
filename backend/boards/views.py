from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BoardSerializer, LikeSerializer
from .models import Board, Like
from users.models import User
from boards.models import Board
from comments.models import Comment
import json
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


@api_view(['POST'])
def board_post(request):
    form = UploadFileForm(request.POST, request.FILES)
    form.save()
    return Response({"message" : "data input!","data":request.data})


@api_view(['POST'])
def board_like_post(request, username, boardno):
    user = get_object_or_404(User ,username=username)
    board = get_object_or_404(Board ,id=boardno)
    like = Like(user=user,board=board)
    like.save()
    return Response({"message" : "data input!","data":request.data})


@api_view(['POST'])
def comment_post(request, boardno, userid, text):
    user = get_object_or_404(User ,id=userid)
    board = get_object_or_404(Board ,id=boardno)
    comment = Comment(text=text, writer=user, board=board)
    print(comment) 
    comment.save()
    return Response({"message" : "data input!","data":request.data})

@api_view(['DELETE'])
def board_like_delete(request, username, boardno):
    user = get_object_or_404(User ,username=username)
    board = get_object_or_404(Board ,id=boardno)
    like = Like.objects.filter(user=user).filter(board=board)
    like.delete()
    return Response({'message':'like has been deleted!'})

@api_view(['DELETE'])
def board_delete(request, boardno):
    board = get_object_or_404(Board ,id=boardno)
    board.delete()
    return Response({'message':'board has been deleted!'})

