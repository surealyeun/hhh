# ㅎㅎㅎ (핫, 힙, 힐링)
### 빅데이터 핫플레이스 추천 SNS

http://i02a202.p.ssafy.io/
http://i02a202.p.ssafy.io/spotlist
http://i02a202.p.ssafy.io/feedlist

---
### 사용 스택
<img src"=/img/react.png" width="200" height="100"/> 
[!typescript](/img/Typescript.png = 200x100)   
[!django](https://lab.ssafy.com/s02-bigdata-sub2/s02p22a202/raw/develop/img/django.png){: width="200" height="100"}
[!mysql](./img/mysql.png){: width="200" height="100"}   
[!aws](/img/aws.png){: width="200" height="100"}  

### 사용 데이터 (예정)
```
다이닝코드
카드사 결제 데이터
서울시 생활인구
SK Tmap 이용데이터
bigdata marketC 문화정보 데이터
SNS 스크래퍼
```
---
### 프론트엔드
> MainPage
- 서비스를 직관적으로 보여줄 수 있도록 서울 지역의 핫플레이스 지수를 지도에 표시한 html 파일을 메인 페이지에 삽입한다.
- 지도 클릭을 통해 해당 지역의 핫플레이스를 보여주는 방식으로 개발할 예정이다.
[!main](/img/main.png)   

> HotPlace
- 지도에서 선택한 장소의 주변 핫플레이스 리스트를 이미지를 통해 보여주며 스크롤 하면 가로로 이동이 가능하다.
- ♡ 를 눌러 장소를 찜할 수도 있다.
- 이미지를 눌러 이동하는 상세페이지는 추후 구현 예정
[!hotplace](/img/spotlist.png)   


> FeedList
- 유저의 팔로우, 팔로워, 게시글 수를 확인할 수 있고 또 작성한 게시글과 각 게시글의 좋아요, 댓글들을 확인할 수 있다.
- 검색 기능을 이용하면 다른 유저들의 피드들을 확인할 수 있다.
[!feed](/img/feedlist.png)   

---
### 백엔드
> django Model 구성
```
- 모델설계
    게시글, 댓글, 팔로우, 위시리스트
```
[!ERD](/img/erd.png)
```
- rest framework 설정 및 redoc 설정
```
[!redoc](/img/redoc1.png)
[!redoc](/img/redoc2.png)

> Web Crawling

- 크롤러 분류 - 상태 유무, JavaScript 유무
- Request 요청 주의 할 점 - 서버 부하 고려
- 콘텐츠 저작권 문제

selenium / beautifulsoup
- 인스타그램에서 해시태그 등을 이용한 데이터 분석 중

---
### 배포 

> frontend
http://i02a202.p.ssafy.io/
http://i02a202.p.ssafy.io/spotlist
http://i02a202.p.ssafy.io/feedlist


> rest API
http://13.125.113.171:8000/

프론트엔드 배포 : nginx

백엔드 배포 : screen, WSGI(Gunicorn)

[!nginx](/img/nginx.png){: width="200" height="100"} 
> WSGI 참고자료
https://paphopu.tistory.com/37
