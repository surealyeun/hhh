# Back End

### Used Stack

- Language : Python 3.6.8
- IDE : Visual Studio Code
- Database : MySQL
- Data
  - Instartgram Web Crawling
  - 서울 열린 데이터 광장
  - 다이닝 코드
  - 카드사 데이터
  - 기타 데이터 수집 중

### DataBase

> ### Board (인스타그램 참고)

1. 게시글 ( 뉴스피드 형식 )

- id 기본 키
- 글쓴 유저
- 내용
- 이미지
- 좋아요 표시

2. 사진 (AWS 저장됨. 파일 이름 생성 규칙.)

- 이미지
- 게시글 번호

3. 좋아요

- 유저 번호

> ### Users

1. 사용자
   - 이메일 (id) - 로그인 시, id
   - 나이
   - 성별
   - 이름
   - 닉네임 (중복 방지)
   - 주소
   - 전화번호

> ### Follow

1. 팔로우
   - 팔로우하는 사람 id
   - 팔로우 받는 사람 id (foreign key)

> ### Comment

1. 코멘트

   - 댓글
   - 글쓴이 (user)
   - 게시글 번호 (Board)
   - 댓글 번호

> ### Place

1. 가게 (Store)

   - 가게 이름
   - 가게 유형
   - 가게 주소
   - 평점

2. 지역

   - 시
   - 구

   - 동 (동 단위로)
   - 위도
   - 경도

3. 가게 유형

   - 카테고리로 작성
     - 한식
     - 중식...

4. 평가 (리뷰)

   - 점수
     - 1 ~ 10
     - 점수별 카운트
   - 가게 번호
   - 한줄평
   - 유저 아이디 (이건 익명성 보장)

> ### Keywords

1. Tags
   - 태그 이름 ( ex: 따뜻한 )
   - 게시글 번호

> ### WishList

1. WishList
   - 가게 번호
   - 유저 번호

### Web Crawling

> ### 주의사항

- 대상 웹 페이지 조건 확인 - robots.txt
- 크롤러 분류 - 상태 유무, JavaScript 유무
- Request 요청 주의 할 점 - 서버 부하 고려
- 콘텐츠 저작권 문제
- 페이지 구조 변경 가능성 숙지

> ### 크롤링하기

1. selenium 설치

   - selenium : 인터넷 브라우저 컨트롤러

   - 브라우저를 이용해 특정 사이트에 접속, 동작하고, 크롤링

   - 인스타그램 등 javascript를 사용하여 페이지를 스크롤할 때 새로운 게시글을 불러오는 방식에 사용

     ```python
     from selenium import webdriver
     ```

   - pip install selenium

2) chrome 드라이버 설치

   - [크롬 드라이버 설치](https://sites.google.com/a/chromium.org/chromedriver/downloads/version-selection)
   - 설정 - Chrome 버전을 확인하고 해당하는 드라이버를 설치해야된다.
   - 현재 버전 : [ 80.0.3987.106]

3. 크롤링

   - driver

     - page_source : 페이지의 html 코드를 가져옴

   - beautifulsoup

     - find_all : 해당 되는 조건에 맞는 모든 결과 검색
       - name : 검색할 태그
       - attr : 클래스 등의 속성들

   - ```python
     import bs4
     from selenium import webdriver as wd

     ...

     opt = wd.ChromeOptions()
     opt.add_argument("headless")

     driver = wd.Chrome("./chromedriver", chrome_options=opt)
     driver.get(url)

     # 페이지의 검색결과가 로딩되는 시간의 유예를 둠
     time.sleep(3)

     ...

     # page_source를 불러오고 html.parser를 사용
     # 검색 조건에 맞는 모든 결과를 가져온다
     soup = bs4.BeautifulSoup(pageString, "html.parser")
     hashtags = soup.find_all(
         name="div", attrs={"class": "AC7dP Igw0E IwRSH eGOV_ _4EzTm YlhBV XTCZH"}
     )
     ```

   - 인스타그램에서 해시태그 등을 이용한 데이터 분석 중
