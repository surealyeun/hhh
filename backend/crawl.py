import requests
import bs4
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re
import json

keyword = "가로수길"

# 태그 입력하여 검색
# keyword = input("검색할 태그를 입력하세요 : ")

url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

instargram_tags = []
instargram_tag_dates = []

opt = wd.ChromeOptions()
opt.add_argument("headless")

driver = wd.Chrome("./chromedriver", chrome_options=opt)
driver.get(url)
time.sleep(3)

pageString = driver.page_source
# print(pageString)

soup = bs4.BeautifulSoup(pageString, "html.parser")
hashtags = soup.find_all(
    name="div", attrs={"class": "AC7dP Igw0E IwRSH eGOV_ _4EzTm YlhBV XTCZH"}
)

data = {}

n = 1
# print(hashtags)
for i in hashtags:
    print(i.a.text)
    data[str(n)] = i.a.text
    n += 1

print(data)

with open("./crawlData/tags.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent="\t")

driver.quit()
