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

     + 기본적으노 html.parser 를 지원하지만 lxml이 더 빠르다.
       + `pip install lxml`
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

     + 사용한 라이브러리들
   
       ```python
       import pandas as pd
       import csv
       import requests
       from tqdm import tqdm
       from urllib.request import urlopen, Request
       from bs4 import BeautifulSoup
       from selenium import webdriver as wd
       from selenium.webdriver.common.by import By
       from selenium.webdriver.support.ui import WebDriverWait
       from selenium.webdriver.support import expected_conditions as EC
    from urllib.parse import quote_plus
       ```

       + tqdm : 상태바 라이브러리. 현재 진행률을 시각적으로 보여준다.

       + urllib : URL을 통해 여러 작업 수행

         + request : url 요청을 위한 클래스나 함수들이 정의되어있음

           + Request : url 요청을 추상화

             + *url, data=None, headers = {}, origin_req_host=None, unverifiable=False, method=None

             + *url* 인자에는 유효한 URL의 문자열을 넣습니다.

               *data* 인자에는 요청에 대한 추가 데이터의 객체를 지정하거나 None을 지정합니다.

               *headers* 인자에는 요청에 필요한 헤더를 넣어줍니다. 여기에 들어갈 인자는 Dictionary형이어야 합니다.

               *origin_req_host* 인자에는 원본 트랙잭션의 요청 호스트를 지정합니다. 기본 값은 URL을 요청한 호스트입니다.

               *unverifiable* 인자에는 요청에 대해 검증할 수 없는지의 여부(True / False)를 지정합니다. 기본 값은 False 입니다.

               *method* 인자에는 HTTP 요청 메소드가 들어갑니다. 기본 값은 GET이고 HEAD, POST 등을 지정할 수 있습니다.

           + urlopen : url을 인스턴스화 해줌.

         + parse : url 구문을 분석하기 위한 함수들

           + quote_plus : 인자로 주어진 문자열에서 특수문자를 문자열로 변환해서 반환. 공백은 +로.

         

       + 주어진 가게명을 가지고 검색을 한다.
   
         1. 검색된 태그에서 총 게시물의 개수를 가져온다.
         2. 



