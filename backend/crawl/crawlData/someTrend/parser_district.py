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
from PyQt5 import QtCore, QtWidgets

# from crawl import models
import time
import re
import json

# 장소를 기준으로 가져옵니다.

def crawled(data, driver):
    global num

    ids = []
    rank = []
    feelings = []
    keywords = []

    # opt = wd.ChromeOptions()
    # opt.add_argument("headless")

    # driver = wd.Chrome("./chromedriver", chrome_options=opt)

    time.sleep(3)

    search = driver.find_element_by_id("searchKeyword")
    search.clear()
    search.send_keys(data)

    button = driver.find_element_by_xpath("//*[@id='searchKeywordClick']")
    button.click()

    time.sleep(5)
    driver.implicitly_wait(3)

    # Login process 생각 중

    # -------------------------------------------
    try:

        pageString = driver.find_element_by_tag_name('html').find_element_by_css_selector(
            "div#issueSentimentSlick > div > div > div.slick-slide.slick-current.slick-active > div.sensitiveTable_wrap > div")

        bsObj = BeautifulSoup(pageString.get_attribute('innerHTML'), 'lxml')

        table = bsObj.find(
            'table', {'class': 'relation_table sensitive_table'})
        # print(table)
        trs = table.find_all('tr')

    # enumerate를 사용 시, 해당 값의 인덱스를 알 수 있다..?
        for idx, tr in enumerate(trs):
            if idx > 0:
                tds = tr.find_all('td')
            # td에서 필요한 건, 순위, 분류, 키워드만 필요. 총 3개
                ids.append(num)
                num += 1
                rank.append(tds[0].text)
                feelings.append(tds[1].span.text)
                keywords.append(tds[2].span.text)

        # print(rank)
        # print(feelings)
        # print(keywords)
        # print(type(rank))
        district = []
        for i in range(0, len(rank)):
            district.append(data)

        print(district)

        frames = {
            "id": ids,
            "ftype": feelings,
            "word": keywords,
            "rank": rank,
            "district": district
        }

        dataframes = pd.DataFrame.from_dict(frames)
        # print(dataframes)
    except Exception as e:
        print("Error Message : ", e)

    return dataframes

# store와 location에 대해 계속 반복하기


global num
num = 1


def main():

    url = "https://some.co.kr/analysis/issue"

    driver = wd.Chrome("chromedriver")
    driver.get(url)

    df1 = pd.DataFrame()

    districts = [
        "강동구", "관악구", "광진구", "강북구", "노원구", "은평구", "강서구", "도봉구", "양천구", "중랑구", "마포구",
        "동작구", "용산구", "금천구", "송파구", "강남구", "성북구", "성동구", "구로구",
        "서대문구", "동대문구", "중구", "영등포구", "종로구", "서초구",
    ]

    for keyword in districts:
        print(keyword)
        df2 = crawled(keyword, driver)

        df1 = pd.concat([df1, df2])
    
    # read_csv()
    data = df1.set_index("id")
    data.to_csv("./data/district_sense.csv", encoding="utf-8")


if __name__ == "__main__":
    main()
