from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404
from follows import models as follow_models
from boards import models as board_models
from boards import serializers as board_serializer
from django.contrib.auth.hashers import check_password

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def user_search(request, username):
    user = get_object_or_404(User, username=username)
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
        login_user = User.objects.get(username=username)
        print(login_user)
        if check_password(password, login_user.password):
            # request.session['user'] = login_user.username
            res_data['message'] = "로그인 성공"
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

    queryset = board_models.Board.objects.filter(writer=user.id)
    for i in range(len(followlist)):
        result = board_models.Board.objects.filter(writer=followlist[i]['followed_id'])
        queryset = queryset | result
    queryset = queryset.order_by("-created")
    feed_serializer = board_serializer.BoardSerializer(queryset, many=True)
    return Response(feed_serializer.data)     

    