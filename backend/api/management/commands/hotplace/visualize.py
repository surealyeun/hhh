import os
import webbrowser
import itertools
import pandas as pd
import folium
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
import numpy as np
from folium import plugins
from collections import Counter
from parse import load_dataframes
from pandas.io.json import json_normalize


def show_stores_distribution_graph(dataframes):
    """
        핫 플레이스 분포를 지도에 표시.
    """
    m = folium.Map(
        location=[37.503309,126.7636763],
        zoom_start=13
    )
    result = pd.read_pickle('./data/hot_place.pkl')

    sigugun_income = './data/seoul_border.json'
    geo_str = json.load(open(sigugun_income, encoding='utf-8'))
    m = folium.Map(location=[37.5553542, 126.9803419], tiles='Stamen Toner', zoom_start=11)
    df = result["hotplace_result"]
    folium.Choropleth(
        geo_data = geo_str,
        data = df,
        name='H H H',
        columns = ('gu','score'),
        fill_color = 'YlGn', #puRd, YlGnBu
        key_on = 'feature.properties.SIG_KOR_NM',
        fill_opacity=0.75,
        line_opacity=0.9, 
        legend_name="Hot Place Score",
        tooltip=df.index
    ).add_to(m)

    """ 서울 구 중심좌표 설정 """
    seoul_gu_center_dic = {
        "lon":[
            126.97942, 126.997985, 126.981987, 127.043114,
            127.088351, 127.057221, 127.095157, 127.019697, 
            127.01327, 127.034471, 127.077134, 126.929119, 
            126.94115, 126.910326, 126.857526, 126.825859, 
            126.858451, 126.902894, 126.912303, 126.953734, 
            126.947435, 127.033245, 127.065334, 127.118003, 
            127.149107
        ],
        "lat":[
            37.592128, 37.557335, 37.528582, 37.54824,
            37.543059, 37.579132, 37.595194, 37.602917,
            37.640710, 37.66633, 37.649734, 37.616431,
            37.574997, 37.556708, 37.52194, 37.55844,
            37.491581, 37.457775, 37.519739, 37.496075,
            37.464570, 37.470740, 37.494712, 37.502168,
            37.547522
        ],
        "gu":[
            "종로구", "중구", "용산구", "성동구",
            "광진구", "동대문구", "중랑구", "성북구",
            "강북구", "도봉구", "노원구", "은평구",
            "서대문구", "마포구", "양천구", "강서구",
            "구로구", "금천구", "영등포구", "동작구",
            "관악구", "서초구", "강남구", "송파구",
            "강동구"
        ]
    }
    center_dataframe = pd.DataFrame(seoul_gu_center_dic)

    """ 구별 주요 키워드 리스트화 """

    """ 단일 마커 추가 코드 (사전작업: 해당 주소지만 걸러주는 url 만들어놓기)"""
    
    """ 서울시 구 갯수만큼 for문 """
    for i in center_dataframe.index[0:]: 
        inner_html = '<b>' + center_dataframe.loc[i, 'gu'] + '</b><br/><a href="'+'https://www.google.com'+'">hi!</a>'
        test = folium.Html(inner_html, script=True)

        popup = folium.Popup(test, max_width=2650)

        folium.Circle( 
            location = center_dataframe.loc[i, ['lat', 'lon']], 
            tooltip = center_dataframe.loc[i, 'gu'], 
            radius = 500,
            color = '#00ffaa',
            opacity = 0.7,
            fill_color = '#00ffaa',
            fill_opacity = 0.4,
            popup= popup
        ).add_to(m)
    m.save('./frontend/hhh/public/map.html')

def main():
    data = load_dataframes()
    show_stores_distribution_graph(data)

if __name__ == "__main__":
    main()
