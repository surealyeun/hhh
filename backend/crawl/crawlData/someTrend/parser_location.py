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
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote_plus
from PyQt5 import QtCore, QtWidgets

# from crawl import models
import time
import re
import json

# 장소를 기준으로 가져옵니다.


def read_csv():

    df = pd.read_csv("../location_full.csv")

    return df


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
    if len(data.location_name) > 20:
            search.send_keys(data.location_name[0:20])
    
    else:
        search.send_keys(data.location_name)

    # button = driver.find_element_by_xpath("//*[@id='searchKeywordClick']")
    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='searchKeywordClick']")))
    button.send_keys(Keys.ENTER)

    time.sleep(5)
    driver.implicitly_wait(3)

    ## Login process 생각 중
    
    ## -------------------------------------------
    try:
    
        pageString = driver.find_element_by_tag_name('html').find_element_by_css_selector("div#issueSentimentSlick > div > div > div.slick-slide.slick-current.slick-active > div.sensitiveTable_wrap > div")
        # print(type(pageString))
        # print(pageString)
        # print(pageString.get_attribute('innerHTML'))
        # print(type(pageString.get_attribute('innerHTML')))
        
        bsObj = BeautifulSoup(pageString.get_attribute('innerHTML'), 'lxml')

        table = bsObj.find('table', {'class' : 'relation_table sensitive_table'})
        # print(table)
        trs = table.find_all('tr')
    
    #enumerate를 사용 시, 해당 값의 인덱스를 알 수 있다..?
        for idx, tr in enumerate(trs):
            if idx > 0:
                tds = tr.find_all('td')
            # td에서 필요한 건, 순위, 분류, 키워드만 필요. 총 3개
                ids.append(num)
                num+=1
                rank.append(tds[0].text)
                feelings.append(tds[1].span.text)
                keywords.append(tds[2].span.text)

        location = []
        for i in range(0 ,len(rank)):
            location.append(data.id)
        
        # print(location)

        frames = {
            "id" : ids,
            "ftype" : feelings,
            "word" : keywords,
            "rank" : rank,
            "location" : location
        }

        dataframes = pd.DataFrame.from_dict(frames)
        # print(dataframes)
    except Exception as e:
        print("Error Message : ", e)
    
    finally:
        return dataframes

# store와 location에 대해 계속 반복하기

global num
num = 1

def main():
    print("안녕")

    url = "https://some.co.kr/analysis/issue"

    opt = wd.ChromeOptions()
    opt.add_argument("headless")
    
    driver = wd.Chrome("./chromedriver", chrome_options=opt)
    driver.get(url)

    dataframes = read_csv()
    df1 = pd.DataFrame()
    
    for idx in tqdm(range(0,1310)):
        print(dataframes.loc[idx, ["id", "location_name"]])
        df2 = crawled(dataframes.loc[idx, ["id", "location_name"]], driver)

        df1 = pd.concat([df1, df2])
    
        data = df1.set_index("id")
        data.to_csv("./data/location_sense_rest.csv", encoding="utf-8")



if __name__ == "__main__":
    main()
