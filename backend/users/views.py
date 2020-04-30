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
from api import models as api_models
from places import models as place_models
from boards import serializers as board_serializer
from django.contrib.auth.hashers import check_password
from comments import models as comments_models
import json, datetime
from django.http import HttpResponse
import pymysql
import pandas as pd
from operator import itemgetter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def wishlist_store(request, store_id, username, score=0):
    user = get_object_or_404(User ,username=username)
    store = get_object_or_404(api_models.DiningStore ,id=store_id)
    exist_star = place_models.Review.objects.filter(user=user).filter(store=store)
    exist_star.delete()
    star = place_models.Review(user=user,store=store, score=score)
    star.save()
    return Response({"message" : "data input!","data":request.data})

@api_view(['POST'])
def wishlist_location(request, location_id, username, score=0):
    user = get_object_or_404(User ,username=username)
    location = get_object_or_404(api_models.Location ,id=location_id)
    exist_star = place_models.Review.objects.filter(user=user).filter(location=location)
    exist_star.delete()
    star = place_models.Review(user=user,location=location,score=score)
    star.save()
    return Response({"message" : "data input!","data":request.data})


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
        if check_password(password, login_user.password):
            # request.session['user'] = login_user.username
            serializer = UserSerializer(login_user)
            res_data['message'] = "로그인 성공"
            res_data['user'] = serializer.data
            return Response(res_data, status=status.HTTP_200_OK)

        elif (password == login_user.password):
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

    feedlist = []
    result = board_models.Board.objects.filter(writer=user.id)[:50]
    result = list(result.values())
    for i in range(len(result)):
        user_writer = get_object_or_404(User ,id=result[i]["writer_id"])
        board = get_object_or_404(board_models.Board ,id=result[i]["id"])
        like = list(board_models.Like.objects.filter(board=board).values())

        if board.location_id is None:
            store = get_object_or_404(api_models.DiningStore, id=board.store_id)
            result[i]["loc_name"] = store.store_name
        if board.store_id is None:
            store = get_object_or_404(api_models.Location, id=board.location_id)
            result[i]["loc_name"] = store.location_name

        result[i]["likes"] =len(like)
        result[i]["username"] = user_writer.username
        
        photos = []
        photo1 = board.photo
        if str(photo1) is not "":
            photos.append("http://13.125.113.171:8000/media/"+str(photo1))

        photo2 = board.photo2
        if str(photo2) is not "":
            photos.append("http://13.125.113.171:8000/media/"+str(photo2))
        
        photo3 = board.photo3
        if str(photo3) is not "":
            photos.append("http://13.125.113.171:8000/media/"+str(photo3))
        result[i]["photos"] = photos 

        if str(user.avatar) is not "":
            result[i]["avatar"] = "http://13.125.113.171:8000/media/"+str(user.avatar)
        else :
            result[i]["avatar"] = ""

        login_user = get_object_or_404(User ,username=username)
        like = list(board_models.Like.objects.filter(board=board).filter(user=login_user).values())
        
        comments = list(comments_models.Comment.objects.filter(board=board).values())
        result[i]["comments"] = comments
        for j in range(len(comments)):
            user_commenter = get_object_or_404(User ,id=comments[j]["writer_id"])
            comments[j]['username'] = user_commenter.username
            if str(user.avatar) is not "":
                comments[j]["avatar"] = "http://13.125.113.171:8000/media/"+str(user.avatar)
            else :
                comments[j]["avatar"] = ""

        pressLike = True
        if len(like) == 0:
            pressLike = False
        result[i]["pressLike"] = pressLike
        feedlist.append(result[i])

    followlist = follow_models.Follow.objects.filter(following=user)
    followlist = list(followlist.values())
    for i in range(len(followlist)):
        result = board_models.Board.objects.filter(writer=followlist[i]['followed_id'])
        result = list(result.values())
        for i in range(len(result)):
            user = get_object_or_404(User ,id=result[i]["writer_id"])
            board = get_object_or_404(board_models.Board ,id=result[i]["id"])

            if board.location_id is None:
                store = get_object_or_404(api_models.DiningStore, id=board.store_id)
                result[i]["loc_name"] = store.store_name
            if board.store_id is None:
                store = get_object_or_404(api_models.Location, id=board.location_id)
                result[i]["loc_name"] = store.location_name

            like = list(board_models.Like.objects.filter(board=board).values())
            result[i]["likes"] =len(like)
            result[i]["username"] = user.username
 
            photos = []
            photo1 = board.photo
            if str(photo1) is not "":
                photos.append("http://13.125.113.171:8000/media/"+str(photo1))

            photo2 = board.photo2
            if str(photo2) is not "":
                photos.append("http://13.125.113.171:8000/media/"+str(photo2))
            
            photo3 = board.photo3
            if str(photo3) is not "":
                photos.append("http://13.125.113.171:8000/media/"+str(photo3))
            result[i]["photos"] = photos  

            
            if str(user.avatar) is not "":
                result[i]["avatar"] = "http://13.125.113.171:8000/media/"+str(user.avatar)
            else :
                result[i]["avatar"] = ""
                
            login_user = get_object_or_404(User ,username=username)
            like = list(board_models.Like.objects.filter(board=board).filter(user=login_user).values())
            
            comments = list(comments_models.Comment.objects.filter(board=board).values())
            result[i]["comments"] = comments
            for j in range(len(comments)):
                user = get_object_or_404(User ,id=comments[j]["writer_id"])
                comments[j]['username'] = user.username
                if str(user.avatar) is not "":
                    comments[j]["avatar"] = "http://13.125.113.171:8000/media/"+str(user.avatar)
                else :
                    comments[j]["avatar"] = ""

            pressLike = True
            if len(like) == 0:
                pressLike = False
            result[i]["pressLike"] = pressLike
            feedlist.append(result[i])
    if len(feedlist) is not 0:
        feedlist = sorted(feedlist, key=lambda  feed: feed["created"], reverse=True)
    json_list = json.dumps(feedlist, cls=DateTimeEncoder)
    return HttpResponse(json_list)

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj): 
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object



