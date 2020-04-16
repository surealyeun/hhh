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

