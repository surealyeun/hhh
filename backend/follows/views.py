from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Follow
from .serializers import FollowSerializer
from users.models import User
from users.serializers import UserSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

@api_view(['GET'])
def following_list(request, user_id):
    followlist = list(Follow.objects.filter(following=user_id).values())
    queryset = Follow.objects.none()
    for i in range(len(followlist)):
        result = User.objects.filter(id=followlist[i]['followed_id'])
        queryset = queryset | result
    if len(list(queryset.values())) is not 0:
        queryset = queryset.order_by("-username")
    follow_serializer = UserSerializer(queryset, many=True)
    return Response(follow_serializer.data)

@api_view(['GET'])
def follower_list(request, user_id):
    followerlist = list(Follow.objects.filter(followed=user_id).values())
    queryset = Follow.objects.none()
    for i in range(len(followerlist)):
        result = User.objects.filter(id=followerlist[i]['following_id'])
        queryset = queryset | result
    if len(list(queryset.values())) is not 0:
        queryset = queryset.order_by("-username")
    follow_serializer = UserSerializer(queryset, many=True)
    return Response(follow_serializer.data)


@api_view(['POST'])
def follow(request, following_id, followed_id):
    following = get_object_or_404(User ,id=following_id)
    followed = get_object_or_404(User ,id=followed_id)
    follow = Follow(following=following,followed=followed)
    follow.save()
    return Response({"message" : "data input!","data":request.data})

@api_view(['DELETE'])
def unfollow(request, follower, followed):
    follower = get_object_or_404(User ,id=follower)
    followed = get_object_or_404(User ,id=followed)
    follow = Follow.objects.filter(following_id=follower.id).filter(followed_id=followed.id)
    follow.delete()
    return Response({'message':'follow has been deleted!'})