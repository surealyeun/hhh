import os
import webbrowser
import itertools
import pandas as pd
import folium
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import requests
import json
import numpy as np
from folium import plugins
from collections import Counter
from parse import load_dataframes
from pandas.io.json import json_normalize




def set_config():
    # 폰트, 그래프 색상 설정
    font_list = fm.findSystemFonts(fontpaths=None, fontext="ttf")
    if any(["notosanscjk" in font.lower() for font in font_list]):
        plt.rcParams["font.family"] = "Noto Sans CJK JP"
    else:
        if not any(["malgun" in font.lower() for font in font_list]):
            raise Exception(
                "Font missing, please install Noto Sans CJK or Malgun Gothic. If you're using ubuntu, try `sudo apt install fonts-noto-cjk`"
            )

        plt.rcParams["font.family"] = "Malgun Gothic"

    sns.set_palette(sns.color_palette("Spectral"))
    plt.rc("xtick", labelsize=6)


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
    print(result["hotplace_result"])
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

    inner_html = '<b>Hello world</b><br/><a href="#">hi!</a>'
    test = folium.Html(inner_html, script=True)

    popup = folium.Popup(test, max_width=2650)
    folium.RegularPolygonMarker(
        location=[37.503309,126.7636763], popup=popup,
    ).add_to(m)

    folium.LayerControl().add_to(m)
    m.save('./frontend/hhh/public/map.html')

def main():
    set_config()
    data = load_dataframes()
    show_stores_distribution_graph(data)

if __name__ == "__main__":
    main()