@api_view(['GET'])
def user_feedlist(request, user_name):
    user = get_object_or_404(User, username=user_name)
    feedlist = []
    result = board_models.Board.objects.filter(writer=user.id)[:50]
    result = list(result.values())
    for i in range(len(result)):
        user = get_object_or_404(User ,id=result[i]["writer_id"])
        board = get_object_or_404(board_models.Board ,id=result[i]["id"])

        if board.location_id is None:
            store = get_object_or_404(api_models.DiningStore, id=board.store_id)
            result[i]["loc_name"] = store.store_name
        if board.store_id is None:
            store = get_object_or_404(api_models.Location, id=board.location_id)
            result[i]["loc_name"] = store.location_name
   
        photos = []
        photo1 = board.photo
        if str(photo1) is not "":
            photos.append("http://13.125.113.171:8000/media/"+str(photo1))

        photo2 = board.photo2
        if str(photo2) is not "":
            photos.append("http://13.125.113.171:8000/media/"+str(photo2))
        
        photo3 = board.photo3
        if str(photo3) is not "":
            photos.append("http://13.125.113.171:8000/media/"+str(photo3))
        result[i]["photos"] = photos 

        like = list(board_models.Like.objects.filter(board=board).values())
        result[i]["likes"] = len(like)
        result[i]["username"] = user.username

        if str(user.avatar) is not "":
            result[i]["avatar"] = "http://13.125.113.171:8000/media/"+str(user.avatar)
        else :
            result[i]["avatar"] = ""
                
        login_user = get_object_or_404(User ,username=user_name)
        like = list(board_models.Like.objects.filter(board=board).filter(user=login_user).values())
        
        comments = list(comments_models.Comment.objects.filter(board=board).values())
        
        result[i]["comments"] = comments
        for j in range(len(comments)):
            user = get_object_or_404(User ,id=comments[j]["writer_id"])
            comments[j]['username'] = user.username
            if str(user.avatar) is not "":
                comments[j]["avatar"] = "http://13.125.113.171:8000/media/"+str(user.avatar)
            else :
                comments[j]["avatar"] = ""

        pressLike = True
        if len(like) == 0:
            pressLike = False
        result[i]["pressLike"] = pressLike
        feedlist.append(result[i])
    if len(feedlist) is not 0:
        feedlist = sorted(feedlist, key=lambda  feed: feed["created"], reverse=True)
    json_list = json.dumps(feedlist, cls=DateTimeEncoder)
    return HttpResponse(json_list)


