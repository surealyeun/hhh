# Web Crawling

> ### 주의사항

+ 대상 웹 페이지 조건 확인 - robots.txt
+ 크롤러 분류 - 상태 유무, JavaScript 유무
+ Request 요청 주의 할 점 - 서버 부하 고려
+ 콘텐츠 저작권 문제
+ 페이지 구조 변경 가능성 숙지



> ### 크롤링하기



1. selenium 설치 

   + selenium : 인터넷 브라우저 컨트롤러

   + 브라우저를 이용해 특정 사이트에 접속, 동작하고, 크롤링

   + 인스타그램 등 javascript를 사용하여 페이지를 스크롤할 때 새로운 게시글을 불러오는 방식에 사용

     ```python
     from selenium import webdriver
     ```

   + pip install selenium

   

2. chrome 드라이버 설치

   + [크롬 드라이버 설치](https://sites.google.com/a/chromium.org/chromedriver/downloads/version-selection)
   + 설정 - Chrome 버전을 확인하고 해당하는 드라이버를 설치해야된다.
   + 현재 버전 : [ 80.0.3987.106]

   

3. 크롤링

   + driver

     + page_source : 페이지의 html 코드를 가져옴

   + beautifulsoup

     + find_all : 해당 되는 조건에 맞는 모든 결과 검색
       + name : 검색할 태그
       + attr : 클래스 등의 속성들

   + ```python
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

   + 인스타그램에서 해시태그 등을 이용한 데이터 분석 중



