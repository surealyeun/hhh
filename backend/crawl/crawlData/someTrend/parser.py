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


def read_csv():

    df = pd.read_csv("./store.csv")
    print(df)

    # for d in df.index:

    #     # df에서 가게명만 뽑아오기
    #     search = df.loc[d, "store_name"]
    #     print(df.loc[d, ["id", "store_name"]])


    return df


def crawled(dataframes):

    rank = []
    feelings = []
    keywords = []

    url = "https://some.co.kr/analysis/issue"

    # opt = wd.ChromeOptions()
    # opt.add_argument("headless")
    
    # driver = wd.Chrome("./chromedriver", chrome_options=opt)
    driver = wd.Chrome("chromedriver")
    driver.get(url)
    
    time.sleep(3)

    # dataframe들 반복하기
    # for data in dataframes:
    #     print(data)

    search = driver.find_element_by_id("searchKeyword")
    search.clear()
    search.send_keys("BBQ")

    button = driver.find_element_by_xpath("//*[@id='searchKeywordClick']")
    button.click()

    time.sleep(5)
    driver.implicitly_wait(3)

    ## Login process 생각 중
    
    ## -------------------------------------------
    try:
    
        pageString = driver.find_element_by_tag_name('html').find_element_by_css_selector("div#issueSentimentSlick > div > div > div.slick-slide.slick-current.slick-active > div.sensitiveTable_wrap > div")
        print(type(pageString))
        print(pageString)
        print(pageString.get_attribute('innerHTML'))
        print(type(pageString.get_attribute('innerHTML')))
        
        bsObj = BeautifulSoup(pageString.get_attribute('innerHTML'), 'lxml', from_encoding='utf-8')

        table = bsObj.find('table', {'class' : 'relation_table sensitive_table'})
        print(table)
        trs = table.find_all('tr')
    
    #enumerate를 사용 시, 해당 값의 인덱스를 알 수 있다..?
        for idx, tr in enumerate(trs):
            if idx > 0:
                tds = tr.find_all('td')
            # td에서 필요한 건, 순위, 분류, 키워드만 필요. 총 3개
                rank.append(tds[0].text)
                feelings.append(tds[1].span.text)
                keywords.append(tds[2].span.text)


        print(rank)
        print(feelings)
        print(keywords)
        
    except Exception as e:
        print("에러", e)
    
    
    return 0

# store와 location에 대해 계속 반복하기


def main():
    print("안녕")
    data = crawled(read_csv())
    # read_csv()
    # print(data)
    print("제발..")


if __name__ == "__main__":
    main()
