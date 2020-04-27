from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
from follows import models as follow_models
from boards import models as board_models
from boards import serializers as board_serializer
from comments import models as comments_models
import json, datetime
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def user_search(request, username):
    user = get_object_or_404(User, username=username)
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data)

@api_view(['GET'])
def user_search_by_id(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data)


@api_view(['PUT','DELETE'])
def user_update_and_delete(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'PUT':
        serializer = UserSerializer(data=request.data, instance=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'User has been updated!'})
    else:
        user.delete()
        return Response({'message':'User has been deleted!'})
     
@api_view(['GET'])
def login(request, username, password):
    if username=='Eum_mericano' and password == '1234':
        return Response({'message':'인증되었습니다'}, status=status.HTTP_200_OK)
    return Response({'message':'아이디와 비밀번호를 다시 확인해주세요'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def user_follow_feedlist(request, username):
    user = get_object_or_404(User, username=username)
    followlist = follow_models.Follow.objects.filter(following=user)
    followlist = list(followlist.values())

    feedlist = []
    result = board_models.Board.objects.filter(writer=user.id)[:50]
    result = list(result.values())
    for i in range(len(result)):
        user = get_object_or_404(User ,id=result[i]["writer_id"])
        board = get_object_or_404(board_models.Board ,id=result[i]["id"])
        like = list(board_models.Like.objects.filter(board=board).values())
        result[i]["likes"] =len(like)

        login_user = get_object_or_404(User ,username=username)
        like = list(board_models.Like.objects.filter(board=board).filter(user=login_user).values())
        
        comments = list(comments_models.Comment.objects.filter(board=board).values())
        result[i]["comments"] = comments

        pressLike = True
        if len(like) == 0:
            pressLike = False
        result[i]["pressLike"] = pressLike
        feedlist.append(result[i])
        
    feedlist.append(result)
    for i in range(len(followlist)):
        result = board_models.Board.objects.filter(writer=followlist[i]['followed_id'])
        result = list(result.values())
        
        for i in range(len(result)):
            user = get_object_or_404(User ,id=result[i]["writer_id"])
            board = get_object_or_404(board_models.Board ,id=result[i]["id"])
            like = list(board_models.Like.objects.filter(board=board).values())
            result[i]["likes"] =len(like)

            login_user = get_object_or_404(User ,username=username)
            like = list(board_models.Like.objects.filter(board=board).filter(user=login_user).values())
            
            comments = list(comments_models.Comment.objects.filter(board=board).values())
            result[i]["comments"] = comments

            pressLike = True
            if len(like) == 0:
                pressLike = False
            result[i]["pressLike"] = pressLike
            feedlist.append(result[i])
    json_list = json.dumps(feedlist, cls=DateTimeEncoder)
    return HttpResponse(json_list)

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object