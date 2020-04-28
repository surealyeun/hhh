import pandas as pd
import csv
import requests as req
import argparse as ap
from tqdm import tqdm
from urllib.request import urlopen, Request, urlretrieve
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

    df = pd.read_csv("../store.csv")
    print(df)


    return df

def isNaN(num):
    return num != num


def crawl(keyword, driver):
    
   
    url_info = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+keyword
    driver.get(url_info)

    headers={'User-Agent': 'Mozila/5.0'}

    time.sleep(3)
   
    
    pageString = driver.find_element_by_tag_name('html').find_element_by_css_selector("#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb")
    # pageString = driver.page_source
    print(type(pageString))

    bsObj = BeautifulSoup(pageString.get_attribute('innerHTML'), "lxml")
   
    image = bsObj.find("img",{"class":"_img"})
    src = image.get("src")
    print(src)
    print("이미지 가져오기")

    return src

def main():

    dataframes = read_csv()
    driver = wd.Chrome("./chromedriver.exe")
    csvtxt = []
    print(dataframes)


    # for i in tqdm(range(0,1000)):
    for i in tqdm(range(0, 10)):
        keyword = ""
        
        if isNaN(dataframes.loc[i, "branch"]) is False:
            keyword = dataframes.loc[i, "store_name"] + " " + str(dataframes.loc[i, "branch"])
            if isNaN(dataframes.loc[i, "area"]) is False:
                keyword = keyword + " " + dataframes.loc[i, "area"]

        else:
            keyword = dataframes.loc[i, "store_name"]
            if isNaN(dataframes.loc[i, "area"]) is False:

                keyword = keyword + " " + dataframes.loc[i, "area"]

        print(keyword)
        
        img_src = crawl(quote_plus(keyword), driver)

        print(type(keyword.find("/")))
        if keyword.find("/") != -1:
            keyword.replace("/", "-")

                   
        # img_filename = "img_" + str(dataframes.loc[i, "id"]) + "_" + keyword

        # urlretrieve(img_src, "./img/"+img_filename+".jpg")

        # csvtxt[i].append(img_filename)
        csvtxt.append([i+1])
        csvtxt[i].append(img_src)
        csvtxt[i].append(dataframes.loc[i, "id"])
        # print(csvtxt)

    data = pd.DataFrame(csvtxt, columns=["id" ,"src", "store"])
    # print()?
    data_set = data.set_index("id")
    data_set.to_csv("./data/store_images.csv", encoding="utf-8")

        

if __name__ == '__main__':
    main()
    