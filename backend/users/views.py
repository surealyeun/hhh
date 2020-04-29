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
<<<<<<< HEAD
from django.contrib.auth.hashers import check_password
=======
from comments import models as comments_models
import json, datetime
from django.http import HttpResponse
>>>>>>> 3b961aebb922ddb522d2290cb5f4ad23614e5d0b

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

    res_data = {}
    
    if not (username and password):
        res_data['error'] = 'ID 혹은 PASSWORD 를 입력하세요.'
    else:
        login_user = get_object_or_404(User, username=username)
        print(login_user)
        print(type(login_user))
        if check_password(password, login_user.password):
            # request.session['user'] = login_user.username
            serializer = UserSerializer(login_user)
            res_data['message'] = "로그인 성공"
            print(serializer.data)
            res_data['user'] = serializer.data
            return Response(res_data, status=status.HTTP_200_OK)

        else:
            res_data['error'] = "비밀번호가 일치하지 않습니다."
            res_data['message'] = "비밀번호가 일치하지 않습니다."
            return Response(res_data, status=status.HTTP_401_UNAUTHORIZED)




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

<<<<<<< HEAD
    
=======
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object
>>>>>>> 3b961aebb922ddb522d2290cb5f4ad23614e5d0b
