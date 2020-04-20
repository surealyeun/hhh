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

import time
import re
import json

# 장소를 기준으로 가져옵니다.

df = pd.read_csv("./store.csv")
print(df.drop_duplicates())
df_droped = df.drop_duplicates()
print(df_droped.count())


baseUrl = "https://www.instagram.com/explore/tags/"
plusUrl = input('검색할 태그를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl)

print("Chrome Driver를 실행합니다.")
opt = wd.ChromeOptions()
opt.add_argument("headless")

driver = wd.Chrome("../chromedriver", chrome_options=opt)
driver.get(url)
time.sleep(3)

# 총 게시물 숫자 불러오기
pageString = driver.page_source
bsObj = BeautifulSoup(pageString, 'lxml')

# print(bsObj)