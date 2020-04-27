from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404


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
        login_user = User.object.get(username=username, )

    # if username=='Eum_mericano' and password == '1234':
    #     return Response({'message':'인증되었습니다'}, status=status.HTTP_200_OK)
    # return Response({'message':'아이디와 비밀번호를 다시 확인해주세요'}, status=status.HTTP_404_NOT_FOUND)