@api_view(['GET'])
def recommend_location_list(request, area_gu, username="Eum_mericano"):
    
    connection = pymysql.connect(
        host='13.125.113.171', user='root', password='ssafya202!@#', db='HHH',
        charset='utf8mb4', autocommit=True, cursorclass=pymysql.cursors.DictCursor
    )

    cursor = connection.cursor()
    user = get_object_or_404(User ,username=username)

    sql = "select * from HHH.api_recommend_by_id_"+area_gu+" where user_id="+str(user.id)
    cursor.execute(sql)
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    
    if username != "Eum_mericano" and df.empty:
        sql = "select * from HHH.api_recommend_by_id_"+area_gu+" where user_id=1"
        cursor.execute(sql)
        result = cursor.fetchall()
        df = pd.DataFrame(result)

    connection.close()

    df = pd.DataFrame(result)
    recommend_list = list(df["recommend"])
    isLocation = list(df["isLocation"])
    
    result= []
    for i in range(len(recommend_list)):
        dic = {}
        if isLocation[i] is 1:
            location = get_object_or_404(api_models.Location, id=recommend_list[i])
            dic["id"] = recommend_list[i]
            dic["url"] = "http://13.125.113.171:8000/media/shop.png"
            dic["location_name"] = location.location_name
            dic["description"] = location.description
            dic["rank"] = str(i+1)
            dic["address_see"] = location.address_see
            dic["address_gu"] = location.address_gu
            dic["address_dong"] = location.address_dong
            dic["latitude"] = location.latitude
            dic["longitude"] = location.longitude
            
        else :
            store = get_object_or_404(api_models.DiningStore, id=recommend_list[i])
            dic["id"] = recommend_list[i]
            dic["category"] = store.category
            dic["url"] = "http://13.125.113.171:8000/media/shop.png"
            dic["store_name"] = store.store_name
            dic["rank"] = str(i+1)
            dic["address_see"] = store.address_see
            dic["address_gu"] = store.address_gu
            dic["address_dong"] = store.address_dong
            dic["latitude"] = store.latitude
            dic["longitude"] = store.longitude
        result.append(dic)
    json_list = json.dumps(result)
    return HttpResponse(json_list)


@api_view(['GET'])
def store_detail(request, store_id):   

    store = get_object_or_404(api_models.DiningStore, id=store_id)
    print(store)
    boards = board_models.Board.objects.filter(store=store.id)
    board_list = list(boards.values())
    print(board_list)
    for i in range(len(board_list)):
        board_list[i]["image"] = "http://13.125.113.171:8000/media/"+str(board_list[i]["photo"])

    print(board_list)
    if len(board_list) is not 0:
        board_list.sort(key=itemgetter('created'), reverse=True)
    json_list = json.dumps(board_list, cls=DateTimeEncoder)
    return HttpResponse(json_list)

@api_view(['GET'])
def location_detail(request, location_id):   

    location = get_object_or_404(api_models.Location, id=location_id)
    
    boards = board_models.Board.objects.filter(location=location.id)
    board_list = list(boards.values())
    
    for i in range(len(board_list)):
        board_list[i]["image"] = "http://13.125.113.171:8000/media/"+str(board_list[i]["photo"])

    print(board_list)
    if len(board_list) is not 0:
        board_list.sort(key=itemgetter('created'), reverse=True)
    json_list = json.dumps(board_list, cls=DateTimeEncoder)
    return HttpResponse(json_list)
