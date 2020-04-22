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

    df = pd.read_csv("./store.csv")
    print(df)


    return df


def crawl(keyword, driver):

    # keyword = ""

    # keyword = "BBQ치킨"
    url_info = "https://www.google.com/search?q="+keyword+"&tbm=isch"
    driver.get(url_info)

    headers={'User-Agent': 'Mozila/5.0'}

    time.sleep(3)
    # driver.get(url)

    pageString = driver.page_source

    bsObj = BeautifulSoup(pageString, "lxml")

    image = bsObj.find(name="img", attrs={"class":"rg_i Q4LuWd tx8vtf"})
    src = image.get("src")

    print("이미지 가져오기")

    return src


def main():

    dataframes = read_csv()
    driver = wd.Chrome("./chromedriver.exe")
    csvtxt = []
    #  dataframes.index
    for i in tqdm(range(0,1000)):
        csvtxt.append([])
        keyword = dataframes.loc[i, "store_name"]
        img_src = crawl(keyword, driver)

        img_filename = "img_" + str(dataframes.loc[i, "id"]) + "_" + keyword

        urlretrieve(img_src, "./img/"+img_filename+".jpg")

        csvtxt[i].append(img_filename)
        # print(csvtxt)

    data = pd.DataFrame(csvtxt)
    data.to_csv("./images.txt", encoding="utf-8")

        

if __name__ == '__main__':
    main()
    