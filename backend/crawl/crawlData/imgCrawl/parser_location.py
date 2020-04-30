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
import base64
import time
import re
import json

# 장소를 기준으로 가져옵니다.


def read_csv():

    df = pd.read_csv("../location_full.csv")
    print(df)


    return df

def isNaN(num):
    return num != num


def crawl(keyword, driver):

    # keyword = ""

    # keyword = "BBQ치킨"
    # url_info = "https://www.google.com/search?q="+keyword+"&tbm=isch"
    url_info = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+keyword
    driver.get(url_info)

    headers={'User-Agent': 'Mozila/5.0'}

    time.sleep(3)
    # driver.get(url)
    # image_link = driver.find_element_by_xpath("//*[@id='islrg']/div[1]/div[1]/a[1]")
    # image_link.click()
    try:

        if driver.find_element_by_tag_name('html').find_element_by_css_selector("#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb") is None:
        
            pageString = None

        else:
            pageString=driver.find_element_by_tag_name('html').find_element_by_css_selector("#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb")
    
        print(type(pageString))

        bsObj = BeautifulSoup(pageString.get_attribute('innerHTML'), "lxml")
   
        image = bsObj.find("img",{"class":"_img"})
        src = image.get("src")
        print(src)

        print("이미지 가져오기")

        return src
    except Exception as e:
        print(e)
        return None


def main():

    dataframes = read_csv()
    opt = wd.ChromeOptions()
    opt.add_argument("headless")
    
    driver = wd.Chrome("./chromedriver", chrome_options=opt)
    # driver = wd.Chrome("./chromedriver.exe")
    csvtxt = []


    for i in tqdm(range(0,1310)):
    # for i in tqdm(range(0, 10)):
        keyword = ""
        
        # if isNaN(dataframes.loc[i, "address_see"]) is False:
        #     keyword = dataframes.loc[i, "location_name"] + " " + str(dataframes.loc[i, "address_see"])
        #     if isNaN(dataframes.loc[i, "address_gu"]) is False:
        #         keyword = keyword + " " + dataframes.loc[i, "address_gu"]

        # else:
        keyword = dataframes.loc[i, "location_name"]
        if isNaN(dataframes.loc[i, "address_gu"]) is False:
             keyword = keyword + " " + dataframes.loc[i, "address_gu"]

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

    data = pd.DataFrame(csvtxt, columns=["id" ,"store", "src"])
    # print()?
    data_set = data.set_index("id")
    data_set.to_csv("./data/location_images.csv", encoding="utf-8")

        

if __name__ == '__main__':
    main()
    